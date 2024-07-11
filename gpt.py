import time
import tkinter as tk
from langchain_community.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = LlamaCpp(
    model_path="models/llama-2-7b-chat.Q5_K_M.gguf",
    n_gpu_layers=40,
    n_batch=512,
    verbose=False,
)

template = """
Question: {question}

Answer:
"""
prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt, llm=llm)


def get_response():
    question = entry.get()
    answer = llm_chain.run(question)
    response.config(state=tk.NORMAL)
    response.delete(1.0, tk.END)
    response.insert(tk.END, answer)
    response.config(state=tk.DISABLED)


root = tk.Tk()
root.title("local-GPT")

init_label = tk.Label(root, text="Initializing chatbot...")
init_label.pack(pady=20)

root.withdraw()

print("Chatbot initializing...")

time.sleep(3)

root.deiconify()

init_label.pack_forget()

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Ask", command=get_response)
button.pack()

response = tk.Text(root, width=60, height=10, wrap=tk.WORD)
response.pack(pady=20)
response.config(state=tk.DISABLED)

root.mainloop()
