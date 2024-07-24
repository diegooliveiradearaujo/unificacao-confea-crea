import streamlit as st
import controllers.ProfissionalController as ProfissionalController
import pandas as pd


def list():
  st.title('Profissionais')
  profList = []

  for item in ProfissionalController.SelecionarTodos():
    profList.append([
      item.rnp,
      item.registro_regional,
      item.sexo,
      item.tipo_registro,
      item.nome,
      item.nome_social,
      item.cpf,
      item.nome_pai,
      item.nome_mae,
      item.data_nascimento,
      item.pais,
      item.naturalidade,
      item.estado,
      item.rg,
      item.data_expedicao,
      item.uf_expedicao,
      item.orgao_expedidor,
      item.estado_civil,
      item.celular,
      item.telefone_residencial,
      item.email,
      item.email_confirma,
      item.cep,
      item.tipo_logradouro,
      item.logradouro,
      item.numero,
      item.complemento,
      item.bairro,
      item.cidade,
      item.uf])

  df = pd.DataFrame(
    profList, columns=[
      'RNP', 'Registro Regional', 'Sexo', 'Tipo de Registro', 'Nome', 'Nome Social',
      'CPF', 'Nome do Pai', 'Nome da Mãe', 'Data de Nascimento', 'País', 'Naturalidade',
      'Estado', 'RG', 'Data de Expedição', 'UF de Expedição', 'Orgão Expedidor',
      'Estado Civil', 'Celular', 'Telefone Residencial', 'Email', 'Email de Confirmação',
      'CEP', 'Tipo de Logradouro', 'Logradouro', 'Número', 'Complemento', 'Bairro',
      'Cidade', 'UF'
    ]
  )

  st.dataframe(df)

if __name__ == '__main__':
  list()