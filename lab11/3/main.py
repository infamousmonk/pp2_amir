import psycopg2
from config import params
config = psycopg2.connect(**params)
current = config.cursor()
create = '''
CREATE TYPE array_table AS VARRAY() OF VARCHAR(50);
'''
insert_many_numbers = '''
    CREATE TYPE array_table AS TABLE OF VARCHAR;
    CREATE OR REPLACE PROCEDURE add_new_numbers(
        list IN VARRAY(n)
    )
    AS $$
    BEGIN
     INSERT INTO
'''
current.execute(create)
current.close()
config.commit()
config.close()