import streamlit as st

def largest_number(num1, num2, num3):
    return max(num1, num2, num3)

st.title("Largest Number Finder")

# User input for three numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find Largest Number"):
    if num1 == num2 == num3:
        st.warning("All numbers are equal.")
    else:
        result = largest_number(num1, num2, num3)
        st.success(f"The largest number is: {result}")
