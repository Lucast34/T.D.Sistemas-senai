# include <stdio.h> // biblioteca de i/o
# include <math.h>

int main(void){
	float 
		nota1, 
		nota2, 
		resul; // notas
	
	printf("Digite as suas notas");
	
	scanf("%f%f"&nota1, &nota2);
	
	while(getchar() != '\n');
	
	resul = nota1 + nota2;
	
	system("PAUSE");
	
	return 0;
}

