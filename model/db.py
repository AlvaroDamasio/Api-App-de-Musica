import sqlite3

banco = sqlite3.connect("musicas_Db.db", check_same_thread=False)
cursor = banco.cursor()



def adicionar(musica, cantor, tom):
    
    cursor.execute(f"INSERT INTO musicas(musica, cantor, tom) VALUES('{musica}' , '{cantor}', '{tom}' )" )
    banco.commit()

""" """
def deleteOnDb(musica):
    cursor.execute(f"DELETE FROM musicas WHERE musica='{musica}';")
    banco.commit()

def read():

    musicas = []
    banco.row_factory= sqlite3.Row
    cursor.execute("SELECT rowid, *  FROM musicas ")
    rows = cursor.fetchall()
    print(rows)

    for i in rows:
        obj = {}
        obj["id"] = i[0]
        obj["musica"] = i[1]
        obj["cantor"] = i[2]
        obj["tom"] = i[3]
        musicas.append(obj)
        
    
    return musicas

def update(musicaParaAtualizar, novaMusica , novoCantor, novoTom):
    cursor.execute(f"UPDATE musicas SET musica ='{novaMusica}',cantor ='{novoCantor}', tom = '{novoTom}'  WHERE musica = '{musicaParaAtualizar}'; ") 
    banco.commit()   

def find(musica):
    musicas = []
    cursor.execute(f"SELECT rowid, *  FROM musicas WHERE musica = '{musica}'")
    rows = cursor.fetchall()
    for i in rows:
        obj = {}
        obj["id"] = i[0]
        obj["musica"] = i[1]
        obj["cantor"] = i[2]
        obj["tom"] = i[3]
        musicas.append(obj)

    return musicas    