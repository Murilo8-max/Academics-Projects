from logging import root
import tkinter as tk
from tkinter import messagebox


class SaborRapidoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sabor Rápido - Protótipo")
        self.root.geometry("400x500")

        self.itens_menu = {"Hambúrguer": 10.00,
                           "Batata Frita": 5.00, "Refrigerante": 3.00}
        self.pedido = []

        tk.Label(self.root, text="Selecione os itens do pedido:",
                 font=("Arial", 12)).pack(pady=10)

        self.listbox = tk.Listbox(
            self.root, selectmode=tk.MULTIPLE, font=("Arial", 10))
        self.listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=False)
        self.atualizar_lista_menu()

        tk.Button(self.root, text="Adicionar ao Pedido",
                  command=self.adicionar_pedido).pack(pady=5)
        tk.Button(self.root, text="Visualizar Pedido",
                  command=self.visualizar_pedido).pack(pady=5)
        tk.Button(self.root, text="Finalizar Pedido",
                  command=self.finalizar_pedido).pack(pady=5)

        tk.Label(self.root, text="Adicionar Novo Item ao Menu:",
                 font=("Arial", 12)).pack(pady=10)
        self.entry_item = tk.Entry(self.root, font=("Arial", 10))
        self.entry_item.pack(padx=10, pady=2, fill=tk.X)
        self.entry_preco = tk.Entry(self.root, font=("Arial", 10))
        self.entry_preco.pack(padx=10, pady=2, fill=tk.X)
        tk.Button(self.root, text="Adicionar Item",
                  command=self.adicionar_item_menu).pack(pady=5)

    def atualizar_lista_menu(self):
        self.listbox.delete(0, tk.END)
        for item in self.itens_menu.keys():
            self.listbox.insert(tk.END, item)

    def adicionar_pedido(self):
        selecionados = self.listbox.curselection()
        if not selecionados:
            messagebox.showinfo("Pedido", "Nenhum item selecionado.")
            return
        for index in selecionados:
            item = self.listbox.get(index)
            self.pedido.append(item)
        messagebox.showinfo("Pedido", "Itens adicionados com sucesso!")

    def visualizar_pedido(self):
        if not self.pedido:
            messagebox.showinfo("Pedido", "Nenhum item no pedido.")
            return
        pedido_texto = "\n".join(self.pedido)
        total = sum(self.itens_menu.get(item, 0) for item in self.pedido)
        messagebox.showinfo(
            "Pedido Atual", f"Itens no pedido:\n{pedido_texto}\n\nTotal parcial: R$ {total:.2f}")

    def finalizar_pedido(self):
        if not self.pedido:
            messagebox.showinfo(
                "Pedido", "Adicione itens antes de finalizar o pedido.")
            return
        total = sum(self.itens_menu.get(item, 0) for item in self.pedido)
        messagebox.showinfo(
            "Total", f"Total do pedido: R$ {total:.2f}\nPedido finalizado!")
        self.pedido.clear()

    def adicionar_item_menu(self):
        item = self.entry_item.get().strip()
        preco = self.entry_preco.get().strip()
        if not item or not preco:
            messagebox.showerror(
                "Erro", "Preencha ambos os campos corretamente.")
            return
        try:
            preco_val = float(preco)
            if preco_val < 0:
                raise ValueError("Preço negativo")
            self.itens_menu[item] = preco_val
            self.atualizar_lista_menu()
            self.entry_item.delete(0, tk.END)
            self.entry_preco.delete(0, tk.END)
            messagebox.showinfo(
                "Sucesso", "Item adicionado ao menu com sucesso!")
        except ValueError:
            messagebox.showerror(
                "Erro", "Preço inválido. Digite um valor numérico.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SaborRapidoApp(root)
    root.mainloop()
