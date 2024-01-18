import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from PIL import Image
import os

class ImageToPDF:
    def __init__(self,root):
            self.root = root
            self.image_parth =[]
            self.output_pdf_name= tk.StringVar()
            self.selected_image_listbox = tk.Listbox(root,selectmode=tk.MULTIPLE)

            self.initialize_ui()

    def initialize_ui(self):
        title_label=tk.Label(self.root,text="Image to PDF Converter",font=("arial",18,"bold"))
        title_label.pack(pady=10)

        select_images_button = tk.Button(self.root, text="Select Images", command=self.select_images)
        select_images_button.pack(pady=(0, 10))

        self.selected_image_listbox.pack(pady=(0,10),fill=tk.BOTH, expand=True)

        label = tk.Label(self.root,text ="Enter output PDF name:")
        label.pack()

        pdf_name_entry = tk.Entry(self.root,textvariable=self.output_pdf_name,width=40,justify='center')
        pdf_name_entry.pack()

        convert_button = tk.Button(self.root, text="Convert To PDf", command=self.convert_images_to_pdf)
        convert_button.pack(pady=(20, 40))

    def  select_images(self):
        self.image_parth=filedialog.askopenfilenames(title="Select Images",filetypes=[("Image Files","*.jpg,*.jpeg,*.png")])
        self.update_selected_images_listbox()

    def update_selected_images_listbox(self):
        self.selected_image_listbox.delete(0,tk.END)

        for image_path in self.image_parth:
            _,image_name = os.path.split(image_path)
            self.selected_image_listbox.insert(tk.END,image_path)

    def convert_images_to_pdf(self):
        if not self.image_parth:
            return
        output_pdf_path=self.output_pdf_name.get()+".pdf" if self.output_pdf_name.get() else "output.pdf"

        pdf =canvas.Canvas(output_pdf_path,pagesize=(612, 792))

        for image_path in self.image_parth:
            img = Image.open(image_path)
            avalabale_width=540
            avalable_hight=720

            scale_factor =min(avalabale_width / img.width, avalable_hight/ img.height)
            new_width = img.width * scale_factor
            new_height =img.height * scale_factor
            x_centered=(612 - new_width)/2
            y_centered=(792 - new_height)/2

            pd








def main():
    root = tk.Tk()
    root.title("Image to PDF")
    converter=ImageToPDF(root)
    root.geometry("400x600")
    root.minsize(width=400, height=400)
    root.maxsize(width=400, height=400)
    root.resizable(width=False, height=False)
    root.mainloop()

if __name__ == "__main__":
    main()


