#include <iostream>

int get_integer(string msg = "Number: ") {
    int i;
    cout << msg;
    cin >> i;
    return i;
}

using namespace std;

int main() {
    int terms = get_integer("No of terms: ");
    int prev_first = 0, prev_second = 1;
    cout << prev_first << endl;
    cout << prev_second << endl;

    while (2 < terms) {
        int n = prev_second + prev_first;
        prev_first = prev_second;
        prev_second = n;
        cout << n << endl;
        terms -= 1;
    }
}