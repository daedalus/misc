#include <stdio.h>
/*
Author Dario Clavijo 2015
*/

double _pow(double a, double b) {
    double c = 1;
    for (int i=0; i<b; i++)
        c *= a;
    return c;
}

double _fact(double x) {
    double ret = 1;
    for (int i=1; i<=x; i++) 
        ret *= i;
    return ret;
}

double _sin(double x) {
    double y = x;
    double s = -1;
    for (int i=3; i<=100; i+=2) {
        y+=s*(_pow(x,i)/_fact(i));
        s *= -1;
    }  
    return y;
}
double _cos(double x) {
    double y = 1;
    double s = -1;
    for (int i=2; i<=100; i+=2) {
        y+=s*(_pow(x,i)/_fact(i));
        s *= -1;
    }  
    return y;
}
double _tan(double x) {
     return (_sin(x)/_cos(x));  
}

int main()
{
	double value;
	value = _cos(1);
	printf("cos 1 %1.10f\n",value);
	value = _sin(1);
	printf("sin 1 %1.10f\n",value);
	value = _pow(2,2);
	printf("pow 2 2 %1.0f\n",value);
	value = _fact(10);
	printf("fact 10 %1.0f\n",value);
}
