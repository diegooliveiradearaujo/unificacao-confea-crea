import streamlit as st
import datetime
import random
import string
import controllers.ProfissionalController as ProfissionalController
import models.Profissional as profissional

def IncluirProfissionalPage():
  st.title("Cadastrar Profissional")

  with st.form(key='include_profissional'):
    st.header("Dados Pessoais", divider='green')
    col1, col2 = st.columns(2)  

    with col1:
      sexo                  = st.selectbox("Sexo",("Masculino", "Feminino"), help="Selecione o sexo")
      nome                  = st.text_input('Nome')
      tipo_registro         = st.selectbox("Tipo de registro",("Registro Definitivo de Profissonal", "Registro Provisório de Profissional"))
      nome_social           = st.text_input('Nome Social')
      cpf                   = st.text_input('CPF')
      nome_pai              = st.text_input('Nome do Pai')
      nome_mae              = st.text_input('Nome da Mãe')
      data_nascimento       = st.date_input("Data de Nascimento",datetime.date(1980,1,1))
      pais                  = st.selectbox("País",("Argentina","Brasil"))
      email                 = st.text_input('Email')
    with col2:
      naturalidade          = st.selectbox("Naturalidade",("Fortaleza","Belo Horizonte","São Paulo"))
      estado                = st.selectbox("Estado",("CE","MG","SP"))
      rg                    = st.text_input('Identidade (RG)') 
      data_expedicao        = st.date_input("Data de Expedição",datetime.date(1980,1,1))
      uf_expedicao          = st.selectbox("UF Expedição",("CE","MG","SP")) 
      orgao_expedidor       = st.text_input('Orgão Expedidor')
      estado_civil          = st.selectbox("Estado Civil",("Solteiro(a)","Casado(a)","Viúvo(a)","Separado(a)"))   
      celular               = st.text_input('Celular')
      telefone_residencial  = st.text_input('Telefone Residencial')
      email_confirma        = st.text_input('Confirme o Email')

    st.header("Endereço Residencial", divider='green')
    col3, col4 = st.columns(2)  

    with col3:
      tipo_logradouro   = st.selectbox("Tipo Logradouro",("Avenida","Beco","Rua","Vila"))   
      logradouro        = st.text_input('Logradouro')
      cep               = st.text_input('CEP')
      complemento       = st.text_input('Complemento/Ponto de referência')

    with col4:
      numero            = st.text_input('Número')
      bairro            = st.text_input('Bairro')
      cidade            = st.selectbox("Cidade",("Fortaleza","Belo Horizonte","São Paulo"))
      uf                = st.selectbox("UF",("CE","MG","SP")) 
    
    rnp               = str(random.randint(10**9, (10**10)-1))
    registro_regional = rnp + uf

    input_button_submit = st.form_submit_button('Cadastrar', type='secondary')

  if input_button_submit:
    ProfissionalController.incluir(profissional.Profissional(rnp,registro_regional,sexo,tipo_registro,nome,nome_social,cpf,nome_pai,nome_mae,data_nascimento,pais,naturalidade,estado,rg,data_expedicao,uf_expedicao,orgao_expedidor,estado_civil,celular,telefone_residencial,email,email_confirma,cep,tipo_logradouro,logradouro,numero,complemento,bairro,cidade,uf))
    st.success('Profissional Criado com sucesso!')

# if __name__ == "__main__":
#   IncluirProfissionalPage()