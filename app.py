import streamlit as st
import random
from alberti import *


st.title("alberti wheels")

st.header('set wheels')
###get wheel lists
outerWheel = '1234ABCDEFGILMNOPQRSTVXZ'
innerWheel = 'acegklnprtvz&xysomqihfdb'

outerLetters = [letter for letter in outerWheel]
innerLetters = [letter for letter in innerWheel]

optOutLet = st.selectbox('set outer wheel',outerLetters)
optInLet = st.selectbox('set inner wheel',innerLetters)

key = "%s%s" % (optOutLet,optInLet)

st.write('Your Key: %s' % key)


####input text-cipher
st.header('input text to cipher')

defaultText = 'In the second century of the christian era'

user_input = st.text_area("cipher text",defaultText)
ciphWord = cipherCWText(user_input,startKey=key)

letters = [letter for letter in ciphWord]
cipher_text = ""
for i,letter in enumerate(letters):
  if i % 5 ==4:
    cipher_text = cipher_text + letter + ' '
  else:
    cipher_text = cipher_text + letter

st.subheader('enciphered')
st.write(cipher_text)

#####input text-decipher
st.header('input text to decipher')



user_input_decipher = st.text_area("cipher text")
deciphWord = deCipherCWText(user_input_decipher,startKey=key)
st.subheader('deciphered')
st.write(deciphWord)