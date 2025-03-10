import ollama

class ollamamodel:
    def __init__(self):
        pass
    def ask_ollama(self,question):
        # Load the DeepSeek 1.5B model
        model_name = "deepseek-r1:1.5b"
        # Generate a response
        response = ollama.chat(model=model_name, messages=[{"role": "user", "content": question}])

        # Return the response
        return(response["message"]["content"])
