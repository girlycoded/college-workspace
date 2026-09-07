#include <iomanip>
#include <iostream>
#include <time.h>
using namespace std;

/*********************************************
 Click the Fork button to make a copy of this code.  Then answer the questions
in the worksheet and make the changes to the code here.
**********************************************/

void Example1() {
  srand(time(0));
  int x = 5, y = 5;
  cout << "*****************************\n";
  cout << "*   Example 1:\n";
  cout << "*****************************\n\n";

  cout << "1. " << x + 2 * 5 + 1 << endl;

  cout << "2. " << (x + 2) * 5 + 1 << endl;

  cout << "3. "
	   << "x: " << x++ << " "
	   << " y: " << ++y << endl;
  cout << "x: " << x << " "
	   << " y: " << y << endl;

  cout << "4. " << setprecision(3) << 1.23456 << endl;

  cout << "5. " << fixed << setprecision(3) << 1.23456 << endl;

  cout << "6. \n";
  cout << setw(4) << 12 << setw(4) << 12 << endl;
  cout << setw(4) << 123 << setw(4) << 123 << endl;

  cout << "7  \n";
  cout << "Type"
	   << "Equation"
	   << "Result" << endl;
  cout << "Int"
	   << "11 / 4" << 11 / 4 << endl;
  cout << "Mod"
	   << "11 % 4" << 11 % 4 << endl;
  cout << "Regular"
	   << "11.0 / 4" << 11.0 / 4 << endl;
}

void Example2() {
  cout << "\n*****************************\n";
  cout << "*   Example 2:\n";
  cout << "*****************************\n\n";

  // Declare Variables
  int fah, cel;
  char unit;
  cout << "Is your temperature currently in Fahrenheit (f) or Celsius (c): ";
  cin >> unit;

  // Determine the unit of measurment
  if (unit == 'f' || unit == 'F') {
	// Get the Input
	cout << "Enter Fahrenheit: ";
	cin >> fah;

	// Do the Math
	cel = 5 / 9 * (fah - 32);

	// Display the output
	cout << "Celsius: " << cel << endl;
  } else {
	cout << "Enter Celcius: ";
	cin >> cel;

	fah = (9.0 / 5) * cel + 32;
	cout << "Farenheit: " << fah << endl;
  }
}



int main() {
	int abc = 0;
	cout << ++abc;
	cout << abc;
	// Example1();
	// Example2();

}