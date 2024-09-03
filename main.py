import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from diffusers import StableDiffusionPipeline

import torch

# Initialize Tkinter app
app = tk.Tk()
app.geometry("400x400")
app.title("AI Image Generator")
ctk.set_appearance_mode("dark")

# Configure grid layout for the entire app
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=1)
app.rowconfigure(2, weight=1)
app.rowconfigure(3, weight=8)

# Create entry widget for user input
prompt = ctk.CTkEntry(app, height=35, text_color="black", fg_color="white")
prompt.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Create label widget to display generated image
lmain = ctk.CTkLabel(app, height=150, width=150)
lmain.grid(row=3, column=0, pady=10)

# Initialize StableDiffusionPipeline
modelId = "CompVis/stable-diffusion-v1-4"
device = "cpu"
pipe = StableDiffusionPipeline.from_pretrained(modelId)
pipe.to(device)

# Variable to hold the last generated image
tempImage = None

# Function to save generated image with prompt text as file name
def saveImage():
    global tempImage
    imgName = prompt.get()
    if tempImage:
        tempImage.save(f'{imgName}.png')

# Function to generate image based on user input
def generate(img_prompt):
    try:
        result = pipe(img_prompt, guidance_scale=8.5)
        image = result.images[0]
        return image
    except Exception as e:
        print(f"Error generating image: {e}")

# Event handler for "Generate Image" button
def onGenerate():
    global tempImage
    img_prompt = prompt.get()
    image = generate(img_prompt)
    tempImage = image
    if image:
        image.save('generatedImage.png')
        img = ImageTk.PhotoImage(image)
        lmain.configure(image=img)
        lmain.image = img

# Update prompt entry width based on window resize
def update_prompt_width(event):
    new_width = event.width - 20
    prompt.configure(width=new_width)

# Create "Generate Image" button
trigger = ctk.CTkButton(app, height=40, width=120, text_color="white", fg_color="blue", command=onGenerate)
trigger.configure(text="Generate Image")
trigger.grid(row=1, column=0, pady=10)

# Create "Save Image" button
save = ctk.CTkButton(app, height=40, width=120, text_color="white", fg_color="green", command=saveImage)
save.configure(text="Save Image")
save.grid(row=2, column=0, pady=10)

# Bind resize event to update prompt width
app.bind("<Configure>", update_prompt_width)

# Start Tkinter main loop
app.mainloop()
