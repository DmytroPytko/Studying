// lab4.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include "conio.h"
#include "iostream"
#include "math.h"

using namespace std;


class Matrix
{

private:
	int **array;
	int size;
public:

	void InputMatrix();
	void OutputMatrix();
	void MathmeticActions();
	void InsertionSort();
};

void Matrix::InputMatrix() {

	cout << "Enter size of matrix>>";
	cin >> size;
	array = new int *[size];
	for (int i = 0; i < size; i++) array[i] = new int[size];
	cout << "Enter matrix>>\n";
	for (int i = 0; i < size; i++) {

		for (int j = 0; j < size; j++) {
			cin >> array[i][j];

		}
	}

}

void Matrix::OutputMatrix() {
	//cout << "Matrix ==>n";
	for (int i = 0; i < size; i++) {

		for (int j = 0; j < size; j++) {
			printf("%5d", array[i][j]);

		}
		cout << endl;
	}

}

void Matrix::InsertionSort()
{
	int temp,
		item;
	for (int j = 0; j < size; j++) {
		for (int i = 1; i < size; i++)
		{
			temp = array[i][j];
			item = i - 1;
			while (item >= 0 && array[item][j] < temp)
			{
				array[item + 1][j] = array[item][j];
				array[item][j] = temp;
				item--;
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
		for (int i = 0; i < size; i++) { // закінчуємо передостаннім рядком, бо використовуємо числа над діагоналлю

			if ((i + j) < (size - 1)) {

				sum += array[i][j];
			}
		}
		cout << " Sum of the " << j + 1 << " column: " << sum << endl;
		product *= sum;//Знаходимо суму для підрахунку середнього геометричного значення
					   //	cout << "p= " << product << endl;
	}
	float geometricAverage = pow(product, (1. / j));

	cout << "Geometric average = " << geometricAverage << endl;

}


int main()
{
	Matrix A;
	A.InputMatrix();
	cout << "Matrix >>\n";
	A.OutputMatrix();

	A.InsertionSort();
	cout << "Sorted matrix=>>" << endl;
	A.OutputMatrix();
	A.MathmeticActions();
	system("pause");
	
	return 0;
}

