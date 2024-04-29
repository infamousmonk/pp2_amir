from venv import create
import psycopg2
from config import params

config = psycopg2.connect(**params)
current = config.cursor()


sql_function = '''
    CREATE OR REPLACE FUNCTION get_by_pattern(pattern VARCHAR)
     RETURNS TABLE(name VARCHAR,number VARCHAR) AS
    $$
    BEGIN 
     RETURN QUERY
     SELECT *FROM phonebook where phonebook.number LIKE pattern;
    END;
    $$
    LANGUAGE plpgsql; 
'''
current.execute(sql_function)

current.close()
config.commit()
config.close()