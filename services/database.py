import psycopg2 as pg
from sqlalchemy import create_engine

conexao = pg.connect(
  host='dpg-cqdv1v0gph6c73ael0ug-a.oregon-postgres.render.com',
  database='db_crea',
  port='5432',
  user='db_crea_user',
  password='hAE7LxG7bsbo9iXAFOruV5TzGGiLJyU2'
)
cursor = conexao.cursor()