#include <stdio.h>
#include <stdlib.h>

//fun��o
int maiormenor(float num1, float num2, float num3);


int main(void){
	float 
		n1,
		n2,
		n3;
	
	printf("Digite a primeira nota: ");
	
	scanf("%f",&n1);
	
	printf("\nDigite a primeira nota: ");
	
	scanf("%f", &n2);
	
	printf("\nDigite a primeira nota: ");
	
	scanf("%f",&n3);
	
	maiormenor(n1 ,n2 ,n3);	
	
	system("Pause");

	
	return 0;
}


int maiormenor(float num1, float num2, float num3){
	int J = 0;
	
	J = (num1 >= num2 ? printf("\nO numero %.2f", num1, "� maior"):(num2 >= num3 ? printf("\nO numero %.2f", num2, "� maior"): printf("\nO numero %.2f", num3, "� maior")));
	return J;
	
	/*
	if(n1 > n2){
		printf("FOdase");
	} 
	elseif(n2>n3){
		printf("lol");
	}
	else{
		printf("lmao");
	}
	*/
}
