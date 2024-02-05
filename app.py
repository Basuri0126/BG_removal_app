import streamlit as st
from rembg import remove
from PIL import Image
import numpy as np
from io import BytesIO


def remove_background(image):
    # Convert image to RGB if it has an alpha channel
    if image.mode == 'RGBA':
        image = image.convert('RGB')

    # Convert PIL image to NumPy array
    image_np = np.array(image)

    # Use rembg library to remove background
    output_image = remove(image_np)

    # Convert NumPy array back to PIL image
    result_image = Image.fromarray(output_image)

    return result_image

def main():
    st.title("Background Removal App")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the original image
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_column_width=True)

        # Remove background
        processed_image = remove_background(original_image)
        st.image(processed_image, caption="Image After Background Removal", use_column_width=True)


if __name__ == "__main__":
    main()
