import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

def generate_name_image(name, font_size=60, width=400, height=200):
    # Create a new image with white background
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)
    
    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    
    # Get the size of the text
    left, top, right, bottom = font.getbbox(name)
    text_width = right - left
    text_height = bottom - top
    
    # Calculate the position to center the text
    position = ((width - text_width) / 2, (height - text_height) / 2)
    
    # Draw the text on the image
    draw.text(position, name, fill='black', font=font)
    
    return image

st.title("Name Image Generator")

# Text input for the name
name = st.text_input("Enter a name:")

if name:
    # Generate the image
    img = generate_name_image(name)
    
    # Convert PIL Image to bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    # Display the image
    st.image(img_byte_arr, caption=f'Generated image for "{name}"', use_column_width=True)
    
    # Provide a download button
    st.download_button(
        label="Download Image",
        data=img_byte_arr,
        file_name=f"{name}.png",
        mime="image/png"
    )