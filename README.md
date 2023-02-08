# Api-App-de-Musica

This is a API that provides routes to be consumed in outhers aplications

Requirements: 
Python 3.7+ 

## How to Install
### Run the commands 

pip install fastapi

pip install "uvicorn[standard]"

## Start the server
### Run this command:

uvicorn server:app --reload --host 0.0.0.0 --port 8000

## Rotas:
 http://localhost:8000/

This route is used to get all musics in data base and return a Json objects

http://localhost:8000/find/{musica}

This route find the music especified in parameter and return the music if found in database

http://localhost:8000/add/{musica}/{cantor}/{tom}

This route save in database the music especified in parameters whith the informations of name of music in first parameter singer in second parameter and the tone in the thirt parameter

http://localhost:8000/delete/{musica}

This route delete the music especified in the parameter

http://localhost:8000/update/{musicaParaAtualizar}/{musicaNova}/{cantorNovo}/{tomNovo}

This route update in database the music especified in parameters whith the informations of name of old music what will be updated in first parameter, the new music to be will save in second parameter,the new singer in the thirt parameter, and the new tone in the fourth parameter 

http://localhost:8000/docs

Provides the documentation of API
