#include <iostream>
#include <math.h>

int get_integer(string msg = "Number: ") {
    int i;
    cout << msg;
    cin >> i;
    return i;
}

double get_float(string msg = "Number: ") {
    double f;
    cout << msg;
    cin >> f;
    return f;
}

using namespace std;

int main() {
    while (true) {
        int n = get_integer("No of sides: ");
        double a = get_float("Each side length: ");
        float diagonals[n - 2];
        diagonals[0] = a;
        double d = n - 3;
        int temp = floor(d / 2);
        double value;

        for (int i = 0; i < d; i++) {
            if ((i + 1) <= ceil(d / 2)) {
                value = diagonals[i] * cos(M_PI / n) + (diagonals[0] * cos((i + 1) * M_PI / n));
            }
            else {
                value = diagonals[temp];
                temp -= 1;
            }
            diagonals[i+1] = value;
        }

        for (int i  = 1; i < n - 2; i++) {
            cout << "Diagonal " << i << " = " << diagonals[i] << endl;
        }
        cout << endl;
    }
}