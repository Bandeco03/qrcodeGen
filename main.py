import qrcode
from qrcode.image.svg import SvgImage
from tkinter import Tk, Label, Entry, Button, StringVar, filedialog, OptionMenu, messagebox
import os


def gerar_qrcode(link, caminho_arquivo, formato):
    if formato == 'PNG':
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="transparent").convert("RGBA")
        img.save(caminho_arquivo)

    elif formato == 'SVG':
        qr = qrcode.make(link, image_factory=SvgImage)
        qr.save(caminho_arquivo)

    messagebox.showinfo("Sucesso", f"QR Code salvo em:\n{caminho_arquivo}")


def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        caminho_var.set(pasta)


def gerar():
    link = link_var.get()
    pasta = caminho_var.get()
    nome = nome_arquivo_var.get()
    formato = formato_var.get()

    if not link or not pasta or not nome:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    caminho_arquivo = os.path.join(pasta, f"{nome}.{formato.lower()}")
    gerar_qrcode(link, caminho_arquivo, formato)


# GUI
app = Tk()
app.title("Gerador de QR Code")
app.geometry("400x230")

link_var = StringVar()
caminho_var = StringVar()
nome_arquivo_var = StringVar()
formato_var = StringVar(value="PNG")

Label(app, text="Link:").pack()
Entry(app, textvariable=link_var, width=50).pack()

Label(app, text="Formato:").pack()
OptionMenu(app, formato_var, "PNG", "SVG").pack()

Label(app, text="Nome do arquivo (sem extensão):").pack()
Entry(app, textvariable=nome_arquivo_var, width=50).pack()

Button(app, text="Escolher pasta de destino", command=selecionar_pasta).pack()
Entry(app, textvariable=caminho_var, width=50).pack()

Button(app, text="Gerar QR Code", command=gerar).pack(pady=10)

app.mainloop()
