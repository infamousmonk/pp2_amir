import psycopg2
from config import params
config = psycopg2.connect(**params)
current = config.cursor()
delete_by_name = '''
    CREATE OR REPLACE PROCEDURE delete_by_name(
        delete_name VARCHAR
    )
    AS $$
    BEGIN
        IF EXISTS(SELECT * FROM phonebook WHERE Phonebook.name = delete_name) THEN
         DELETE FROM Phonebook WHERE Phonebook.name = delete_name;         
         END IF;
    END;        
    $$
    LANGUAGE PLPGSQL;
'''
delete_by_number = '''
    CREATE OR REPLACE PROCEDURE delete_by_number(
        delete_number VARCHAR
    )
    AS $$
    BEGIN
        IF EXISTS(SELECT * FROM phonebook WHERE Phonebook.number = delete_number) THEN
         DELETE FROM Phonebook WHERE Phonebook.number = delete_number;         
         END IF;
    END;        
    $$
    LANGUAGE PLPGSQL;
'''
current.execute(delete_by_name)
current.execute(delete_by_number)
current.close()
config.commit()
config.close()