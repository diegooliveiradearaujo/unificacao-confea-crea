import streamlit as st
import paginas.art as a
import controllers.ProfissionalController as ProfissionalController
import models.Profissional as profissional
import pages.profissional.create as PageCreateProfissional
import pages.profissional.list as PageListProfissional
import pages.profissional.bi as PageBIProfissional

import paginas.crea as crea
import paginas.confea as confea

st.set_page_config(page_title="Sistema Nacional Unificado de Gerenciamento de Profissionais dos CREAs")
cor_de_fundo = "#f0f0f0"
image1 = "https://cdn.confea.org.br/assets/img/logo/confea.png"
image2 = 'https://www.chiaviniesantos.com/wp-content/uploads/2018/09/logo-sistema-confea-crea-2.png'
image3 = 'https://www.mutua.com.br/wp-content/uploads/2022/12/logo_mutua.webp'

st.sidebar.image(image1, use_column_width=True)

st.sidebar.title("Sistema Nacional de Unificação dos CREAs")
pagina_profissional = st.sidebar.selectbox('Profissional',
  ['Power BI - Usuário CREA', 'Power BI - Usuário CONFEA', 'Cadastrar', 'Consultar', 'Acessar ART'])

# Power BI
if pagina_profissional == 'Power BI - Usuário CREA':
  crea.inicio()
if pagina_profissional == 'Power BI - Usuário CONFEA':
  confea.inicio()      

if pagina_profissional == 'Cadastrar':
  PageCreateProfissional.IncluirProfissionalPage()
if pagina_profissional == 'Consultar':
  PageListProfissional.list()
if pagina_profissional == 'Acessar ART':
  a.inicio()     
# if pagina_profissional == 'Power BI':
#   PageBIProfissional.index()





# st.markdown(f'<div style="background-color: {cor_de_fundo}; display: flex; justify-content: center; align-items: center; height: 100px; width: 100px; border-radius: 10px;">', unsafe_allow_html=True)
# col1, col2 = st.columns(2)
# with col1:
#   st.image(image2, width=200)
# with col2:
#   st.image(image3, width=200)
# st.markdown('</div>', unsafe_allow_html=True)

# st.markdown('<style>footer {position: fixed; bottom: 0; left: 0; width: 100%; background-color: ' + cor_de_fundo + '; text-align: center; padding: 10px;}</style>', unsafe_allow_html=True)
# st.markdown('<footer><img src="https://www.chiaviniesantos.com/wp-content/uploads/2018/09/logo-sistema-confea-crea-2.png" style="max-height: 50px; vertical-align: middle;"></footer>', unsafe_allow_html=True)
# st.markdown('<footer><img src="https://www.mutua.com.br/wp-content/uploads/2022/12/logo_mutua.webp" style="max-height: 50px; vertical-align: middle;"></footer>', unsafe_allow_html=True)

# Estilizando o rodapé
st.markdown('<style>footer {position: fixed; bottom: 0; left: 0; width: 100%; background-color: ' + cor_de_fundo + '; text-align: center; padding: 10px; display: flex; justify-content: space-around;}</style>', unsafe_allow_html=True)

# Inserindo as imagens no rodapé
st.markdown('<footer><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdWEhISBcenXIMjJqA8m6C4jlyhfzObVV9ZbAyl41X3T6bUcJjvV1yjylAbkFlKkDfiQ&usqp=CAU" style="max-height: 50px; vertical-align: middle; margin-right: 10px;"></img><img src="https://www.mutua.com.br/wp-content/uploads/2022/12/logo_mutua.webp" style="max-height: 50px; vertical-align: middle; margin-left: 10px;"></footer>', unsafe_allow_html=True)
