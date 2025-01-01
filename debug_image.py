import streamlit as st

# Absolute path to an image
image_path = "/Users/shraddhadarade/Desktop/PROJECTS WINTER BREAK/Weather Forecast Data App/images/clear.png"

# Display the image
if st.button("Show Image"):
    st.image(image_path, caption="Test Image", use_column_width=True)
