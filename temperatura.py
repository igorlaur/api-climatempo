# -*- coding: utf-8 -*-

API_URL = "https://advisor.climatempo.com.brhttp://apiadvisor.climatempo.com.br/api/v1/climate/rain/locale/3477?token=your-app-token/f4ee5d46deae19261dca80fd75477a5c"

def hello(nome, idade):
    print('Olá', nome, 'sua idade é', idade, 'anos')

hello('Fabio', 20)

def temp(id, latitude, longitude, token):
    print('ID: ', id, 'Latitude: ', latitude, 'Longitude', longitude, 'Token: ', token)

temp()