from tkinter import Tk, Label, Entry, Button, StringVar, filedialog, OptionMenu, messagebox, Checkbutton, IntVar, DISABLED, NORMAL
import os
import webbrowser



def generate_qrcode(link, doc_path, save_format, include_logo, logo_path):
    import qrcode
    from qrcode.image.svg import SvgImage
    from PIL import Image, ImageDraw

    if save_format == 'PNG':
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="transparent").convert("RGBA")

        if include_logo and logo_path:
            try:
                logo = Image.open(logo_path).convert("RGBA")
                base_width = img.size[0] // 4
                w_percent = (base_width / float(logo.size[0]))
                hsize = int((float(logo.size[1]) * float(w_percent)))
                logo = logo.resize((base_width, hsize), Image.LANCZOS)

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

        img.save(doc_path)

    elif save_format == 'SVG':
        qr = qrcode.make(link, image_factory=SvgImage)
        qr.save(doc_path)

    messagebox.showinfo("Sucesso", f"QR Code salvo em:\n{doc_path}")


def select_folder():
    file = filedialog.askdirectory()
    if file:
        path_var.set(file)


def select_logo_file():
    arc = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
    if arc:
        logo_path_var.set(arc)

def toggle_logo():
    if include_logo_flag.get():
        logo_btn.config(state=NORMAL)
    else:
        logo_btn.config(state=DISABLED)
        logo_path_var.set("")


def generate():
    link = link_var.get()
    file = path_var.get()
    name = filename_var.get()
    save_format = save_format_var.get()
    include_logo = include_logo_flag.get()
    logo_path = logo_path_var.get()

    if not link or not file or not name:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    if include_logo and not logo_path and save_format == "PNG":
        messagebox.showerror("Erro", "Selecione o arquivo da logo.")
        return

    doc_path = os.path.join(file, f"{name}.{save_format.lower()}")
    generate_qrcode(link, doc_path, save_format, include_logo, logo_path)


# GUI
window = Tk()
window.title("Gerador de QR Code")
window.geometry("420x300")

link_var = StringVar()
path_var = StringVar()
filename_var = StringVar()
save_format_var = StringVar(value="PNG")
logo_path_var = StringVar()
include_logo_flag = IntVar()

Label(window, text="Link:").pack()
Entry(window, textvariable=link_var, width=50).pack()

Label(window, text="Formato:").pack()
OptionMenu(window, save_format_var, "PNG", "SVG").pack()

Label(window, text="Nome do arquivo (sem extensão):").pack()
Entry(window, textvariable=filename_var, width=50).pack()

Button(window, text="Escolher local de destino", command=select_folder).pack()
Entry(window, textvariable=path_var, width=50).pack()

Checkbutton(window, text="Incluir logo no QR (PNG, JPEG ou JPG)", variable=include_logo_flag, command=toggle_logo).pack()

logo_btn = Button(window, text="Selecionar logo", command=select_logo_file, state=DISABLED)
logo_btn.pack()

Entry(window, textvariable=logo_path_var, width=50, state="readonly").pack()

Button(window, text="Gerar QR Code", command=generate).pack(pady=10)

sign_label = Label(window, text="Desenvolvido por Rafael Bandini", font=("Arial", 8, "italic"), fg="blue", cursor="hand2")

sign_label.place(relx=1.0, rely=1.0, anchor="se")
sign_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.linkedin.com/in/rafael-bandini/"))

window.mainloop()
