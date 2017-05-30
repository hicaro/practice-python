"""
Function to print the n first numbers of the fibonacci series
"""
def fibonacci(number):
    a = 0
    b= 1
    for i in range(1, int(number)):
        print str(a);
        aux = a + b; 
        a = b;
        b = aux;

fibonacci(10)

