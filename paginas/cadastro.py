import streamlit as st
import datetime
import random
import string

def inicio():
    
    st.title("Cadastro profissional")
    st.header("Dados Pessoais")
    sexo = st.selectbox("Sexo",("Masculino", "Feminino"))
    tipo_registro = st.selectbox("Tipo de registro",("Registro Definitivo de Profissonal", "Registro Provisório de Profissional"))
    nome = st.text_input('Nome')
    nome_social = st.text_input('Nome Social')
    cpf = st.text_input('CPF')
    nome_pai = st.text_input('Nome do Pai')
    nome_mae = st.text_input('Nome da Mãe')
    data_nascimento = st.date_input("Data de Nascimento",datetime.date(1900,1,1))
    pais = st.selectbox("País",("Argentina","Brasil"))
    naturalidade = st.selectbox("Naturalidade",("Fortaleza","Belo Horizonte","São Paulo"))
    estado = st.selectbox("Estado",("CE","MG","SP"))
    rg = st.text_input('Identidade (RG)') 
    data_expedicao = st.date_input("Data de Expedição",datetime.date(1900,1,1))
    uf_expedicao = st.selectbox("UF Expedição",("CE","MG","SP")) 
    orgao_expedidor = st.text_input('Orgão Expedidor')
    estado_civil = st.selectbox("Estado Civil",("Solteiro(a)","Casado(a)","Viúvo(a)","Separado(a)"))   
    celular = st.text_input('Celular')
    telefone_residencial = st.text_input('Telefone Residencial')
    email = st.text_input('Email')
    email_confirma = st.text_input('Confirme o Email')


    st.header("Endereço Residencial")
    cep = st.text_input('CEP')
    tipo_logradouro = st.selectbox("Tipo Logradouro",("Avenida","Beco","Rua","Vila"))   
    logradouro = st.text_input('Logradouro')
    numero = st.text_input('Número')
    complemento = st.text_input('Complemento/Ponto de referência')
    bairro = st.text_input('Bairro')
    cidade = st.selectbox("Cidade",("Fortaleza","Belo Horizonte","São Paulo"))
    uf = st.selectbox("UF",("CE","MG","SP")) 
    rnp = str(random.randint(10**9, (10**10)-1))
    registro_regional = rnp + uf

    if st.button("Cadastrar"):
        query = '''insert into transacao.profissional (rnp,registro_regional,sexo,tipo_registro,nome,nome_social,cpf,nome_pai,nome_mae,data_nascimento,pais,naturalidade,estado,rg,data_expedicao,uf_expedicao,orgao_expedidor,estado_civil,celular,telefone_residencial,email,email_confirma,cep,tipo_logradouro,logradouro,numero,complemento,bairro,cidade,uf) 
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

        conectado.execute(query,(rnp,registro_regional,sexo,tipo_registro,nome,nome_social,cpf,nome_pai,nome_mae,data_nascimento,pais,naturalidade,estado,rg,data_expedicao,uf_expedicao,orgao_expedidor,estado_civil,celular,telefone_residencial,email,email_confirma,cep,tipo_logradouro,logradouro,numero,complemento,bairro,cidade,uf))
        conexao.commit()
        st.write('Dados enviados com sucesso!')


   

    





    
    #pais = st.selectbox("País",("Brasil"))



    