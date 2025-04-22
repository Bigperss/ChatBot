from openai import OpenAI
import tiktoken

class Bot:
    def __init__(self, system_promt:str, model:str, max_token:int, api_key:str = "ollama"):
        self.model = model
        self.system_prompt = system_promt
        self.message_history = (
            [{"role": "system", "content": self.system_prompt}]
            if len(self.system_prompt.strip()) > 0 else []
        )
        self.max_token = max_token
        self.openai = OpenAI(base_url="http://localhost:11434/v1", api_key=api_key)
        self.encoding = tiktoken.get_encoding("cl100k_base")

    def total_tokens(self, messages):
        return sum(len(self.encoding.encode(m["content"])) for m in messages)
    
    def ask(self, new_message: str):
        if len(self.encoding.encode(new_message)) > self.max_token:
            yield "Too long message, please take care of me."
            return

        self.message_history.append({"role": "user", "content": new_message})
        while self.total_tokens(self.message_history) > self.max_token and len(self.message_history) > 1:
            self.message_history.pop(1)

        response = self.openai.chat.completions.create(
            model=self.model,
            messages=self.message_history,
            stream=True,
        )
        full_reply = ""
        for chunk in response:
            delta = chunk.choices[0].delta
            if hasattr(delta, "content") and delta.content is not None:
                full_reply += delta.content
                yield delta.content
        self.message_history.append({"role": "assistant", "content": full_reply})