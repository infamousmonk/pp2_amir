import psycopg2,re
from config import params
config = psycopg2.connect(**params)
current = config.cursor()
pattern_1 = r"\+{1}\d+$"
pattern_2 = r"\d+$"
def insert_many(a):
    for i in a:
        if re.match(pattern_1,i[1]) or re.match(pattern_2,i[1]):
            pass
        else:
            print("Impossible phone number")
            continue
        try:
            current.execute('CALL add_new_number(%s,%s)',(i[0],i[1]))
        except:
            print(f"number with name {i[0]} already written in the book")
        config.commit()
    current.close()     
    config.close()
array = [("Brat", "87779653657"),("Baga","87655424123"),("Vared","87756412341"),("Tara","748619871412")]
insert_many(array)