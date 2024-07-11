# local-GPT

**local-GPT** is a simple graphical user interface (GUI) application built using Tkinter and LlamaCpp for interacting with a pretrained language model.

## Installation

1. **Download the Model:**
   - You can download a demo model from [here](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF).
   - Place the downloaded `.gguf` model file into a `models` folder in your project directory.

2. **Setup:**
   - Ensure you have Python installed on your system.
   - Install required Python packages:
     ```
     pip install langchain-community tkinter
     ```

3. **Run the Application:**
   - Navigate to your project directory where the `local-GPT.py` file is located.
   - Run the application:
     ```
     python gpt.py
     ```

## Usage

- After running the application, a GUI window titled "local-GPT" will appear.
- Input your question in the text entry box and click the "Ask" button to receive a response from the chatbot.
- Responses will be displayed in the text area below the input box.

## Notes

- This application uses LlamaCpp for language model inference.
- Ensure the `models` folder contains the pretrained model file (`llama-2-7b-chat.Q5_K_M.gguf`) for proper functioning.
- Adjustments may be needed based on your system's environment and setup.
