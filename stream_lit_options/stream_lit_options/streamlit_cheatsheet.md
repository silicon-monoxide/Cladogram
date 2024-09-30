# Streamlit Demo Cheatsheet

## Page Configuration
```python
st.set_page_config(page_title="Title", layout="wide")
```
Sets the page title and layout.

## Text and Markdown
```python
st.title("Main Title")
st.header("Header")
st.markdown("# Heading 1")
st.markdown("## Heading 2")
st.markdown("### Heading 3")
st.markdown("**Bold Text**")
st.markdown("*Italic Text*")
st.markdown("`Code Text`")
st.write("Normal text or variables")
```

## Input Widgets
### Text Input
```python
user_input = st.text_input("Label", "Default Value")
```

### Slider
```python
value = st.slider("Label", min_value, max_value, default_value)
```

### Selectbox (Dropdown)
```python
option = st.selectbox("Label", ["Option1", "Option2", "Option3"])
```

### Checkbox
```python
if st.checkbox("Label"):
    # Do something when checked
```

## Layout
### Columns
```python
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1 content")
with col2:
    st.write("Column 2 content")
```

## Data Display
### DataFrame
```python
st.dataframe(df)
```

## Charts
### Line Chart
```python
st.line_chart(data)
```

## File Handling
### File Uploader
```python
uploaded_file = st.file_uploader("Label", type="file_extension")
```

### Image Display
```python
st.image(image, caption="Caption", use_column_width=True)
```

## Interactive Plots
### Plotly Chart
```python
st.plotly_chart(fig)
```

## Conditional Execution
```python
if condition:
    # Execute this block
```

## Running the App
In the terminal:
```
streamlit run your_script.py
```