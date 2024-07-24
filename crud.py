from os import write
import streamlit as st

st.title('Incluir Clientes')

with st.form(key='include_cliente'):
  input_name = st.text_input(label='Insira o seu nome')
  input_age  = st.number_input(label='Insira sua idade', format='%d', step=1)
  input_occupation = st.selectbox(label='selecione sua profissão', 
  options=['Música', 'Designer', 'Engenheiro', 'Matemático'])
  input_button_submit = st.form_submit_button('Enviar')

if input_button_submit:
  st.write(f'Nome: {input_name}')
  st.write(f'Idade: {input_age}')
  st.write(f'Profissão: {input_occupation}')
  