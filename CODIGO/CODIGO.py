import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import io
from rembg import remove
import os

def select_image():
    global image_path
    image_path = filedialog.askopenfilename(title="SELECIONE UMA IMAGEM", filetypes=[("Imagens", "*.*")])
    if image_path:
        image_label.config(text="CAMINHO: " + image_path)
        image_label.pack() 
        save_button.config(state=tk.NORMAL)

def remove_background_and_save():
    if image_path:
        with open(image_path, "rb") as f:
            image_data = f.read()
        output = remove(image_data)
        img = Image.open(io.BytesIO(output))
        output_image_path = os.path.splitext(image_path)[0] + "_ICONE.ico"
        img.save(output_image_path, format="ICO")
        
        messagebox.showinfo("SUCESSO!", "O fundo foi removido e a imagem foi salva com sucesso!")

root = tk.Tk()
root.title("IMAGEM PARA ICO")
root.geometry("400x200")

image_path = ""

select_button = tk.Button(root, text="SELECIONAR", command=select_image)
select_button.pack(pady=10)

image_label = tk.Label(root, text="CAMINHO: ")

save_button = tk.Button(root, text="SALVAR", command=remove_background_and_save, state=tk.DISABLED)
save_button.pack(pady=10)

footer_label = tk.Label(root, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA", bg="gray", fg="white", height=2)
footer_label.pack(side=tk.BOTTOM, fill=tk.X)        
root.state('zoomed')

root.mainloop()
