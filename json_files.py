#primeiro você precisa importar a biblioteca json
import json

#principais operações em python relacionados a um json
#escrever e salvar dados em um arquivo formato json
#estrutura:
#json_value = '''
#{
#    "list":[
#    {
#        "key1":"value1",
#        "key2":"value2"
#    },
#    {
#        "key1":"value3",
#        "key2":"value4"
#    }
#    ]
#}
#'''

#Exemplo
melhor_jogo = '''
{
    "jogos": [
        {
            "nome": "Elden Ring",
            "nota": "9.5",
            "produtora": "FromSoftware"
        },
        {
            "nome": "Sekiro",
            "nota": "10",
            "produtora": "FromSoftware"
        }
    ]
}
'''
#agora pegamos a informação desse json e colocamos em um objeto

data = json.loads(melhor_jogo)

print(data)

#transformando essas informações em um objeto python é mais facil de trabalhar com eles, por exemplo

#aqui ele vai retornar apenas o nome do jogo
for jogo in data['jogos']:
    print(jogo['nome'])

#com isso podemos tambem manipular os arquivos

for jogo in data['jogos']:
    del jogo['produtora']

#usando indent podemos indentar para facilitar a visualização
new_data = json.dumps(data, indent=2)

print(new_data)
