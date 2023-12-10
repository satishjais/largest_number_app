# Importing necessary libraries
import streamlit as st

# Define a function to find the largest number among three
def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

# Streamlit app content
def main():
    st.title("Find the Largest Number App")

    # Get user input for three numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Check if the numbers are not empty
    if num1 and num2 and num3:
        # Call the function to find the largest number
        result = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {result}")

# Run the Streamlit app
if __name__ == "__main__":
    main()