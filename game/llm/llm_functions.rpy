init -10 python:
    import threading
    import queue
    import time
    import uuid
    from llm.core import post, hasInternet

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
            return []

        status, data = post(payload)

        if not data['ok']:
            print(f"URL Error: {data}")
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
