
import pandas as pd

data = [

    {"Index": 10, "Name": "Pedro", "Idade": 34, "Nota": 15, "Cidade": "São Paulo"},

    {"Index": 11, "Name": "Maria", "Idade": 59, "Nota": 12, "Cidade": "Rio de Janeiro"},

    {"Index": 12, "Name": "Janaina", "Idade": 68, "Nota": 18, "Cidade": "Belo Horizonte"},

    {"Index": 13, "Name": "Wong", "Idade": 89, "Nota": 17, "Cidade": "Curitiba"},

    {"Index": 14, "Name": "Roberto", "Idade": 98, "Nota": 19, "Cidade": "Porto Alegre"},

    {"Index": 15, "Name": "Marco", "Idade": 61, "Nota": 14, "Cidade": "Salvador"},

    {"Index": 16, "Name": "Paula", "Idade": 44, "Nota": 16, "Cidade": "Fortaleza"}

]

df = pd.DataFrame(data)

print(df)