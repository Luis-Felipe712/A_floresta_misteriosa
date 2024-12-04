import tkinter as tk
from tkinter import messagebox
from areas import get_area_description, get_area_items, get_area_enemy, is_final_area
from combate import Combate
from quebra_cabeca import QuebraCabeca


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("A Floresta Misteriosa")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")

        self.current_area = "floresta"
        self.inventory = []
        self.health = 100
        self.visited_areas = set()  # Áreas já visitadas
        self.completed_puzzles = set()  # Enigmas resolvidos
        self.defeated_enemies = set()  # Inimigos derrotados

        # Frame Superior (Título)
        self.frame_titulo = tk.Frame(self.root, bg="#34495e")
        self.frame_titulo.pack(fill=tk.X, pady=5)
        self.titulo = tk.Label(
            self.frame_titulo,
            text="A Floresta Misteriosa",
            font=("Arial", 24, "bold"),
            fg="#ecf0f1",
            bg="#34495e",
        )
        self.titulo.pack(pady=10)

        # Frame Central (Descrição e Inventário)
        self.frame_central = tk.Frame(self.root, bg="#2c3e50")
        self.frame_central.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.descricao = tk.Label(
            self.frame_central,
            text="",
            font=("Arial", 16),
            wraplength=700,
            bg="#2c3e50",
            fg="#ecf0f1",
            justify=tk.LEFT,
        )
        self.descricao.pack(pady=20)

        self.inventario_label = tk.Label(
            self.frame_central,
            text="Inventário: Nenhum item",
            font=("Arial", 14, "italic"),
            bg="#2c3e50",
            fg="#ecf0f1",
            wraplength=700,
        )
        self.inventario_label.pack(pady=10)

        # Frame Inferior (Botões)
        self.frame_botoes = tk.Frame(self.root, bg="#2c3e50")
        self.frame_botoes.pack(pady=20)

        self.botao_norte = tk.Button(
            self.frame_botoes,
            text="Norte",
            font=("Arial", 14),
            command=lambda: self.move("norte"),
            bg="#16a085",
            fg="white",
            width=10,
            height=2,
        )
        self.botao_sul = tk.Button(
            self.frame_botoes,
            text="Sul",
            font=("Arial", 14),
            command=lambda: self.move("sul"),
            bg="#16a085",
            fg="white",
            width=10,
            height=2,
        )
        self.botao_leste = tk.Button(
            self.frame_botoes,
            text="Leste",
            font=("Arial", 14),
            command=lambda: self.move("leste"),
            bg="#16a085",
            fg="white",
            width=10,
            height=2,
        )
        self.botao_oeste = tk.Button(
            self.frame_botoes,
            text="Oeste",
            font=("Arial", 14),
            command=lambda: self.move("oeste"),
            bg="#16a085",
            fg="white",
            width=10,
            height=2,
        )
        self.botao_sair = tk.Button(
            self.frame_botoes,
            text="Sair",
            font=("Arial", 14),
            command=self.exit_game,
            bg="#e74c3c",
            fg="white",
            width=10,
            height=2,
        )

        # Posicionamento dos botões
        self.botao_norte.grid(row=0, column=1, padx=10, pady=10)
        self.botao_sul.grid(row=2, column=1, padx=10, pady=10)
        self.botao_leste.grid(row=1, column=2, padx=10, pady=10)
        self.botao_oeste.grid(row=1, column=0, padx=10, pady=10)
        self.botao_sair.grid(row=3, column=1, pady=10)

        self.update_description(
            "Você está em uma floresta escura. Escolha uma direção para explorar."
        )

    def update_description(self, text):
        self.descricao.config(text=text)
        self.inventario_label.config(
            text=f"Inventário: {', '.join(self.inventory) if self.inventory else 'Nenhum item'}"
        )

    def move(self, direction):
        area_map = {
            "norte": "cabana",
            "sul": "floresta",
            "leste": "rio",
            "oeste": "bosque",
        }

        new_area = area_map.get(direction)
        if new_area and new_area != self.current_area:
            self.current_area = new_area
            self.handle_area(new_area)
        else:
            self.update_description("Você não pode ir nessa direção.")

    def handle_area(self, area):
        # Exibir descrição da área
        self.update_description(get_area_description(area))

        # Adicionar itens ao inventário (sem repetição)
        for item in get_area_items(area):
            if item not in self.inventory:
                self.inventory.append(item)

        # Resolver combate (uma vez por área)
        enemy = get_area_enemy(area)
        if enemy and area not in self.defeated_enemies:
            combate = Combate(self.root, enemy, self.health)
            self.health = combate.start_combat()
            if self.health <= 0:
                self.update_description("Você foi derrotado! Fim de jogo!")
                return
            self.defeated_enemies.add(area)

        # Resolver enigma (uma vez por área)
        if area == "cabana" and area not in self.completed_puzzles:
            quebra_cabeca = QuebraCabeca(self.root)
            if quebra_cabeca.solve():
                self.completed_puzzles.add(area)
            else:
                self.update_description("Você falhou no desafio!")
                return

        # Verificar se é a área final
        if is_final_area(area, self.inventory):
            self.update_description("Parabéns! Você concluiu o jogo com sucesso!")
            return

    def exit_game(self):
        if messagebox.askyesno("Sair", "Você tem certeza que deseja sair do jogo?"):
            self.root.destroy()

    def start(self):
        self.root.mainloop()
