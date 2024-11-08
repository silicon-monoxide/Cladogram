import streamlit as st
import cladogram_generator_PIL as clade_gen

# the two inputs (text)
user_input = st.text_input("input:")
user_input_dimensions = st.text_input("image height/width (in pixels):")

#dropdown menu for line width
user_input_linew = st.selectbox(
    "Line Width", 
    ["Large", "Medium", "Small", "Smallest"]
    )

#if both have been filled out
if user_input and user_input_dimensions:
    # run the cladogram image generator
    clade_gen.run_program(user_input, user_input_dimensions, user_input_linew)
    #display the image
    st.image("cladogram.png", output_format="PNG")