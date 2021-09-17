#include <iostream>
using namespace std;


int get_integer(string msg = "Number: ") {
    int i;
    cout << msg;
    cin >> i;
    return i;
}

bool isodd(int num) {
    bool odd = false;
    if (num % 2) {
        odd = true;
    }
    return odd;
}

int main() {
    while (true) {
        int num = get_integer("Number: ");
        int total = 0;
        cout << "Factors: " << endl;
        if (isodd(num)) {
            for (int i = 1; i < num + 1; i += 2) {
                if (num % i == 0) {
                    cout << i << endl;
                    total++;
                }
            }
        }
        else {
            for (int i = 1; i < num + 1; i++) {
                if (num % i == 0) {
                    cout << i << endl;
                    total++;
                }
            }
        }
        cout << "Total = " << total << endl << endl;
    }
}