#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

// espa�o deticado a fun��o
void resultado(float resul);

void maiormenor(float numeroM, float numeroN);
// foi declarado depois por�m vai ser usado depois 

int main(void){
	float 
		n1,
		n2,
		result;
	
	printf("\nDigite a primeira nota:\n");
	
	scanf("%f", &n1); // pegando o input
	
	printf("\nDigite a segunda nota:\n");
	
	scanf("%f",&n2); //pegando o segundo input
	
	result = (n1 + n2)/2;  // opera��o
	
	// fun��o 1
	resultado(result);
	// fun��o 2
	maiormenor(n1, n2);
	
	printf("\nO resultado foi %.2f\n\n", result);
	
	system("PAUSE"); // pausando o sistema 

	return 0; // Fim do programa
}

void resultado (float resul){
	if (resul >= 5){
		puts("O aluno foi aprovado\n");
	} else {
		puts("O aluno foi reprovado\n");
	}
}

void maiormenor (float numeroM, float numeroN){
	if (numeroM > numeroN){
			printf("A maior nota foi %.2f", numeroM);
	} else{
		printf("A maior nota foi %.2f", numeroN);
	}
}



