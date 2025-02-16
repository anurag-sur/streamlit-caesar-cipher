import streamlit as st

# Define a function to perform the Caesar Cipher shift
def caesar_cipher(message, shift):

  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  new_text = ''
  for char in message:
    if char.isalpha():
      new_index = (alphabet.index(char.lower()) + shift) % 26
      new_char = alphabet[new_index]
      # Preserve case using ternary operator
      new_text += new_char.upper() if char.isupper() else new_char
    else:
      # Add the symbol directly without modification
      new_text += char
  return new_text

# Center the title and description with CSS
st.markdown("""
<style>
  .title {
    text-align: center;
  }
</style>

<h1 class="title">The Caesar Cipher</h1>
<p class="title">Encrypt or decrypt messages with ease!</p>
""", unsafe_allow_html=True)

# Create a container with full width for centering
with st.container():
  # Empty first column to push content to the center
  st.columns([1])

  # Center the remaining content using another container
  with st.container():
    # Rest of your existing app content goes here...
    st.expander("Enter your message and choose an action:", expanded=True)  # Set default to open
    message = st.text_area("Message:", key="message_input")
    # Removed validation check for message input

    action = st.radio("Action:", ("Encrypt", "Decrypt"), key="action", index=0) # Set default action to "Encrypt"

    shift = st.number_input("Shift value (1-25):", min_value=1, max_value=25, key="shift_value")

    # Submit button and results section
    if st.button("Submit"):
      if action == "Encrypt":
        cipher_text = caesar_cipher(message, shift)
        st.success(f"**Encrypted Text:** {cipher_text}") # Use markdown formatting for bold text
      else:
        plain_text = caesar_cipher(message, -shift)
        st.success(f"**Decrypted Text:** {plain_text}") # Use markdown formatting for bold text

st.markdown("""
<style>
  .title {
    text-align: center;
  }
</style>

<p class="title">
Created by Anurag Sur.
Check me out on Github!
</p>
""", unsafe_allow_html=True)
