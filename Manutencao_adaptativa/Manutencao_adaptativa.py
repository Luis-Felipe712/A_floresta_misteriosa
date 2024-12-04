import tkinter as tk
from tkinter import messagebox


class JogoAventura:
    def __init__(self, root):
        self.root = root
        self.root.title("A Floresta Misteriosa")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")  # Cor de fundo.

        self.localizacao = "floresta"
        self.inventario = []

        # Frame Superior (Título)
        self.frame_titulo = tk.Frame(root, bg="#34495e")
        self.frame_titulo.pack(fill=tk.X, pady=5)
        self.titulo = tk.Label(self.frame_titulo, text="A Floresta Misteriosa", font=("Arial", 24, "bold"), fg="#ecf0f1", bg="#34495e")
        self.titulo.pack(pady=10)

        # Frame Central (Descrição e Inventário)
        self.frame_central = tk.Frame(root, bg="#2c3e50")
        self.frame_central.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.descricao = tk.Label(self.frame_central, text="Bem-vindo à Aventura em Texto!", font=("Arial", 16), wraplength=700, bg="#2c3e50", fg="#ecf0f1", justify=tk.LEFT)
        self.descricao.pack(pady=20)

        self.inventario_label = tk.Label(self.frame_central, text="Inventário: Nenhum item", font=("Arial", 14, "italic"), bg="#2c3e50", fg="#ecf0f1", wraplength=700)
        self.inventario_label.pack(pady=10)

        # Frame Inferior (Botões)
        self.frame_botoes = tk.Frame(root, bg="#2c3e50")
        self.frame_botoes.pack(pady=20)

        self.botao_norte = tk.Button(self.frame_botoes, text="Norte", font=("Arial", 14), command=lambda: self.mover("norte"), bg="#16a085", fg="white", width=10, height=2)
        self.botao_sul = tk.Button(self.frame_botoes, text="Sul", font=("Arial", 14), command=lambda: self.mover("sul"), bg="#16a085", fg="white", width=10, height=2)
        self.botao_leste = tk.Button(self.frame_botoes, text="Leste", font=("Arial", 14), command=lambda: self.mover("leste"), bg="#16a085", fg="white", width=10, height=2)
        self.botao_oeste = tk.Button(self.frame_botoes, text="Oeste", font=("Arial", 14), command=lambda: self.mover("oeste"), bg="#16a085", fg="white", width=10, height=2)
        self.botao_sair = tk.Button(self.frame_botoes, text="Sair", font=("Arial", 14), command=self.sair, bg="#e74c3c", fg="white", width=10, height=2)

        # Posicionamento dos botões
        self.botao_norte.grid(row=0, column=1, padx=10, pady=10)
        self.botao_sul.grid(row=2, column=1, padx=10, pady=10)
        self.botao_leste.grid(row=1, column=2, padx=10, pady=10)
        self.botao_oeste.grid(row=1, column=0, padx=10, pady=10)
        self.botao_sair.grid(row=3, column=1, pady=10)

        self.atualizar_descricao("Você está em uma floresta escura. Uma trilha se estende ao norte e outra ao leste.")

    def atualizar_descricao(self, texto):
        """Atualiza a descrição do jogo na interface."""
        self.descricao.config(text=texto)
        self.inventario_label.config(text=f"Inventário: {', '.join(self.inventario) if self.inventario else 'Nenhum item'}")

    def mover(self, direcao):
        """Processa o movimento e atualiza a localização."""
        if direcao == "norte":
            if self.localizacao == "floresta":
                self.localizacao = "cabana"
                self.atualizar_descricao("Você encontra uma cabana abandonada.")
                if "chave" not in self.inventario:
                    self.inventario.append("chave")
                    self.atualizar_descricao("Dentro da cabana, você encontra uma chave enferrujada.")
            else:
                self.atualizar_descricao("Não há caminho para o norte aqui.")
        elif direcao == "leste":
            if self.localizacao == "floresta":
                self.localizacao = "rio"
                self.atualizar_descricao("Você chega a um rio de águas turbulentas.")
                if "chave" in self.inventario:
                    self.atualizar_descricao("Você usa a chave para destravar a ponte e encontra um tesouro escondido!")
                    self.localizacao = "tesouro"
            else:
                self.atualizar_descricao("Não há caminho para o leste aqui.")
        elif direcao == "sul":
            if self.localizacao == "cabana":
                self.localizacao = "floresta"
                self.atualizar_descricao("Você retorna à floresta.")
            else:
                self.atualizar_descricao("Não há caminho para o sul aqui.")
        elif direcao == "oeste":
            if self.localizacao == "rio":
                self.localizacao = "floresta"
                self.atualizar_descricao("Você retorna à floresta.")
            else:
                self.atualizar_descricao("Não há caminho para o oeste aqui.")
        else:
            self.atualizar_descricao("Comando inválido.")

    def sair(self):
        """Exibe mensagem de saída e fecha o jogo."""
        if messagebox.askyesno("Sair", "Você tem certeza que deseja sair do jogo?"):
            self.root.destroy()


# Inicialização do jogo
if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoAventura(root)
    root.mainloop()
