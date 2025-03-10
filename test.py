import ollama
question = "Should I invest in Apple stock?"
# Load the DeepSeek 1.5B model
model_name = "deepseek-r1:1.5b"
# Generate a response
response = ollama.chat(model=model_name, messages=[{"role": "user", "content": question}])
print(response["message"]["content"])