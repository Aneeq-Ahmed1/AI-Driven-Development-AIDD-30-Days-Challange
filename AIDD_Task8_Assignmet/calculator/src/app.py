import streamlit as st
from calculator import calculate

# Page config
st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered",
)

# Title
st.markdown("<h1 style='text-align: center; color: #4B0082;'>🧮 Simple Calculator</h1>", unsafe_allow_html=True)
st.write("---")

# Input fields
num1 = st.number_input("Enter first number", format="%f")
num2 = st.number_input("Enter second number", format="%f")

# Operation selection with full names
operation_dict = {
    "Addition ➕": "+",
    "Subtraction ➖": "-",
    "Multiplication ✖️": "*",
    "Division ➗": "/"
}

operation_name = st.selectbox("Select Operation", list(operation_dict.keys()))
operation = operation_dict[operation_name]

# Calculate button with color
if st.button("Calculate", key="calc_btn"):
    try:
        expression = f"{num1} {operation} {num2}"
        result = calculate(expression)
        st.markdown(
            f"<h2 style='color: green; text-align: center;'>Result: {result}</h2>",
            unsafe_allow_html=True
        )
    except ZeroDivisionError:
        st.markdown(
            "<h3 style='color: red; text-align: center;'>Error: Cannot divide by zero.</h3>",
            unsafe_allow_html=True
        )
    except Exception as e:
        st.markdown(
            f"<h3 style='color: red; text-align: center;'>Error: {e}</h3>",
            unsafe_allow_html=True
        )

# Footer
st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
