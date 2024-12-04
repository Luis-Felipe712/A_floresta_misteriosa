import tkinter as tk
import random

class Combate:
    def __init__(self, root, enemy, player_health):
        self.root = root
        self.enemy = enemy
        self.player_health = player_health
        self.result = None

    def start_combat(self):
        self.window = tk.Toplevel(self.root)
        self.window.title("Combate!")
        self.window.geometry("400x300")
        self.window.configure(bg="#2c3e50")

        self.info = tk.Label(self.window, text=f"Você encontrou um {self.enemy['nome']}!", font=("Arial", 16), bg="#2c3e50", fg="#ecf0f1")
        self.info.pack(pady=10)

        self.player_health_label = tk.Label(self.window, text=f"Vida do Jogador: {self.player_health}", font=("Arial", 14), bg="#2c3e50", fg="#ecf0f1")
        self.player_health_label.pack()

        self.enemy_health_label = tk.Label(self.window, text=f"Vida do {self.enemy['nome']}: {self.enemy['vida']}", font=("Arial", 14), bg="#2c3e50", fg="#ecf0f1")
        self.enemy_health_label.pack()

        self.action_frame = tk.Frame(self.window, bg="#2c3e50")
        self.action_frame.pack(pady=20)

        tk.Button(self.action_frame, text="Atacar", command=self.attack, bg="#16a085", fg="white", font=("Arial", 14)).pack(side=tk.LEFT, padx=10)
        tk.Button(self.action_frame, text="Fugir", command=self.run_away, bg="#e74c3c", fg="white", font=("Arial", 14)).pack(side=tk.RIGHT, padx=10)

        self.window.grab_set()
        self.window.wait_window()

        return self.player_health

    def attack(self):
        player_damage = random.randint(5, 15)
        enemy_damage = random.randint(0, self.enemy['ataque'])

        self.enemy["vida"] -= player_damage
        self.player_health -= enemy_damage

        self.update_labels()

        if self.enemy["vida"] <= 0:
            self.info.config(text=f"Você derrotou o {self.enemy['nome']}!")
            self.window.after(1500, self.window.destroy)
        elif self.player_health <= 0:
            self.info.config(text="Você foi derrotado!")
            self.window.after(1500, self.window.destroy)

    def run_away(self):
        self.info.config(text="Você fugiu do combate!")
        self.window.after(1500, self.window.destroy)

    def update_labels(self):
        self.player_health_label.config(text=f"Vida do Jogador: {self.player_health}")
        self.enemy_health_label.config(text=f"Vida do {self.enemy['nome']}: {self.enemy['vida']}")