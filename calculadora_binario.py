import tkinter as tk
from tkinter import messagebox

def dec_para_bin():
    dec_num = entrada.get()
    try:
        # Converte o número decimal para binário e remove o prefixo '0b'
        binario = bin(int(dec_num))[2:]
        resultado_var.set(f"Binário: {binario}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada decimal inválida.")

def bin_para_dec():
    bin_num = entrada.get()
    try:
        # Converte o número binário para decimal
        decimal = int(bin_num, 2)
        resultado_var.set(f"Decimal: {decimal}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada binária inválida.")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Decimal ↔ Binário")

# Entrada
entrada = tk.Entry(janela, width=30)
entrada.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Botões
botao_decimal = tk.Button(janela, text="Decimal → Binário", command=dec_para_bin)
botao_decimal.grid(row=1, column=0, padx=5, pady=5)

botao_binario = tk.Button(janela, text="Binário → Decimal", command=bin_para_dec)
botao_binario.grid(row=1, column=1, padx=5, pady=5)

# Resultado
resultado_var = tk.StringVar()
resultado_label = tk.Label(janela, textvariable=resultado_var, font=("Arial", 12))
resultado_label.grid(row=2, column=0, columnspan=2, pady=10)

janela.mainloop()
