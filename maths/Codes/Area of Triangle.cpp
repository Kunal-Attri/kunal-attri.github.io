#include <iostream>
#include <math.h>

using namespace std;

int main() {
    cout << "\nThis code is used to calculate the area of a triangle given it's sides.\nYou have to enter the sides of the triangle in any unit! Make sure all the sides are in same units.\n\nEg. Q. Side 1 = 120 cm; Side 2 = 1 m; Side 3 = 11000 mm\n    Ten enter the data only in one of the above units like:\n    Side 1 = 120 cm; Side 2 = 100 cm; Side 3 = 110 cm.\n\nNOTE:- DO NOT WRITE THE UNITS. ONLY WRITE THE NUMERICAL VALUE OF THE SIDE LENGTH.\n";
    float a, b, c, s, area;
    while (true) {
        cout << "First side: ";
        cin >> a;
        cout << "Second side: ";
        cin >> b;
        cout << "Third side: ";
        cin >> c;
        if (a + b < c or a + c < b or b + c < a) {
            cout << "Triangle with these given sides is not possible. Try making one yourself!\n";
        }
        else {
            s = (a + b + c) / 2;
            area = sqrt(s * (s - a) * (s - b) * (s - c));
            cout << "Area = " << area << " square units\n\n";
        }
    }
}