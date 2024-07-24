import services.database as db
import psycopg2 as pg
import models.Profissional as profissional


def incluir(profissional):
  try:
    sql = ''' 
    INSERT INTO transacao.Profissional (rnp,
                              registro_regional,
                              sexo, 
                              tipo_registro,
                              nome,
                              nome_social,
                              cpf,
                              nome_pai,
                              nome_mae,
                              data_nascimento,
                              pais,
                              naturalidade,
                              estado,
                              rg,
                              data_expedicao,
                              uf_expedicao,
                              orgao_expedidor,
                              estado_civil,
                              celular,
                              telefone_residencial,
                              email,
                              email_confirma,
                              cep,
                              tipo_logradouro,
                              logradouro,
                              numero,
                              complemento,
                              bairro,
                              cidade,
                              uf) 
    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    db.cursor.execute(sql, (
      profissional.rnp,
      profissional.registro_regional,
      profissional.sexo,
      profissional.tipo_registro,
      profissional.nome,
      profissional.nome_social,
      profissional.cpf,
      profissional.nome_pai,
      profissional.nome_mae,
      profissional.data_nascimento,
      profissional.pais,
      profissional.naturalidade,
      profissional.estado,
      profissional.rg,
      profissional.data_expedicao,
      profissional.uf_expedicao,
      profissional.orgao_expedidor,
      profissional.estado_civil,
      profissional.celular,
      profissional.telefone_residencial,
      profissional.email,
      profissional.email_confirma,
      profissional.cep,
      profissional.tipo_logradouro,
      profissional.logradouro,
      profissional.numero,
      profissional.complemento,
      profissional.bairro,
      profissional.cidade,
      profissional.uf
    ))

    db.conexao.commit()

  except pg.Error as e:
    print(f"Erro ao incluir profissional no banco de dados: {e}")
    # db.conexao.rollback()
  # finally:
    # db.cursor.close()
    # db.conexao.close()

def SelecionarTodos():
  try:
    cursor = db.conexao.cursor()
    db.cursor.execute('SELECT * FROM transacao.Profissional')
    profList = []

    for row in db.cursor.fetchall():
      profList.append(profissional.Profissional(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
        row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18],
        row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29]
      ))

    return profList
  except Exception as e:
    print(f"Erro ao selecionar profissionais: {e}")
  # finally:
  #   if 'cursor' in locals():
  #     cursor.close()