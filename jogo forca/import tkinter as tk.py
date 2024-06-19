import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# atualizar a imagem de acordo com a quantidade de erros
def update_image():
    global errors
    if errors < len(images):
        img_tk = images[errors]
        image_label.config(image=img_tk)
        image_label.image = img_tk

# processar o palpite de letra
def guess_letter():
    global errors
    letter = entry.get().lower() # transforma a letra em minuscula
    entry.delete(0, tk.END)
    
    if letter in word:
         # se a letra esta na palavra, atualiza a exibição da palavra com todas as ocorrências da letra
        for idx, char in enumerate(word):
            if char == letter:
                word_display[idx] = letter
        word_label.config(text=" ".join(word_display))
    else:
        # se a letra nao tiver na palavra, coloca o erro na imagem
        errors += 1
        update_image()
# Verifica se o jogador perdeu
    if errors == len(images):
        messagebox.showinfo("Forca", "Você perdeu!")
        # Verifica se o jogador ganhou
    elif "_" not in word_display:
        messagebox.showinfo("Forca", "Você ganhou!")


errors = 0
word = "cachorro"
word_display = ["_" for _ in word]


root = tk.Tk()
root.title("Jogo da Forca")

# caminho das imagens de inicio e erro
image_paths = [
    r"C:\Users\paulo\OneDrive\Desktop\jogo forca\erros\inicio.png",
    r"C:\Users\paulo\OneDrive\Desktop\jogo forca\erros\erro1.png",
    r"C:\Users\paulo\OneDrive\Desktop\jogo forca\erros\erro2.png",
    r"C:\Users\paulo\OneDrive\Desktop\jogo forca\erros\erro3.png",
    r"C:\Users\paulo\OneDrive\Desktop\jogo forca\erros\erro4.png",
    r"C:\Users\paulo\OneDrive\Desktop\jogo forca\erros\erro5.png"
]



try:
    images = [ImageTk.PhotoImage(Image.open(path)) for path in image_paths]
except IOError as e:
    messagebox.showerror("Erro", f"Erro ao carregar imagem: {e}")
# Exibe mensagem de erro se houver problema ao carregar as imagens
images = [ImageTk.PhotoImage(Image.open(path)) for path in image_paths]


img_tk = images[0]
image_label = tk.Label(root, image=img_tk)
image_label.pack()


word_label = tk.Label(root, text=" ".join(word_display), font=("Helvetica", 24))
word_label.pack()

# Cria uma entrada para o jogador inserir letras
entry = tk.Entry(root)
entry.pack()

# Botão para o jogador enviar uma letra
guess_button = tk.Button(root, text="Adivinhar", command=guess_letter)
guess_button.pack()


root.mainloop()
