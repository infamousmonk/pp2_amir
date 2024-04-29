import psycopg2
from config import params
config = psycopg2.connect(**params)
current = config.cursor()
insert_number = '''
    CREATE OR REPLACE PROCEDURE add_new_number(
        new_name VARCHAR,
        new_number VARCHAR
    )
    AS $$
    BEGIN
        IF EXISTS(SELECT * FROM phonebook WHERE phonebook.name = new_name) THEN
         UPDATE Phonebook SET number = new_number WHERE phonebook.name = new_name;
        ELSE
         INSERT INTO phonebook VALUES (new_name,new_number);
         END IF;
    END;        
    $$
    LANGUAGE PLPGSQL;
'''
current.execute(insert_number)
current.close()
config.commit()
config.close()