# QR Code Generator GUI

Transforma qualquer link em QR Code (PNG transparente ou SVG) com uma interface gráfica simples em Tkinter — sem dor de cabeça, só clicar e gerar.

---

## 🚀 Funcionalidades

- Insere um link qualquer.  
- Escolhe formato de saída: **PNG** (fundo transparente) ou **SVG**.  
- Define nome do arquivo (sem extensão) e pasta de destino.  
- Gera o QR Code e avisa quando está salvo.  

---

## 🛠️ Tecnologias

- Python 3.13  
- [qrcode](https://pypi.org/project/qrcode/)  
- [Pillow (PIL)](https://pypi.org/project/Pillow/)  
- Tkinter (GUI nativa do Python)  

---

## 📥 Requisitos

Instale no seu ambiente virtual:

```bash
pip install qrcode[pil]
pip install svgwrite
````

> Se quiser gerar o `.exe`, instale também o PyInstaller:
>
> ```bash
> pip install pyinstaller
> ```

---

## ⚙️ Como usar (código-fonte)

1. Clone este repositório.
2. Ative sua venv:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Instale dependências (veja acima).
4. Execute o script:

   ```bash
   python qrcodeGenerator.py
   ```
5. Preencha na janela:

   * **Link**
   * **Formato** (PNG ou SVG)
   * **Nome do arquivo**
   * **Pasta de destino**
6. Clique em **Gerar QR Code**.

---

## 📦 Executável (Windows)

Já inclui um `.exe` pronto para usar:

1. Baixe `qrcodeGenerator.exe` na pasta `dist/`.
2. Clique duas vezes e use a GUI normalmente.

---

## 🧰 Como gerar seu próprio .exe

```bash
pyinstaller --onefile --noconsole --icon=icone.ico \
  --hidden-import=qrcode \
  --hidden-import=qrcode.image.svg \
  --hidden-import=PIL \
  qrcodeGenerator.py
```

* `--icon=icone.ico` → define o ícone do EXE (coloque o arquivo `.ico` na mesma pasta).
* `--noconsole` → esconde o terminal ao abrir a GUI.
