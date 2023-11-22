import os
import streamlit as st
import cv2
import numpy as np
from image_dehazer import remove_haze  # Replace 'your_dehazing_module' with the actual module name

def main():
    st.title("Image Dehazing with Streamlit")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Save the uploaded file to the 'images' folder
        file_path = os.path.join("images", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        # Read the image
        image = cv2.imread(file_path)

        # Display the original image
        st.image(image, caption="Original Image", use_column_width=True)

        # Dehaze the image
        dehazed_img, transmission_map = remove_haze(image)

        # Display the dehazed image
        st.image(dehazed_img, caption="Dehazed Image", use_column_width=True)

        # Display the transmission map
        st.image(transmission_map, caption="Haze Transmission Map", use_column_width=True)

if __name__ == "__main__":
    main()
