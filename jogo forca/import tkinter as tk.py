import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Função para atualizar a imagem com o nível de água no copo
def update_image():
    global errors
    if errors < len(images):
        img_tk = images[errors]
        image_label.config(image=img_tk)
        image_label.image = img_tk

# Função para adivinhar a letra
def guess_letter():
    global errors
    letter = entry.get().lower()
    entry.delete(0, tk.END)
    
    if letter in word:
        for idx, char in enumerate(word):
            if char == letter:
                word_display[idx] = letter
        word_label.config(text=" ".join(word_display))
    else:
        errors += 1
        update_image()

    if errors == len(images):
        messagebox.showinfo("Forca", "Você perdeu!")
    elif "_" not in word_display:
        messagebox.showinfo("Forca", "Você ganhou!")

# Configuração inicial
errors = 0
word = "cachorro"
word_display = ["_" for _ in word]

# Configuração da janela
root = tk.Tk()
root.title("Jogo da Forca")

# Caminhos completos das imagens
image_paths = [
    r"C:\Users\paulo\OneDrive\Desktop\jogo forca\erros\inicio.png",
    r"C:\Users\paulo\OneDrive\Desktop\jogo forca\erros\erro1.png",
    r"C:\Users\paulo\OneDrive\Desktop\jogo forca\erros\erro2.png",
    r"C:\Users\paulo\OneDrive\Desktop\jogo forca\erros\erro3.png",
    r"C:\Users\paulo\OneDrive\Desktop\jogo forca\erros\erro4.png",
    r"C:\Users\paulo\OneDrive\Desktop\jogo forca\erros\erro5.png"
]


# Carregar as imagens
try:
    images = [ImageTk.PhotoImage(Image.open(path)) for path in image_paths]
except IOError as e:
    messagebox.showerror("Erro", f"Erro ao carregar imagem: {e}")

images = [ImageTk.PhotoImage(Image.open(path)) for path in image_paths]

# Configuração da imagem inicial
img_tk = images[0]
image_label = tk.Label(root, image=img_tk)
image_label.pack()

# Configuração da palavra oculta
word_label = tk.Label(root, text=" ".join(word_display), font=("Helvetica", 24))
word_label.pack()

# Entrada para adivinhar a letra
entry = tk.Entry(root)
entry.pack()

# Botão para enviar a letra
guess_button = tk.Button(root, text="Adivinhar", command=guess_letter)
guess_button.pack()

# Iniciar o loop principal do tkinter
root.mainloop()
