import json

usuario = {
    'nome':'emilia',
    'idade': 15,
    'cep': 88888-88
}

with open('dados.json' ,'w', encoding='utf8') as leitura:
    json.dump(
        usuario,
        leitura,
        indent=2
    )
    
    
    #leitura.write('ATENÇÃO!!')

with open('dados.json','r',encoding='utf8') as leitura:
    pessoa = json.load(leitura)
    print(pessoa['nome'])