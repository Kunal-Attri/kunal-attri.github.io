#include <iostream>

using namespace std;

int main() {
    int t;
    cout << "Numbers of numbers: ";
    cin >> t;
    int x[t];
    cout << "Numbers: ";
    for (int i = 0; i < t; i++) {
        cin >> x[i];
    }
    
    // HCF Function
    // Smallest num
    int smaller = x[0];
    for (int i = 0; i < t; i++) {
        if (x[i] < smaller) {
            smaller = x[i];
        }
    }
    // finding hcf
    for (int i = smaller; i > 0; i--) {
        bool hcf = true;
        for (int j = 0; j < t; j++) {
            if (x[j] % i != 0) {
                hcf = false;
                break;
            }
        }
        if (hcf) {
            cout << "HCF is " << i << endl;
            break;
        }
    }
}