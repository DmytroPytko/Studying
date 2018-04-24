#include "stdafx.h"
#include "conio.h"
#include "iostream"
#include "math.h"

using namespace std;


class Matrix
{

private:
 int **matrix;
 int size;
public:

 void ReadMatrixFromConsole();
 void OutputMatrixToConsole();
 void MathmeticActions();
 void InsertionSortOfColumns(); //by descending
};

void Matrix::ReadMatrixFromConsole() {

 cout << "Enter size of matrix>>";
 cin >> size;
 matrix = new int *[size];
 for (int i = 0; i < size; i++) 
	 matrix[i] = new int[size];
 cout << "Enter matrix>>\n";
 for (int i = 0; i < size; i++) {
  for (int j = 0; j < size; j++) {
   cin >> matrix[i][j];
  }
 }
}

void Matrix::OutputMatrixToConsole() {
 for (int i = 0; i < size; i++) {
  for (int j = 0; j < size; j++) {
   printf("%5d", matrix[i][j]);
  }
  cout << endl;
 }
}

void Matrix::InsertionSortOfColumns() //by descending
{
 int temp, previousItem; //temporary values
 for (int j = 0; j < size; j++) {
  for (int i = 1; i < size; i++)
  {
   temp = matrix[i][j]; //current element
   previousItem = i - 1; 
   while (previousItem >= 0 && matrix[previousItem][j] < temp)
   {
    matrix[previousItem + 1][j] = matrix[previousItem][j];
    matrix[previousItem][j] = temp;
    previousItem--;
   }
  }
 }
}

void Matrix::MathmeticActions() {

 int sum = 0;
 long product = 1;
 int j;
 for (j = 0; j < size - 1; j++) {
  sum = 0;
  for (int i = 0; i < size; i++) { 

   if ((i + j) < (size - 1)) {

    sum += matrix[i][j];
   }
  }
  cout << " Sum of the " << j + 1 << " column: " << sum << endl;
  product *= sum;
 }
 float geometricAverage = pow(product, (1. / j));

 cout << "Geometric average = " << geometricAverage << endl;

}


int main()
{
 Matrix A;
 A.ReadMatrixFromConsole();
 cout << "Matrix >>\n";
 A.OutputMatrixToConsole();

 A.InsertionSortOfColumns();
 cout << "Sorted matrix=>>" << endl;
 A.OutputMatrixToConsole();
 A.MathmeticActions();
 system("pause");
 
 return 0;
}