Estudo de caso 1:
- Tira Sangue
	Primeiro eu insiro minha idade e meu peso após essa ação o sistema processa se a minha idade e maior que 18 e com peso menor que 80, com isso se for verdadeiro eu posso doar o sangue.
	Porém se for igual a 20 e peso igual 70,5 ele pode tirar uma quantidade média.
	Entretendo se idade for diferente de  30 peso 75 ele pode tirar uma quantidade maior.

Cenário:
- Dado que eu seja idade>18
- e peso < 80
- Quando for doar sangue
- Então eu estou apto a doar sangue(pode retira sangue 200ml)

Outro cenário se 
- Dado que eu seja idade == 20 
- e peso == 70.5
- Quando for doar sangue
- Então eu estou apto a doar sangue média(pode retirar 250ml)

Outro cenário se
- Dado que eu seja então != 30
- e peso != 75
- Quando for doar sangue
- Então eu apto a doar sangue máxima (pode retira 400ml)

Estudo de caso 2:
- Desconto de mercado
	Primeiro eu insiro o preço e a quantidade de produtos após essa ação o programa deve definir um tipo de desconto
Cenário:
- Dado que eu  informo preço > 10
-  E eu peço a quantidade <= 5
- Então a saída for verdadeiro 
- Eu recebo valor cheio com 30% de desconto

Outro cenário:
- Dado que eu informo preco == 20
- E eu peço a quantidade == 3
- Então a saída for verdadeiro
- Eu recebo valor com desconto  

Outro cenário:
- Dado que eu informo preco != 15.99 
- Ou eu peço a quantidade < 2
- Então a saída for verdadeiro
- Eu recebo valor cheio


Estudo de Caso 3:
- Nota aprovado ou arredondamento
	Eu insiro três valores, após essa ação o programa pode passar ou arrendondar a nota
- Dado que eu informo nota 1 for maior que a nota 2
- E nota 3 for maior que 10
- e somar nota1, nota2, nota3 dividido por 3 sendo maior ou igual a sete 
- Eu recebo o valor aprovado

Outro cenário:
- Dado que eu informo nota 1 for maior que a nota 2
- E nota 3 for maior que 10
- E somar nota1, nota2, nota3 dividido por 3 sendo maior ou igual a sete
- E se nota for igual a oito e nota3 for diferente de 9
- Eu recebo o valor arrendondado 


Estudo de caso 4:
- Verificar temperatura
	Primeiro eu insiro o valor temperatura e a Umidade, após essa ação o programa irá definir se a qualidade do ar e a temperatura está favorável.

Cenário:
- Quando a temperatura for igual ou maior a 25
- E a umidade for igual ou menor 70
- Então a saída for verdadeiro
- Eu recebo o valor temperatura alta e qualidade do ar ruim 

Outro cenário:
- Quando a temperatura for igual a 30 
- E a umidade for igual a 65.5
- Então a saída for verdadeiro
- Eu recebo o valor temperatura extrema qualidade do ar péssima 

outro cenário:
- Quando a temperatura for diferente a 20 
- E a umidade for maior que 60
- Então a saída for verdadeiro
- Eu recebo o valor temperatura fria qualidade do ar boa


Estudo de caso 5:
- Definir salários 
	Primeiro eu insiro o valor salario e horas trabalhadas, após essa ação o programa irá
	definir um salário padrão.

Cenário:
- Quando eu insiro a horas trabalhadas for igual 40
- E se o salario for maior que 2,000
- Então a saída for verdadeiro
- Eu recebo o retorno "Dois salários mínimos"

Outro Cenário:
- Quando eu insiro a horas trabalhadas for menor que 45
- E se o salario for maior ou igual que 2,000
- Então a saída for verdadeiro
- Eu recebo o retorno "Salário com bônus"

Outro Cenário:
- Quando eu insiro a horas trabalhadas for diferente 35
- E se o salario for menor que 3,000
- Então a saída for verdadeiro
- Eu recebo o retorno "Salário de estágio"