#include <iostream>

using namespace std;
/*********************************************
  Example 1: For loops
**********************************************/
void Example1() {
    cout << "*****************************\n";
    cout << "*   Example 1:\n";
    cout << "*****************************\n\n";

    // 1.
    cout << "1.  Expected Values: 0 1 2 3 4 5" << endl;
    for (int i = 0; i < 6; i++) {
        cout << i << " ";
    }
    cout << endl << endl;
    // 2.
    cout << "2.  Expected Values: 5 4 3 2 1" << endl;
    for (int i = 0; i < 6; i++) {
        cout << i << " ";
    }
    cout << endl << endl;

    // 3.
    cout << "3.  Expected Values: 2 4 6 8 10" << endl;
    for (int i = 0; i < 6; i++) {
        cout << i << " ";
    }
    cout << endl << endl;
    // 4.
    cout << "4.  Expected Values: 9 6 3 0" << endl;
    for (int i = 0; i < 6; i++) {
        cout << i << " ";
    }
    cout << endl << endl;
}


/*********************************************
  Example 2: While loops
**********************************************/
void Example2() {
    cout << "*****************************\n";
    cout << "*   Example 2:\n";
    cout << "*****************************\n\n";
    int high = 0;
    int low = 0;
    int num;
    do {

        cout << "Enter a number: (-1 to quit)";
        cin >> num;
        if (num == -1) {
            break;
        }
        if (num < 1 || num > 100) {
            cout << "Invalid number:  " << num << endl;
        }
        if (num < low) {
            low = num;
        }
        if (num > high) {
            high = num;
        }
        cout << "High: " << high << endl;
        cout << "Low: " << low << endl;
    } while (num != -1);
}


/*********************************************
  Example 3: Math logic with loops
**********************************************/
void Example3() {
    cout << "\n*****************************\n";
    cout << "*   Example 3:\n";
    cout << "*****************************\n\n";
    // Variables
    int num, sum = 0;

    // Inputs
    cout << "Enter a number: ";
    cin >> num;

    // Equations
    for (int i = 1; i < num; i++) {
        if (num % i == 0) {
            sum += i;
        }
    }
    cout << "The sum of the factors of " << num << " is " << sum << endl;
    // Determine the number type
}

int main() {
    Example1();
    // Example2();
    // Example3();
}