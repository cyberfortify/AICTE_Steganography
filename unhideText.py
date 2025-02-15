import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if file_path:
        image_entry.delete(0, tk.END)
        image_entry.insert(0, file_path)

def unhide_text():
    file_path = image_entry.get().strip()
    if not file_path:
        messagebox.showerror("Error", "Please select an image!")
        return

    try:
        # Open the image
        image = Image.open(file_path)

        # Convert image to RGBA (ensures uniform pixel structure)
        if image.mode != "RGBA":
            image = image.convert("RGBA")

        img_array = np.array(image, dtype=np.uint8)  # Ensure uint8 format

        # Extract LSBs
        binary_data = ''.join(str(pixel & 1) for pixel in img_array.flatten())

        # Decode binary to text
        decoded_text = ""
        for i in range(0, len(binary_data), 8):
            char = chr(int(binary_data[i:i+8], 2))
            if decoded_text.endswith("###"):  # Stop at delimiter
                break
            decoded_text += char

        decoded_text = decoded_text.replace("###", "")

        if decoded_text:
            messagebox.showinfo("Extracted Text", f"Hidden Text:\n{decoded_text}")
        else:
            messagebox.showerror("Error", "No hidden text found!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
root = tk.Tk()
root.title("Extract Hidden Text (Supports All Formats)")
root.geometry("400x150")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(pady=10)

tk.Label(frame, text="Select Image:").pack()
image_entry = tk.Entry(frame, width=40)
image_entry.pack()
tk.Button(frame, text="Browse", command=select_image).pack(pady=5)

tk.Button(frame, text="Unhide Text", command=unhide_text, bg="blue", fg="white").pack(pady=10)

root.mainloop()
