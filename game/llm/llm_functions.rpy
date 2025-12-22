init -10 python:
    import threading
    from llm.core import post

    def user_language() -> str:
        lang = getattr(persistent, "choosen_language", None)

        if not lang:
            return "English"

        return lang

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

        response_size = max(16, min(int(response_size), 512))
        
        payload = {
            "system_prompt": system_prompt,
            "player_input": player_input,
            "reasoning_effort": reasoning_effort,
            "text_verbosity": text_verbosity,
            "response_size": response_size
        }

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

            print("AI says:", response[-1])

        except Exception as e:
            print(f"LLM Warmup failed: {e}")
    
    def start_llm_warmup() -> None:
        t = threading.Thread(target=_llm_warmup, daemon=True)
        t.start()