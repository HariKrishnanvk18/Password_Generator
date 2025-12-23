import random
import streamlit as st

# Page config
st.set_page_config(page_title="Password Generator", page_icon="🔐")

st.title("🔐 Random Password Generator")
st.write("Generate strong random passwords easily")

# Character set
random_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"

# User inputs
number_of_passwords = st.number_input(
    "Number of passwords to generate",
    min_value=1,
    max_value=20,
    value=1
)

password_length = st.number_input(
    "Length of each password",
    min_value=4,
    max_value=32,
    value=8
)

# Generate button
if st.button("Generate Password"):
    st.subheader("✅ Generated Password(s):")

    for i in range(number_of_passwords):
        password = ""
        for _ in range(password_length):
            password += random.choice(random_characters)

        st.code(password)
