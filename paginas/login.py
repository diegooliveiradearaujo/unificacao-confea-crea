import streamlit as st
import bcrypt

def login():
  st.title("Login")

  username = st.text_input("Username")
  password = st.text_input("Password", type="password")

  if st.button("Login"):
    # Adicione aqui a lógica de autenticação
    if username == "admin" and password == "123456":
      st.success("Login efetuado com sucesso!")
      return True
    else:
      st.error("Usuário ou Senha inválido")
      return False

def authenticate(username, password):
  valid_username = 'usuario'
  valid_password = b'$2b$12$hXhfywl1w/ZPQALJEArKC.QwXcaMA4mh51hdBzRB2sChyIEUQTMwW'  # bcrypt hash da senha 'senha123'

  if username == valid_username and bcrypt.checkpw(password.encode('utf-8'), valid_password):
    return True
  else:
    return False

def main():
  st.title('Login')

  username = st.text_input('Usuário')
  password = st.text_input('Senha', type='password')

  if st.button('Login'):
    if authenticate(username, password):
      st.success('Login bem-sucedido!')
      # redirecionar para outra página
    else:
      st.error('Nome de usuário ou senha incorretos')


if __name__ == '__main__':
  main()