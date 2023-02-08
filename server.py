from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.db import *

app = FastAPI()




origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    
    result = read()
    return result

@app.get('/find/{musica}')
#essa função irá pesquisar no banco de dados e retornar a musica
def search(musica):
    result = find(musica)
    return result

@app.get('/add/{musica}/{cantor}/{tom}')
#essa função irá salvar no banco de dados
def add(musica, cantor, tom: str):
    tomUpper = tom.upper()
    adicionar(musica , cantor , tomUpper)

    result = {"Musica": musica,
                "cantor": cantor,
                "Tom": tomUpper
            }
    return result

@app.get('/delete/{musica}')
#esta rota deleta a musica por id
def delete(musica: str):
    deleteOnDb(musica)
    return musica

@app.get('/update/{musicaParaAtualizar}/{musicaNova}/{cantorNovo}/{tomNovo}')
def atualizar(musicaParaAtualizar, musicaNova,cantorNovo,tomNovo):
    print(musicaParaAtualizar)
    update(musicaParaAtualizar, musicaNova, cantorNovo, tomNovo)
    return {"status": "sucesso"}

