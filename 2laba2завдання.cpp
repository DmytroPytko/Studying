// 2laba2завдання.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"
#include "stdlib.h"


int main()
{
	double a = 1;
	double b = 1.5;
	double h = 0.05;
	double d = 0.00001;

	printf("enter a: ");
	scanf_s("%lf", &a);
	printf("enter b: ");
	scanf_s("%lf", &b);
	printf("enter h: ");
	scanf_s("%lf", &h);
	printf("enter d: ");
	scanf_s("%lf", &d);

	while (a < b + h / 2) {
		double sum = 0;
		double element = 0;
		int n = 1;
		do {
			element = pow(-1, n + 1) * pow(a - 1, n) / n;
			sum = sum + element;
			n++;
		} while (element > d);
		printf("%.2f  -->  %.5f\n", a, sum);
		a = a + h;
	}

	system("pause");
	return 0;
}

