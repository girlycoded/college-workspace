#include <iostream>
#include <time.h>
#include <iomanip>
#include <optional>

using namespace std;

/**
    @file: main.cpp
    @author: juli tibbetts
    @brief: generate
    @date: 09/07/2026
    @return
*/

int tokens = 100;

string game_loop() {
    char choice;

    cout << "Tokens: " << tokens << endl;
    cout << "Press 'p' to pull: ";
    cin >> choice;
    cout << endl;

    if (choice == 'q' || choice == 'Q') return "";
    else if (choice != 'P' && choice != 'p') return "Invalid input!";
    if (tokens <= 0) return "You need at least one token to play!";

    int slot1 = rand() % 6 + 1;
    int slot2 = rand() % 6 + 1;
    int slot3 = rand() % 6 + 1;

    cout << setw(3) << slot1 << setw(3) << slot2 << setw(3) << slot3 << endl;
    if (slot1 == slot2 && slot1 == slot3) { // All three match
        tokens += 6;
        return "You win 6 tokens!";
    }
    else if (slot1 == slot2 || slot2 == slot3 || slot1 == slot3) { // Two match
        tokens += 2;
        return "You win 2 tokens!";
    } 
    // No match

    tokens -= 1;
    return "You lost your token!";
}

void init() {
    srand(time(0));
    cout << "Slot Machine" << endl;
}

int main() {
    init();
    while(true) {
        string response = game_loop();
        if (response.empty()) break;
        else cout << response << endl;
    }
    return 0;
}