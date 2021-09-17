#include <iostream>

int get_integer(string msg = "Number: ") {
    int i;
    cout << msg;
    cin >> i;
    return i;
}

using namespace std;

int main() {
    cout << "\nThis code finds out the no of diagonals in a regular polygon. Please enter the no of sides.\n\n";
    while (true) {
        int no_of_sides = get_integer("Sides: ");
        if (no_of_sides > 2) {
            int no_of_diagonals = no_of_sides * (no_of_sides - 3) / 2;
            cout << "No of diagonals = " << no_of_diagonals << endl << endl;
        }
        else {
            cout << "A polygon cannot be formed with no of sides less than 3\n\n";
        }
    }
}