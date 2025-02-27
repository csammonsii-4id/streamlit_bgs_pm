import streamlit as st
import streamlit_authenticator as stauth

# Create a Hasher object with the list of passwords
hasher = stauth.Hasher(['123', '456'])

# Hash the passwords
hashed_passwords = hasher.generate()

# Print the hashed passwords to the console
print(hashed_passwords)