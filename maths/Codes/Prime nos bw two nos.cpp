#include <iostream>

int basic_prime[25] = {3, 5, 7, 11, 13, 15, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};

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

bool iseven(int num) {
    bool even = true;
    if (num % 2) {
        even = false;
    }
    return even;
}

bool isprime(int num) {
    bool prime = true;
    if (iseven(num) and num / 2 != 1) {
        prime = false;
    }
    if (isodd(num)) {
        for (int i = 0; i < 25; i++) {
            if (num % basic_prime[i] == 0 and num / basic_prime[i] != 1) {
                prime = false;
            }
        }
        if (prime) {
            for (int i = 101; i < (sqrt(num) + 1); i++) {
                if (num % i == 0) {
                    prime = false;
                    break;
                }
            }
        }
    }
    return prime;
}


using namespace std;

int main() {
    while (true) {
        int ini_no = get_integer("Initial no: ");
        int final_no = get_integer("Final no: ");

        int total = 0;
        cout << "Prime no.s in range from " << ini_no << " to " << final_no << " are: \n";
        for (int i = ini_no; i <= final_no; i++) {
            if (isprime(i) and i != 1) {
                cout << i << endl;
                total++;
            }
        }
        if (total == 0) {
            cout << "None\n";
        }
        else {
            cout << "Total = " << total << endl;
        }
        cout << endl;
    }
}