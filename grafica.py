import math
import tkinter as tk
from tkinter import messagebox, ttk

R = 8.314
entries = {}  # Dicionário para armazenar referências das entradas


# Funções para cálculos
def val_temp():
    try:
        n = float(entries['Temp'][0].get())
        Ti = float(entries['Temp'][1].get())
        Tf = float(entries['Temp'][2].get())
        tipo_processo = processo_var.get()
        tipo_gas = gas_var.get()

        gas_values = {'V': {'M': 3.0 / 2.0, 'D': 5.0 / 2.0, 'P': 3},
                      'P': {'M': 5.0 / 2.0, 'D': 7.0 / 2.0, 'P': 4}}

        if tipo_gas in gas_values[tipo_processo]:
            gas = gas_values[tipo_processo][tipo_gas]
        else:
            messagebox.showerror("Erro", "Tipo de gás inválido!")
            return

        deltaS = n * gas * R * math.log(Tf / Ti)
        messagebox.showinfo("Resultado", f"ΔS (temperatura): {deltaS:.2f} J/K")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos.")


def val_vol():
    try:
        n = float(entries['Vol'][0].get())
        Vi = float(entries['Vol'][1].get())
        Vf = float(entries['Vol'][2].get())
        deltaS = n * R * math.log(Vf / Vi)
        messagebox.showinfo("Resultado", f"ΔS (volume): {deltaS:.2f} J/K")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos.")


def val_press():
    try:
        n = float(entries['Press'][0].get())
        Pi = float(entries['Press'][1].get())
        Pf = float(entries['Press'][2].get())
        deltaS = -n * R * math.log(Pf / Pi)
        messagebox.showinfo("Resultado", f"ΔS (pressão): {deltaS:.2f} J/K")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos.")


def calc_n():
    try:
        P = float(entries['Mols'][0].get()) * 101325  # Conversão de atm para Pa
        V = float(entries['Mols'][1].get())
        T = float(entries['Mols'][2].get())
        if T <= 0:
            raise ValueError("A temperatura deve ser maior que zero Kelvin.")
        n = (P * V) / (R * T)
        messagebox.showinfo("Resultado", f"Número de mols: {n:.2f} mol")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


# Função principal da interface
def criar_interface():
    global processo_var, gas_var

    root = tk.Tk()
    root.title("Calculadora de Entropia")

    notebook = ttk.Notebook(root)

    # Abas para cada cálculo
    abas = {'Temp': ('Número de mols (n)', 'Temperatura inicial (Ti em K)', 'Temperatura final (Tf em K)'),
            'Vol': ('Número de mols (n)', 'Volume inicial (Vi em m³)', 'Volume final (Vf em m³)'),
            'Press': ('Número de mols (n)', 'Pressão inicial (Pi em Pa)', 'Pressão final (Pf em Pa)'),
            'Mols': ('Pressão (atm)', 'Volume (m³)', 'Temperatura (K)')}

    for aba, labels in abas.items():
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=aba)
        entries[aba] = []

        for i, label in enumerate(labels):
            tk.Label(frame, text=label).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(frame)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[aba].append(entry)

        if aba == 'Temp':
            # Seletor de tipo de processo
            tk.Label(frame, text="Tipo de processo:").grid(row=3, column=0)
            processo_var = tk.StringVar(value="V")
            tk.OptionMenu(frame, processo_var, "V", "P").grid(row=3, column=1)

            # Seletor de tipo de gás
            tk.Label(frame, text="Tipo de gás:").grid(row=4, column=0)
            gas_var = tk.StringVar(value="M")
            tk.OptionMenu(frame, gas_var, "M", "D", "P").grid(row=4, column=1)

            tk.Button(frame, text="Calcular", command=val_temp).grid(row=5, columnspan=2, pady=10)

        elif aba == 'Vol':
            tk.Button(frame, text="Calcular", command=val_vol).grid(row=3, columnspan=2, pady=10)

        elif aba == 'Press':
            tk.Button(frame, text="Calcular", command=val_press).grid(row=3, columnspan=2, pady=10)

        elif aba == 'Mols':
            tk.Button(frame, text="Calcular", command=calc_n).grid(row=3, columnspan=2, pady=10)

    notebook.pack(expand=True, fill='both')
    root.mainloop()


# Executa a interface
if __name__ == "__main__":
    criar_interface()
