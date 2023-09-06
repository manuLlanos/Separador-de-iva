import tkinter as tk

#falta agregar botones para copiar

def get_neto(iva, tasa):
    return iva/tasa + iva

entry_data = {
    "iva21": {"input_text": "Iva 21:", "tax":0.21, "output_text": "Gravado 21%:"},
    "iva105": {"input_text": "Iva 10,5:", "tax":0.105, "output_text": "Gravado 10,5%:"}
}

def update_iva(event, tipo):
    tax = entry_data[tipo]["tax"]
    input = ent_iva[tipo].get()

    try:
        iva = float(input)
        output_neto[tipo].config(text=f"{get_neto(iva, tax):.2f}")
        update_total(None)
    except ValueError:
        output_neto[tipo].config(text="Entrada no valida")


def update_total(event):
    grav21 = output_neto["iva21"]["text"]
    grav105 = output_neto["iva105"]["text"]

    try:
        grav21 = float(grav21)
        grav105 = float(grav105)
        output_total.config(text=f"{(grav21+grav105):.2f}")
    except ValueError:
        output_total.config(text="Entrada no valida")

def copiar(texto):
    print(texto)
    window.clipboard_clear()
    window.clipboard_append(texto)
    window.update()

window = tk.Tk()
window.title("Separador de IVA")
# todo: hacer que esto sea toggeable
window.attributes("-topmost", True)

lbl_iva = {}
lbl_out = {}
ent_iva = {}
output_neto = {}
btn_copy = {}

for idx, tipo_iva in enumerate(entry_data):
    lbl_iva[tipo_iva] = tk.Label(window, text=entry_data[tipo_iva]["input_text"])
    ent_iva[tipo_iva] = tk.Entry(window, width=12)
    ent_iva[tipo_iva].bind("<KeyRelease>", lambda event, tipo=tipo_iva: update_iva(event, tipo), add="+")


    lbl_out[tipo_iva]= tk.Label(window, text=entry_data[tipo_iva]["output_text"])
    output_neto[tipo_iva] = tk.Label(window, text="", width=12)

    lbl_iva[tipo_iva].grid(row=idx, column=0, padx=5, pady=5)
    ent_iva[tipo_iva].grid(row=idx, column=1, padx=5, pady=5)
    lbl_out[tipo_iva].grid(row=idx, column=2, padx=5, pady=5)
    output_neto[tipo_iva].grid(row=idx, column=3, ipadx=20, pady=5)

    btn_copy[tipo_iva] = tk.Button(
        window, 
        text="Copiar", 
        command = lambda tipo=tipo_iva: copiar(output_neto[tipo].cget("text")))
    btn_copy[tipo_iva].grid(row=idx, column=4, padx=10)

lbl_total = tk.Label(window, text="Total:")
output_total = tk.Label(window, text="")
btn_copy_total = tk.Button(window, text="Copiar", command = lambda: copiar(output_total.cget("text")))

lbl_total.grid(row=2, column=2, padx=5, pady=5)
output_total.grid(row=2, column=3, padx=5, pady=5)
btn_copy_total.grid(row=2, column=4, padx=10)


window.mainloop()