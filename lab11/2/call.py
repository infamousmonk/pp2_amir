import psycopg2
from config import params
from psycopg2 import Error
config = psycopg2.connect(**params)
current = config.cursor()
name = 'Arman'
number = '87767283492'
current.execute('CALL add_new_number(%s,%s)',(name,number))
current.close()
config.commit()
config.close()