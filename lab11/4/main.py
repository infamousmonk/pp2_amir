import psycopg2
from config import params
config = psycopg2.connect(**params)
current = config.cursor()
pagination_by_limit = '''
    CREATE OR REPLACE FUNCTION pagination_by_limit(current_page INT,records_per_page INT,offset_1 INT)
     RETURNS TABLE(name VARCHAR,number VARCHAR) AS
    $$
    BEGIN
     RETURN QUERY
     SELECT * FROM Phonebook ORDER BY name LIMIT records_per_page OFFSET offset_1;
    END;
    $$
    LANGUAGE plpgsql;
'''
current.execute(pagination_by_limit)
current.close()
config.commit()
config.close()