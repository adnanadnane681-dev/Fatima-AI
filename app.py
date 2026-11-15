
from gtts import gTTS
import google.generativeai as genai
import os
import streamlit as st

# Saitin shafin Streamlit da Sunan Fatima AI
st.set_page_config(
    page_title='Fatima AI - Hausa Voice Assistant', page_icon='🤖'
)

# Nuna Hoton Logo a saman shafin (Zaka iya sanya hoton da ka zaba a nan ko barin sa)
st.title('Fatima AI 🤖')
st.subheader('Hausa Digital Assistant')

# Karɓar API Key na Gemini daga gurin mai amfani
api_key = st.text_input('Shigar da Gemini API Key ɗinka:', type='password')

if api_key:
  genai.configure(api_key=api_key)
  model = genai.GenerativeModel('gemini-pro')

  # Wurin rubuta sako daga mai amfani
  user_prompt = st.text_area(
    'Me kake so Fatima AI ta taimake ka da shi a yau?'
  )

  if st.button('Aika Sako'):
    if user_prompt:
      with st.spinner('Fatima tana tunani...'):
        # Samun amsa daga Gemini
        response = model.generate_content(
          user_prompt + ' (Ka ba da amsa a harshen Hausa kaɗai)'
        )
        response_text = response.text

        # Nuna rubutun amsar a shafin
        st.write('**Amsa:**')
        st.write(response_text)

        # Mayar da amsar ta zama murya (Text-to-Speech) a harshen Hausa
        tts = gTTS(text=str(response_text), lang='ha')
        audio_file = 'temp_audio.mp3'
        tts.save(audio_file)

        # Kunna sautin a cikin app din domin a saurara
        st.audio(audio_file, format='audio/mp3')
    else:
      st.warning('Don Allah rubuta sako kafin ka danna maɓallin aika wa.')
else:
  st.info('Don Allah shigar da Gemini API Key ɗinka a sama domin fara amfani da ita.')
    
