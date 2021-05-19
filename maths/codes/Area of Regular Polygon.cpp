#include <iostream>
#include <math.h>
using namespace std;

int main() {
    cout << "\nThis code calculates the area of a given regular polygon. \nPlease enter the no of sides and length of each side. \n \n";
    int no_of_sides;
    double side_length, area;
    while (true) {
        cout << "Sides: ";
        cin >> no_of_sides;
        if (no_of_sides > 2) {
            cout << "Length: ";
            cin >> side_length;
            if (side_length > 0) {
                area = no_of_sides * (side_length * side_length) / (4 * tan(M_PI / no_of_sides));
                cout << "Area = " << area << " square units\n\n";
            }
            else {
                cout << "Length of a side cannot be negative\n";
            }
        }
        else {
             cout << "Polygon with less than 3 sides cannot be formed\n \n";
        }
    }
}