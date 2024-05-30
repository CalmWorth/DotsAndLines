# text_handler.py

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import sys

class TextHandler:
    """This class allows to redirect stdout and stderr to a tkinter Text widget."""
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.text_widget.config(state=tk.DISABLED)
        self.text_widget.bind("<1>", lambda event: self.text_widget.focus_set())

    def write(self, message):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)
        self.text_widget.config(state=tk.DISABLED)

    def flush(self):
        pass

    def clear(self):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.config(state=tk.DISABLED)
