# import os
# from tkinter import Tk, Label, Button, filedialog, StringVar, Entry
# from PIL import Image, ImageDraw, ImageFont
# import pandas as pd
# from fpdf import FPDF

# # Certificate Generator Function
# def generate_certificates():
#     try:
#         template_path = filedialog.askopenfilename(title="Select Certificate Template", filetypes=[("Image Files", "Svvv.jpg")])
#         data_path = filedialog.askopenfilename(title="Select Excel/CSV File", filetypes=[("Excel Files", "sv.xlsx")])

#         if not template_path or not data_path:
#             status.set("File selection canceled!")
#             return

#         # Load template
#         template = Image.open(template_path)
#         draw = ImageDraw.Draw(template)
        
#         # Font Configuration
#         font_path = filedialog.askopenfilename(title="Select Font File", filetypes=[("Font Files", "*.ttf")])
#         font_size = int(font_size_var.get())
#         font = ImageFont.truetype(font_path, font_size)
        
#         # Load recipient data
#         data = pd.read_excel(data_path) if data_path.endswith('.xlsx') else pd.read_csv(data_path)
#         output_dir = filedialog.askdirectory(title="Select Output Directory")

#         if not output_dir:
#             status.set("Output directory not selected!")
#             return

#         for _, row in data.iterrows():
#             recipient_name = row['Name']
#             output_path = os.path.join(output_dir, f"{recipient_name}.pdf")
            
#             # Customize certificate
#             certificate = template.copy()
#             draw = ImageDraw.Draw(certificate)
#             text_width, text_height = draw.textsize(recipient_name, font=font)
#             position = ((certificate.width - text_width) // 2, 300)  # Centered text
#             draw.text(position, recipient_name, fill="black", font=font)

#             # Save as PDF
#             pdf = FPDF()
#             pdf.add_page()
#             pdf.image(certificate, x=10, y=10, w=190)
#             pdf.output(output_path)

#         status.set("Certificates generated successfully!")
#     except Exception as e:
#         status.set(f"Error: {e}")

# # UI Setup
# root = Tk()
# root.title("Certificate Generator")
# root.geometry("400x200")

# Label(root, text="Font Size:").pack(pady=5)
# font_size_var = StringVar(value="32")
# Entry(root, textvariable=font_size_var).pack(pady=5)

# Button(root, text="Generate Certificates", command=generate_certificates).pack(pady=20)

# status = StringVar(value="Status: Waiting...")
# Label(root, textvariable=status, fg="green").pack(pady=5)

# root.mainloop()

# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageDraw, ImageFont
# import os

# def select_template():
#     global template_path
#     template_path = filedialog.askopenfilename(title="Select Template", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
#     if template_path:
#         template_label.config(text="Template Selected: " + os.path.basename(template_path))

# def generate_certificate():
#     name = name_entry.get()
#     course = course_entry.get()
#     date = date_entry.get()
    
#     if not template_path or not name or not course or not date:
#         messagebox.showerror("Error", "All fields are required!")
#         return

#     # Load the template
#     img = Image.open(template_path)
#     draw = ImageDraw.Draw(img)

#     # Set font (You may need to download custom fonts)
#     font = ImageFont.truetype("arial.ttf", 40)

#     # Coordinates to place text (adjust as per your template)
#     draw.text((300, 200), f"Name: {name}", fill="black", font=font)
#     draw.text((300, 300), f"Course: {course}", fill="black", font=font)
#     draw.text((300, 400), f"Date: {date}", fill="black", font=font)

# # Save the output
#     output_path = os.path.join("certificates", f"{name}_certificate.png")
#     os.makedirs("certificates", exist_ok=True)
#     img.save(output_path)
#     messagebox.showinfo("Success", f"Certificate saved at: {output_path}")

# # UI Setup
# root = tk.Tk()
# root.title("Certificate Generator")

# template_path = ""

# tk.Label(root, text="Certificate Generator", font=("Helvetica", 18, "bold")).pack(pady=10)
# template_label = tk.Label(root, text="No Template Selected")
# template_label.pack(pady=5)

# tk.Button(root, text="Select Template", command=select_template).pack(pady=5)

# tk.Label(root, text="Name:").pack()
# name_entry = tk.Entry(root, width=30)
# name_entry.pack()

# tk.Label(root, text="Course:").pack()
# course_entry = tk.Entry(root, width=30)
# course_entry.pack()

# tk.Label(root, text="Date:").pack()
# date_entry = tk.Entry(root, width=30)
# date_entry.pack()

# tk.Button(root, text="Generate Certificate", command=generate_certificate).pack(pady=20)

# root.mainloop()

import cv2
import datetime
from tkinter import Tk, Label, Button, filedialog, StringVar, Entry, messagebox

# Function to generate a certificate for the provided name
def generate_certificate():
    try:
        name = name_var.get().strip()
        if not name:
            messagebox.showerror("Input Error", "Name cannot be empty!")
            return
        
        # Get certificate template path
        template_path = filedialog.askopenfilename(title="Select Certificate Template", filetypes=[("Image Files", "*.jpg;*.png")])
        if not template_path:
            messagebox.showerror("Template Error", "Certificate template not selected!")
            return

        # Output directory
        output_folder = filedialog.askdirectory(title="Select Output Directory")
        if not output_folder:
            messagebox.showerror("Output Error", "Output directory not selected!")
            return
        
        # Generate certificate
        template = cv2.imread(template_path)
        if template is None:
            messagebox.showerror("Template Error", "Failed to load the template image!")
            return
        
        # Language and date
        language_name = language_var.get().strip() or "Python"
        dt = datetime.datetime.now()

        # Add text to template
        cv2.putText(template, name, (766, 734), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(template, str(dt.date()), (250, 1172), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(template, language_name, (1238, 786), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        
        # Save the certificate
        output_path = f"{output_folder}/{name}.jpg"
        cv2.imwrite(output_path, template)

        messagebox.showinfo("Success", f"Certificate generated successfully!\nSaved to: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# UI Setup
root = Tk()
root.title("Certificate Generator")
root.geometry("500x300")

# Name Input
Label(root, text="Enter Recipient Name:").pack(pady=10)
name_var = StringVar()
Entry(root, textvariable=name_var).pack(pady=5)

# Programming Language Input
Label(root, text="Programming Language (default: Python):").pack(pady=10)
language_var = StringVar(value="Python")
Entry(root, textvariable=language_var).pack(pady=5)

# Generate Certificate Button
Button(root, text="Generate Certificate", command=generate_certificate).pack(pady=20)

# Start the application
root.mainloop()
