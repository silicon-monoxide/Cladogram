import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image  # Add this import

def main():
    st.set_page_config(page_title="Streamlit Top 10 Features Demo", layout="wide")

    st.title("Top 10 Streamlit Features Demo")
    st.markdown("This demo showcases some of the most useful Streamlit features.")

    # 1. Text of different sizes and styles
    st.header("1. Text Formatting")
    st.markdown("# Heading 1")
    st.markdown("## Heading 2")
    st.markdown("### Heading 3")
    st.markdown("**Bold Text**")
    st.markdown("*Italic Text*")
    st.markdown("`Code Text`")

    # 2. Text Input
    st.header("2. Text Input")
    user_input = st.text_input("Enter your name", "John Doe")
    st.write(f"Hello, {user_input}!")

    # 3. Slider
    st.header("3. Slider")
    age = st.slider("Select your age", 0, 100, 25)
    st.write(f"You are {age} years old.")

    # 4. Dropdown (Selectbox)
    st.header("4. Dropdown")
    option = st.selectbox("Choose your favorite color", ["Red", "Green", "Blue", "Yellow"])
    st.write(f"Your favorite color is {option}.")

    # 5. Checkbox
    st.header("5. Checkbox")
    if st.checkbox("Show additional info"):
        st.write("Here's some additional information!")

    # 6. Columns
    st.header("6. Columns")
    col1, col2 = st.columns(2)
    with col1:
        st.write("This is column 1")
    with col2:
        st.write("This is column 2")

    # 7. DataFrames
    st.header("7. DataFrames")
    df = pd.DataFrame(
        np.random.randn(5, 3),
        columns=('Column 1', 'Column 2', 'Column 3')
    )
    st.dataframe(df)

    # 8. Charts
    st.header("8. Charts")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.line_chart(chart_data)

    # 9. File Uploader
    st.header("9. File Uploader")
    uploaded_file = st.file_uploader("Choose a PNG image", type="png")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded PNG Image', use_column_width=True)

    # 10. Interactive Plots
    st.header("10. Interactive Plots")
    df = px.data.gapminder().query("year == 2007")
    fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                     hover_name="country", log_x=True, size_max=60)
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()