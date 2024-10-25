import streamlit as st
import cladogram_generator_PIL as clade_gen

user_input = st.text_input("input:")
user_input_dimensions = st.text_input("image height/width (in pixels):")
st.image("cladogram.png")
clade_gen.run_program('[[["clade zero"]], "clade one", ["clade two", ["clade three", "clade four", [[[0]], "clade five"], "clade six"]]]', "900")