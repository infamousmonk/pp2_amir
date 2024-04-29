import psycopg2
from config import params
from psycopg2 import Error
config = psycopg2.connect(**params)
current = config.cursor()
name = "Arman"
number = "3121414313"
#current.execute('CALL delete_by_number(%s)',(number,))
current.execute("CALL delete_by_name(%s)",(name,))
current.close()
config.commit()
config.close()