import qrcode


def gerar_qrcode_png_transparente(link, caminho_arquivo):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="transparent").convert("RGBA")

    img.save(caminho_arquivo)
    print(f"QR Code com fundo transparente salvo em: {caminho_arquivo}")


link = input("Digite o link: ")
caminho = input("Digite o caminho do arquivo (deve terminar com .png): ")
gerar_qrcode_png_transparente(link, caminho)
