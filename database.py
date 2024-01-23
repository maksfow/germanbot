import sqlite3
conn=sqlite3.connect("mydata.db",check_same_thread=False)
sql=conn.cursor()
sql.execute("CREATE TABLE IF NOT EXISTS words(word TEXT,translate TEXT);")
def register(wordb,translatee):
     sql.execute("INSERT INTO words VALUES(?,?);", (wordb,translatee))
     conn.commit()
def ask_nem():
    a=sql.execute("SELECT word FROM words;").fetchall()
    return a

def ask_ru():
    a=sql.execute("SELECT translate FROM words;").fetchall()
    return a


incorrect_answers = 0

def ask_translate(wordb,q):
    global incorrect_answers
    a = sql.execute("SELECT translate FROM words WHERE  word=?", (q,)).fetchone()

    if a and a[0] == wordb:
        return "Так держать!Пройдем тест еще раз)?"
    else:
        incorrect_answers += 1
        return f"Кабачок,подумай еще раз!!!!\nКоличество ошибок: {incorrect_answers}"



def ask_translate_ru(wordb,q):
    global incorrect_answers
    a = sql.execute("SELECT word FROM words WHERE  translate=?", (q,)).fetchone()

    if a and a[0] == wordb:
        return "Так держать!Пройдем тест еще раз)?"
    else:
        incorrect_answers += 1
        return f"Кабачок,подумай еще раз!!!!\nКоличество ошибок: {incorrect_answers}"





