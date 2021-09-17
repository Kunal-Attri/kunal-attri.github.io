#include <iostream>
#include <math.h>

using namespace std;

int get_integer(string msg = "Number: ") {
    int i;
    cout << msg;
    cin >> i;
    return i;
}

int factorial(int num) {
    int f = 1;
    for (int i = 1; i <= num; i++) {
        f *= i;
    }
    return f;
}

int main() {
    while (true) {
        int fact = get_integer("Factorial of: ");
        fact = factorial(fact);
        cout << "Factorial: " << fact << endl << endl;
    }
}