lst ={'A': True,'B': True, 'C': False}

s = '[A] and ([C] or [B]) or [C]'
#print(bool(s))
for a in lst.keys():
    f= '['+a+']'
    g= 'True' if lst.get(a) else 'False'
    s= s.replace(f,g)
print(s)
import sqlite3 as sq

connection = sq.connect('your_database_name.db')

cursor = connection.cursor()

cursor.execute('select '+s)
data = cursor.fetchall()

print(data[0][0])

cursor.close()
connection.close()