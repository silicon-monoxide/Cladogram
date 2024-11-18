import streamlit as st
import cladogram_generator_PIL as clade_gen
import json

# the two inputs (text)
user_input = st.text_input("input:")
user_input_dimensions = st.text_input("image height/width (in pixels):")

#dropdown menu for line width
user_input_linew = st.selectbox(
    "Line Width", 
    ["Large", "Medium", "Small", "Smallest"]
    )

#optional settings
adv_set = st.checkbox("Advanced settings")


#if both have been filled out
if user_input and user_input_dimensions:
    # uses the locate_leaves function from the generator 
    # to get the list of leaf names
    user_lists = json.loads(user_input) #Note: maybe remove the line from the PIL file and do it all here?
    leaf_names = clade_gen.locate_leaves(user_lists)

    #list of heights of leaves, generated from a slider for each leaf (optional settings)
    heights = []
    if adv_set:
        for leaf in leaf_names:
            heights.append(st.slider(leaf+" height", 0, len(leaf_names), 0))
    
    # run the cladogram image generator
    clade_gen.run_program(user_input, 
        user_input_dimensions, 
        line_width=user_input_linew,
        heights_list=heights
    )
    #display the image (with a title above it)
    st.markdown("# Cladogram")
    st.image("cladogram.png", output_format="PNG")