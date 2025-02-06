# include <stdio.h> // biblioteca de i/o
# include <stdlib.h> // biblioteca básico
# include <math.h>

/* Espaço para protipos de função */
void resultado(float result);

int main(void){
	float 
		nota1, 
		nota2, 
		resul; // notas
	
	printf("Digite as suas notas\n");
	
	scanf("%f%f", &nota1, &nota2);
	
	while(getchar() != '\n');
	
	resul = (nota1 + nota2)/2;
	resultado(resul);
	
	printf("Media --> %.2f\n", resul);
	
	// estrutura de repetição
	
	if(nota1 > nota2){
		printf("A maior nota foi %.2f\n", nota1);
	}
	else {
		printf("A Maior nota foi %.2f\n", nota2);
	};
	
	system("PAUSE");
	
	return 0; // Fim do programa
}

void resultado(float result){
	if (result >= 5) puts("Aprovado!");
	else puts("Reprovado");
}

