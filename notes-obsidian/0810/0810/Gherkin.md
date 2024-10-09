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
- Dado que eu informo nota 1 for maior que a nota 2
- E nota 3 for maior que 10
- 

