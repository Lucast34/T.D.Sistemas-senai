#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(void) {
	int n1,
		n2,
		n3,
		aux;
	
	// pegando variavel
	printf("Informe 3 numeros:");
	scanf("%d %d %d", &n1, &n2, &n3);
	fflush(stdin);
	
	if (n1 < n3){
		/*Algoritmo de troca n1 = n3 e n3 = n1 anterior*/
		aux = n3;// aux está sendo atribuido com n3
		n3 = n1; // n3 recebe o valor de n1
		n1 = aux; // e o n1 recebo o valor de n3
	}
	
	if (n2 < n3){
		aux = n3;
		n3 = n2;
		n2 = aux;
	}
	
	printf("Numeros ordenados: %d %d %d\n", n1, n2, n3);
	system("PAUSE");
	
	return 0;
}
