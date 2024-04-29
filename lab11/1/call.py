import psycopg2
from config import params
config = psycopg2.connect(**params)
current = config.cursor()
pattern = input()
pattern = "%"+pattern+"%"
current.callproc('get_by_pattern',(pattern,))
result = current.fetchall()
for row in result:
    print(row[0],row[1])
current.close()
config.commit()
config.close()