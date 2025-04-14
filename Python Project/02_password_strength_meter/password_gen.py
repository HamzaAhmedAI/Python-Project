import streamlit as st 
import random
import string


def generate_password(lengeth, use_digit, use_special,):
    characters = string.ascii_letters                                # asscii_letters provides a-z and A-Z

    if use_digit: 
        characters += string.digits                                  # Add digits (0-9)

    if use_special:
        characters += string.punctuation                              # Add special characters (!@#$%^&*() etc.)

    return ''.join(random.choice(characters) for _ in range(lengeth))  # Generate password of specified length

st.title("🔑Password Generator") 

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)  # Slider to select password length

use_digit = st.checkbox("Include Digits (0-9)")                          # Checkbox to include digits

use_special = st.checkbox("Include Special Characters (!@#$%^&*())")     # Checkbox to include special characters

if st.button("Generate Password", use_container_width=True):  # Button to generate password
    password = generate_password(length, use_digit, use_special)       # Call the function to generate password
    st.markdown(f"<h1 style='text-align: center;'>Generated Password: <span style='color:red;'>{password}</span></h1>", unsafe_allow_html=True)                     # Display the generated password
    st.balloons()

st.markdown("<hr style='border:2px solid gray'>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>Made with ❤️ by <a href='#' style='text-decoration:none;'>Hamza Ahmed</a></p>", unsafe_allow_html=True)
