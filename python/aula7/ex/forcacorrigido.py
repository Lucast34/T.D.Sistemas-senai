def exercicio3():
    tentativa = 6
    palavra_secreta = 'PYTHON'
    letras_p_secreta = set(palavra_secreta)

    letras_tentaivas = set()

    while tentativa > 0 and letras_p_secreta:
        #exibir a palavra 
        palavra_exibida = []
        for letra in letras_p_secreta:
            palavra_exibida.append(letra)
        else:
            palavra_exibida.append('_')

        print('Palavra',' '.join(palavra_exibida))

        #pedir uma letra 
        letra = input('Digite uma letra: ').upper()
        
        #tentativa 
        letras_tentaivas.add(letra)

        #verificar acerto
        if letra in letras_p_secreta:
            print(f'BOA! a letra {letra} esta na palavra!')
            letras_p_secreta.remove(letra)
        else:
            print(f'ERROU! a letra {letra} não existe')
            tentativa -= 1
            print(f'Vidas restantes: {tentativa}')
        
    # tentativas > 0
    if not letras_p_secreta:
        print(f'VOCÊ GANHOU O JOGO! palavra secreta{palavra_secreta}')
    else:
        print(f'GAME OVER! a plavra secreta {palavra_secreta}')
exercicio3()