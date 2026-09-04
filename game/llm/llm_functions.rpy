init -10 python:
    import os
    import threading
    import queue
    import time
    import uuid

    from pathlib import Path
    from datetime import datetime
    from llm.core import post, hasInternet

    files_dir = None

    if renpy.mobile:
        files_dir = Path(config.savedir).parent
    else:
        files_dir = config.basedir

    def user_language() -> str:
        lang = getattr(persistent, "choosen_language", None)

        return lang or "English"

    def sanitize_llm_output(text : str) -> list:
        lines = text.strip().split("\n")
        clean = []

        for line in lines:
            line = line.strip()
            if not line:
                continue
            clean.append(line)

        return clean
    
    def log_ia_interaction(prompt_text: str, user_input: str, raw_output: str, response_list: list, log_type: set[str]) -> None:
        logs = {
            "prompt": ("[LLM PROMPT]", prompt_text),
            "input": ("[PLAYER INPUT]", user_input),
            "raw_output": ("[LLM RAW OUTPUT]", raw_output),
            "response": ("[LLM RESPONSE LIST]", response_list)
        }

        for key in log_type:
            if key in logs:
                title, content = logs[key]
                print(title)
                print(content)
    
    def log_error(filename, error):
        log_file_path = os.path.join(files_dir, f"{filename}.txt")

        with open(log_file_path, "w", encoding="utf-8") as log_file:
            log_file.write("I'm sorry, but an uncaught exception occurred.\n\n")
            log_file.write(f"{error}")
            log_file.write("\n\n")
            log_file.write(f"{renpy.version()}\n")
            log_file.write(f"{config.name} {config.version}\n")
            log_file.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            log_file.write("If you're sure this error is not caused by a specific case, or is persistent and are unsure how to fix,\nplease report it through an issue on the game's repository: https://github.com/AndreyFernandes-NP/Tsukiyo-no-Sentaku/issues")

    def generate_response(system_prompt:str, player_input:str, reasoning_effort:str = "medium", text_verbosity:str = "medium", response_size:int = 256, log_response:bool = False, log_type:set[str] | None = None) -> list[str]:
        if log_type is None:
            log_type = set()

        response_size = max(16, min(int(response_size), 1024))
        
        payload = {
            "system_prompt": system_prompt,
            "player_input": player_input,
            "reasoning_effort": reasoning_effort,
            "text_verbosity": text_verbosity,
            "response_size": response_size
        }

        if not hasInternet():
            print("Warning: No internet connection available.")
            renpy.notify([f"{ERROR_PROTOCOL['generic']}", f"{ERROR_MESSAGES['no_internet']}"])
            return []

        status, data = post(payload)

        if not data.get("ok", False):
            print(f"URL Request Failed. Status='{status}' \nData={data}")
            renpy.notify([f"{ERROR_PROTOCOL['http']}", f"{ERROR_MESSAGES['http_failure']}"])
            log_error("http_log", f"Status: {status}\nData: {data}")
            return []

        raw_output = data.get("output_text", "")
        response_text = sanitize_llm_output(raw_output)

        if log_response:
            log_ia_interaction(system_prompt, player_input, raw_output, response_text, log_type)
        
        return response_text

    def _llm_warmup() -> None:
        try:
            response = generate_response(
                system_prompt="Always answer Pong!",
                player_input="Ping!",
                reasoning_effort="none",
                text_verbosity="low",
                response_size=16,
                log_response=False
            )

            if response:
                print("Ping -", response[0])

        except Exception as e:
            print(f"LLM Warmup failed: {e}")
            renpy.notify([f"{ERROR_PROTOCOL['llm']}", f"{ERROR_MESSAGES['llm_warmup_failure']}"])
            log_error("llm_log", f"LLM Warmup failed with exception: {e}")
    
    def start_llm_warmup() -> None:
        t = threading.Thread(target=_llm_warmup, daemon=True)
        t.start()
    
    class LLMJob:
        def __init__(self):
            self.id = str(uuid.uuid4())
            self.done = False
            self.result = []   # list[str]
            self.error = None  # Exception | None
    
    def llm_request(system_prompt: str, player_input: str, reasoning: str = "medium", verbosity: str = "medium", response_size: int = 256,
                    log_response: bool = False, log_type: set[str] | None = None) -> LLMJob:

        job = LLMJob()

        def _worker():
            try:
                job.result = generate_response(
                    system_prompt=system_prompt,
                    player_input=player_input,
                    reasoning_effort=reasoning,
                    text_verbosity=verbosity,
                    response_size=response_size,
                    log_response=log_response,
                    log_type=log_type
                )
            except Exception as e:
                job.error = e
                job.result = []
            finally:
                job.done = True

        threading.Thread(target=_worker, daemon=True).start()
        return job
