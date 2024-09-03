
# AI Image Generator

### AI Image Generator Using Stable Diffusion

**Overview**:  
This project is an AI-powered tool that generates high-quality images from user-provided text prompts using the **Stable Diffusion** model. Built with Python, **Tkinter**, and **CustomTkinter**, the app provides a simple GUI where users can input text, generate images, and save them.

**Key Features**:
- **User-Friendly Interface**: Built with Tkinter for easy interaction.
- **Text-to-Image Generation**: Utilizes the Stable Diffusion model (`CompVis/stable-diffusion-v1-4`) for creating images from text.
- **Preview and Save Images**: Generated images are displayed in the app, and users can save them locally with custom filenames.
- **Error Handling**: Handles exceptions during image generation.

**Requirements**:
- Python 3.8+, `Tkinter`, `CustomTkinter`, `PIL`, `diffusers`, `torch`.



### Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary libraries:

1. **CustomTkinter**: A modern and customizable UI library based on Tkinter.
   ```bash
   pip install customtkinter
   ```

2. **Pillow (PIL)**: Python Imaging Library for handling image operations.
   ```bash
   pip install Pillow
   ```

3. **Diffusers**: Hugging Face library for running diffusion models like Stable Diffusion.
   ```bash
   pip install diffusers
   ```

4. **PyTorch**: Deep learning framework needed to run the Stable Diffusion model.
   ```bash
   pip install torch
   ```

5. **Transformers**: Needed by the diffusers library for running Stable Diffusion models.
   ```bash
   pip install transformers
   ```

6. **Accelerate** (optional): For optimizing the model's performance.
   ```bash
   pip install accelerate
   ```

---

### Results
- **Image Generation**: Generates high-quality images based on user text prompts, displayed in the app.
- **Image Quality**: Produces detailed and contextually relevant visuals.
- **User Experience**: Provides a straightforward GUI for easy image generation and saving.

---
