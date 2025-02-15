import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
import os

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if file_path:
        image_entry.delete(0, tk.END)
        image_entry.insert(0, file_path)

def hide_text():
    file_path = image_entry.get().strip()
    input_text = text_entry.get("1.0", tk.END).strip()

    if not file_path or not input_text:
        messagebox.showerror("Error", "Please select an image and enter text to hide!")
        return

    try:
        # Open the image
        image = Image.open(file_path)

        # Convert image to RGBA (to support transparency in PNGs)
        if image.mode != "RGBA":
            image = image.convert("RGBA")

        img_array = np.array(image, dtype=np.uint8)  # Ensure uint8 format

        # Convert text to binary
        input_text += "###"  # Delimiter to mark the end
        binary_data = ''.join(format(ord(c), '08b') for c in input_text)

        if len(binary_data) > img_array.size:
            messagebox.showerror("Error", "Text is too large for this image!")
            return

        # Flatten pixel array and modify only the least significant bit (LSB)
        flat_pixels = img_array.flatten()
        binary_array = np.array(list(map(int, binary_data)), dtype=np.uint8)

        # Modify the LSB safely
        flat_pixels[:len(binary_array)] = (flat_pixels[:len(binary_array)] & 0xFE) | binary_array

        # Reshape back to original shape
        encoded_image = Image.fromarray(flat_pixels.reshape(img_array.shape), "RGBA")

        # Save as PNG (to avoid lossy formats like JPG)
        save_path = os.path.join(os.path.dirname(file_path), "stego_image.png")
        encoded_image.save(save_path, "PNG")

        messagebox.showinfo("Success", f"Steganography image saved at:\n{save_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
root = tk.Tk()
root.title("Hide Text in Image (Supports All Formats)")
root.geometry("400x250")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(pady=10)

tk.Label(frame, text="Select Image:").pack()
image_entry = tk.Entry(frame, width=40)
image_entry.pack()
tk.Button(frame, text="Browse", command=select_image).pack(pady=5)

tk.Label(frame, text="Enter Text to Hide:").pack()
text_entry = tk.Text(frame, height=3, width=40)
text_entry.pack()

tk.Button(frame, text="Hide Text", command=hide_text, bg="green", fg="white").pack(pady=10)

root.mainloop()
