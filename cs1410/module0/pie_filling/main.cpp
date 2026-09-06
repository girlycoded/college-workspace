#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;
/**
 * @author: Juli Tibbetts
 * @brief: Pie Calculator (calculates quarts and pints for a pie)
 * @date: 08/26/26
 * @return
**/

const double PI = 3.14;
const double QUART_INCHES = 69.3549;
const double PINT_INCHES = 34.7664;

int main() {
    double pan_diameter, pan_height;
    double volume, quarts, pints;

    // Input
    std::cout << "Enter the pie pan diameter: ";
    std::cin >> pan_diameter;
    
    std::cout << "Enter the pie pan height: ";
    std::cin >> pan_height;

    // Output
    volume = PI * pow(pan_diameter / 2 , 2) * pan_height;
    quarts = volume / QUART_INCHES;
    pints = volume / PINT_INCHES;

    std::cout << fixed << setprecision(1);
    std::cout << setw(10) << "Jar" << setw(10) << "Amount" << endl;
    std::cout << setw(10) << "Quarts" << setw(10) << quarts << endl;
    std::cout << setw(10) << "Pints" << setw(10) << pints << endl;

    return 0;
}