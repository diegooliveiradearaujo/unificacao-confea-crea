import psycopg2 as pg
from sqlalchemy import create_engine
import streamlit as st
import datetime

conexao = pg.connect(host='dpg-cqdv1v0gph6c73ael0ug-a.oregon-postgres.render.com',
                     database='db_crea',
                     port='5432',
                     user='db_crea_user',
                     password='hAE7LxG7bsbo9iXAFOruV5TzGGiLJyU2'
                     )
conectado = conexao.cursor()

def inicio():
    st.title("Anotação de Responsabilidade Técnica - ART")
    st.header("1 - Responsável Técnico")

    st.write('**Antônio Carlos Pereira Siqueira**')
    st.write("**RNP:**"+" 6110163844")
    st.write('**Registro Regional:**'+' 6110163844CE')
    st.write('**Título Profissional:**'+' Engenheiro Civil')


    st.header("2 - Dados do Contratante")
    st.write('**Contratante:**'+' João Gonçalves Moura')
    st.write("**CPF/CNPJ:**"+" 4007009011")
    st.write('**Endereço:**'+' Rua I')
    st.write('**Bairro:**'+' Alagadiço')
    st.write('**Título Profissional:**'+' Engenheiro Civil')






    # sexo = st.selectbox("Sexo",("Masculino", "Feminino"))
    # tipo_registro = st.selectbox("Tipo de registro",("Registro Definitivo de Profissonal", "Registro Provisório de Profissional"))
    # nome = st.text_input('Nome')
    # nome_social = st.text_input('Nome Social')
    # cpf = st.text_input('CPF')
    # nome_pai = st.text_input('Nome do Pai')
    # nome_mae = st.text_input('Nome da Mãe')
    # data_nascimento = st.date_input("Data de Nascimento",datetime.date(1900,1,1))
    # pais = st.selectbox("País",("Argentina","Brasil"))
    # naturalidade = st.selectbox("Naturalidade",("Fortaleza","Belo Horizonte","São Paulo"))
    # estado = st.selectbox("Estado",("CE","MG","SP"))
    # rg = st.text_input('Identidade (RG)') 
    # data_expedicao = st.date_input("Data de Expedição",datetime.date(1900,1,1))
    # uf_expedicao = st.selectbox("UF Expedição",("CE","MG","SP")) 
    # orgao_expedidor = st.text_input('Orgão Expedidor')
    # estado_civil = st.selectbox("Estado Civil",("Solteiro(a)","Casado(a)","Viúvo(a)","Separado(a)"))   
    # celular = st.text_input('Celular')
    # telefone_residencial = st.text_input('Telefone Residencial')
    # email = st.text_input('Email')
    # email_confirma = st.text_input('Confirme o Email')


    # st.header("Endereço Residencial")
    # cep = st.text_input('CEP')
    # tipo_logradouro = st.selectbox("Tipo Logradouro",("Avenida","Beco","Rua","Vila"))   
    # logradouro = st.text_input('Logradouro')
    # numero = st.text_input('Número')
    # complemento = st.text_input('Complemento/Ponto de referência')
    # bairro = st.text_input('Bairro')
    # cidade = st.selectbox("Cidade",("Fortaleza","Belo Horizonte","São Paulo"))
    # uf = st.selectbox("UF",("CE","MG","SP")) 

    # if st.button("Cadastrar"):
    #     query = '''insert into transacao.profissional (sexo,tipo_registro,nome,nome_social,cpf,nome_pai,nome_mae,data_nascimento,pais,naturalidade,estado,rg,data_expedicao,uf_expedicao,orgao_expedidor,estado_civil,celular,telefone_residencial,email,email_confirma,cep,tipo_logradouro,logradouro,numero,complemento,bairro,cidade,uf) 
    #     values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

    #     conectado.execute(query,(sexo,tipo_registro,nome,nome_social,cpf,nome_pai,nome_mae,data_nascimento,pais,naturalidade,estado,rg,data_expedicao,uf_expedicao,orgao_expedidor,estado_civil,celular,telefone_residencial,email,email_confirma,cep,tipo_logradouro,logradouro,numero,complemento,bairro,cidade,uf))
    #     conexao.commit()
    #     st.write('Dados enviados com sucesso!')


   

    





    
    #pais = st.selectbox("País",("Brasil"))



    