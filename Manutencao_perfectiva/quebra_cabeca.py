import tkinter as tk
from tkinter import simpledialog

class QuebraCabeca:
    def __init__(self, root):
        self.root = root

    def solve(self):
        answer = simpledialog.askstring("Enigma", "Quanto mais você tira de mim, maior eu fico. O que sou?")
        if answer and answer.lower() in ["buraco", "BURACO"]:
            return True
        return False