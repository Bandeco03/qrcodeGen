from tkinter import Tk, Label, Entry, Button, StringVar, filedialog, OptionMenu, messagebox, Checkbutton, IntVar, DISABLED, NORMAL
import os
import webbrowser



def gerar_qrcode(link, caminho_arquivo, formato, incluir_logo, caminho_logo):
    import qrcode
    from qrcode.image.svg import SvgImage
    from PIL import Image, ImageDraw

    if formato == 'PNG':
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="transparent").convert("RGBA")

        if incluir_logo and caminho_logo:
            try:
                logo = Image.open(caminho_logo).convert("RGBA")
                basewidth = img.size[0] // 4
                wpercent = (basewidth / float(logo.size[0]))
                hsize = int((float(logo.size[1]) * float(wpercent)))
                logo = logo.resize((basewidth, hsize), Image.LANCZOS)

                pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)

                erase_width = int(logo.size[0] * 0.95)
                erase_height = int(logo.size[1] * 0.95)
                erase_x = pos[0] + (logo.size[0] - erase_width) // 2
                erase_y = pos[1] + (logo.size[0] - erase_height) // 2

                draw = ImageDraw.Draw(img)
                draw.rectangle(
                    [erase_x, erase_y, erase_x + erase_width, erase_y + erase_height],
                    fill=(255, 255, 255, 0)
                )

                img.paste(logo, pos, mask=logo)

            except Exception as e:
                messagebox.showwarning("Erro na logo", f"Erro ao adicionar logo: {e}")

        img.save(caminho_arquivo)

    elif formato == 'SVG':
        qr = qrcode.make(link, image_factory=SvgImage)
        qr.save(caminho_arquivo)

    messagebox.showinfo("Sucesso", f"QR Code salvo em:\n{caminho_arquivo}")


def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        caminho_var.set(pasta)


def selecionar_logo():
    arquivo = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
    if arquivo:
        logo_var.set(arquivo)

def toggle_logo():
    if incluir_logo_var.get():
        botao_logo.config(state=NORMAL)
    else:
        botao_logo.config(state=DISABLED)
        logo_var.set("")


def gerar():
    link = link_var.get()
    pasta = caminho_var.get()
    nome = nome_arquivo_var.get()
    formato = formato_var.get()
    incluir_logo = incluir_logo_var.get()
    caminho_logo = logo_var.get()

    if not link or not pasta or not nome:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    if incluir_logo and not caminho_logo and formato == "PNG":
        messagebox.showerror("Erro", "Selecione o arquivo da logo.")
        return

    caminho_arquivo = os.path.join(pasta, f"{nome}.{formato.lower()}")
    gerar_qrcode(link, caminho_arquivo, formato, incluir_logo, caminho_logo)


# GUI
app = Tk()
app.title("Gerador de QR Code")
app.geometry("420x300")

link_var = StringVar()
caminho_var = StringVar()
nome_arquivo_var = StringVar()
formato_var = StringVar(value="PNG")
logo_var = StringVar()
incluir_logo_var = IntVar()

Label(app, text="Link:").pack()
Entry(app, textvariable=link_var, width=50).pack()

Label(app, text="Formato:").pack()
OptionMenu(app, formato_var, "PNG", "SVG").pack()

Label(app, text="Nome do arquivo (sem extensão):").pack()
Entry(app, textvariable=nome_arquivo_var, width=50).pack()

Button(app, text="Escolher pasta de destino", command=selecionar_pasta).pack()
Entry(app, textvariable=caminho_var, width=50).pack()

Checkbutton(app, text="Incluir logo no QR (PNG, JPEG ou JPG)", variable=incluir_logo_var, command=toggle_logo).pack()

botao_logo = Button(app, text="Selecionar logo", command=selecionar_logo, state=DISABLED)
botao_logo.pack()

Entry(app, textvariable=logo_var, width=50, state="readonly").pack()

Button(app, text="Gerar QR Code", command=gerar).pack(pady=10)

sign_label = Label(app, text="Desenvolvido por Rafael Bandini", font=("Arial", 8, "italic"), fg="blue", cursor="hand2")

sign_label.place(relx=1.0, rely=1.0, anchor="se")
sign_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.linkedin.com/in/rafael-bandini/"))

app.mainloop()
