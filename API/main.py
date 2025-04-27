from fastapi import FastAPI, Query
import requests


app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que mostra o hello world
    '''
    return {'hello':'world'}

@app.get('/api/restaurantes')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardapios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    
    print(response)
    dados_restaurante = []

    if response.status_code == 200:
        dados = response.json()

        if restaurante is None:
            return {'dados': dados}

        for item in dados:
            if item['Company'] == restaurante:            
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
        #print(dados_restaurante['McDonald’s'])
    else:
        print('deu erro na API')