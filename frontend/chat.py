# chat.py
import tkinter as tk
from tkinter import scrolledtext
from bot import check_for_numbers  # Import the function from bot.py
from aiBackend import create_thread_and_run, get_response, wait_on_run, submit_message, MEDICAL_ASSISTANT_ID, pretty_print

def center_window(root, width, height):
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates for the Tk root window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    # Set the dimensions and position
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

class ChatApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")

        self.root.geometry('800x850')
        self.root.resizable(width=False, height=False)

        self.chat_display = scrolledtext.ScrolledText(self.root, width=90, height=50, state='disabled')
        self.chat_display.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        self.text_input = tk.Entry(self.root, width=70)
        self.text_input.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        self.root.grid_columnconfigure(0, weight=1)
        self.thread1, self.run1 = create_thread_and_run("Hello")

    def send_message(self):
        message = self.text_input.get().strip()
        if message:  # Only process non-empty messages
            self.update_chat_display(f"You: {message}")
            print(f"You: {message}")  # Print message to the terminal

            

            self.run1 = submit_message(MEDICAL_ASSISTANT_ID, self.thread1, message)

            self.run1 = wait_on_run(self.run1, self.thread1)
            

            # Check message for numbers using bot.py
            bot_response = pretty_print(get_response(self.thread1))
            if bot_response:
                self.update_chat_display(f"Bot: {bot_response}")
                print(f"Bot: {bot_response}")  # Also print bot's response to the terminal

            self.text_input.delete(0, tk.END)  # Clear the input field after sending the message

    def update_chat_display(self, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)


def start_chat_app():
    root = tk.Tk()
    center_window(root, 800, 800)  # Adjust width and height if different dimensions are desired
    app = ChatApplication(root)
    root.mainloop()
