#include <stdio.h> // Include the header file for the input and output


//Multiplication operation
{
	int multiplication(int *p1,int *p2){
	int result;
	result=((*p1)*(*p2));
	return result;
}

// Addition funtion
int addition ( int* n1 , int* n2 ) // Receiving the address of the arguments
{
	int result = *n1 + *n2;   // Storing the value to the result variable
	return result;       // return the result
}

// function for subtracting two number
int subtraction(int* n1, int* n2) 
{
  int diff; // Declared a variable to store the difference the two number
  diff = *n1 - *n2; // performed subtraction and stored it the diff variable
  return diff; // returing the value of diff
}

//Main funtion
int main()
{
int n1; // Initialize the variable "n1" for input1 
int n2; // Initialize the variable "n2" for input2
int task;
int result;
printf ("Enter the values of n1 and n2 by leaving one spacebar: \n");
scanf ("%d %d",&n1,&n2); // Scan the inputs and store it in variable address of n1, n2
printf("Enter the operation need to perform\n");
printf("1: Addition , 2: Subtraction , 3: multiplication\n ");
scanf("%d",&task);
switch (task)
	{
		case 1: 
	    		result = addition(&n1,&n2); //Send the value of n1 and n2 as function addition
	    		printf("The result of operation : %d ",result);
	    		break;
		case 2:
		   	result = subtraction(&n1,&n2); //Send the value of n1 and n2 as function subtraction
		   	printf("The result of operation : %d \n",result);
			break;
		case 3: 
		    	result = multiplication(&n1,&n2); //Send the value of n1 and n2 as function multiply
		    	printf("The result of operation : %d ",result);
			break;
		default: 
			printf("Invalid task selected");
	}
	
	
}
