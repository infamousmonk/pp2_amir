import psycopg2
from config import params
config = psycopg2.connect(**params)
current = config.cursor()
current_page,records_per_page = map(int,input().split())
offset = (current_page - 1) * records_per_page
current.callproc('pagination_by_limit',(current_page,records_per_page,offset))
output = current.fetchall()
print(output)
current.close()
config.commit()
config.close()