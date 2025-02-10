#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(void) {
	float 
		peso,
		altura,
		imc;
	
	printf("Programa de imc\n");

	puts("\nOBS: coloque . em vez da ,\n");
	printf("\nDigite o seu peso:");
	
	scanf("%f",&peso);
	
	printf("\nDigite a sua altura:");
	scanf("%f", &altura);
	
	imc = peso/pow(altura, 2);
	
	if (imc<= 30){
		printf("\nPeso normal\n");
	}else
		printf("\nObeso\n");
	
	
	system("PAUSE");
	
	return 0;
}
