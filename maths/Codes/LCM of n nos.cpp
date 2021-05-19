#include <iostream>

int basic_prime[25] = {3, 5, 7, 11, 13, 15, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};

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
    int t;
    cout << "Numbers of numbers: ";
    cin >> t;
    int x[t];
    cout << "Numbers: ";
    for (int i = 0; i < t; i++) {
        cin >> x[i];
    }
    

    // LCM function
    int larger = x[0];
    for (int i = 0; i < t; i++) {
        if (x[i] > larger) {
            larger = x[i];
        }
    }

    int divisors[larger];
    int divQuan[larger];
    for (int i = 0; i < larger; i++) {
        divisors[i] = 0;
        divQuan[i] = 0;
    }
    for (int a = 0; a < t; a++) {
        int i = 2;
        while (x[a] > 1) {
            int quantity = 0;
            while (x[a] % i == 0) {
                if (isprime(i)) {
                    divisors[i] = i;
                    quantity++;
                    x[a] /= i;
                }
            }
            if (quantity > divQuan[i]) {
                divQuan[i] = quantity;
            }
            i++;
        }
    }
    int lcm = 1;
    for (int i = 0; i < larger; i++) {
        lcm *= pow(divisors[i], divQuan[i]);
    }

    cout << "LCM is " << lcm;
}