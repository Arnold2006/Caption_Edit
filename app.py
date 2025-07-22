import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Billede og Tekst Editor")
        
        self.left_frame = tk.Frame(root)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.image_label = tk.Label(self.left_frame)
        self.image_label.pack()
        
        self.text_widget = tk.Text(self.right_frame)
        self.text_widget.pack(fill=tk.BOTH, expand=True)
        
        self.load_button = tk.Button(root, text="Indlæs Billede og Tekst", command=self.load_files)
        self.load_button.pack()
        
        self.save_button = tk.Button(root, text="Gem Tekst", command=self.save_text)
        self.save_button.pack()
        
        self.image_path = None
        self.text_file_path = None

    def load_files(self):
        image_path = filedialog.askopenfilename(filetypes=[("Billedfiler", "*.jpg *.png")])
        if image_path:
            self.image_path = image_path
            base_name = os.path.splitext(image_path)[0]
            self.text_file_path = base_name + '.txt'
            
            img = Image.open(image_path)
            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            
            if os.path.exists(self.text_file_path):
                with open(self.text_file_path, 'r') as f:
                    content = f.read()
            else:
                content = ''
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, content)

    def save_text(self):
        if self.text_file_path:
            content = self.text_widget.get(1.0, tk.END)
            with open(self.text_file_path, 'w') as f:
                f.write(content)
            messagebox.showinfo("Success", "Tekst gemt!")
        else:
            messagebox.showerror("Fejl", "Ingen tekstfil indlæst.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageTextEditor(root)
    root.mainloop()
