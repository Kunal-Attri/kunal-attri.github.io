#include <iostream>
#include <math.h>

double get_float(string msg = "Number: ") {
    double f;
    cout << msg;
    cin >> f;
    return f;
}

using namespace std;

int main() {
    cout << "This code calculates distance between any two coordinates on earth. Provide following data.\n";
    while (true) {
        cout << "Input coordinates of two points...\n";
        double start_lat = (get_float("Starting latitude: ") * M_PI / 180);
        double start_lon = (get_float("Starting longitude: ") * M_PI / 180);
        double end_lat = (get_float("Ending latitude: ") * M_PI / 180);
        double end_lon = (get_float("Ending longitude: ") * M_PI / 180);

        double dist = 6371.01 * acos(sin(start_lat) * sin(end_lat) + cos(start_lat) * cos(end_lat) * cos(start_lon - end_lon));
        cout << "The distance is " << dist << " km.\n\n";
    }
}