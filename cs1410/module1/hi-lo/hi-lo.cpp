// name: juli
// desc: random_card

#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

using std::string;

// CONSTS
const string STARTING_PROMPT = "1. The next card will be higher\n2. The next card will be lower\n3. Quit\n";

// // vars
int last_card;
int wins = 0, losses = 0;

string get_user_input(const string& input_prompt) {
    string user_input;

    std::cout << input_prompt;
    std::cin >> user_input;
    return user_input;
}

bool game_loop() {
    string selected_option_input = get_user_input(STARTING_PROMPT + "What option would you like to choose: ");
    int selected_option = std::atoi(selected_option_input.c_str());
    if ((!selected_option) || selected_option < 1 || selected_option > 3) {
        std::cout <<  "Invalid option!" << std::endl;
        return false;
    }
    if (selected_option == 3) return true;

    bool guess_is_higher = selected_option == 1;
    int random_card = rand() % 15 + 1;

    if (random_card == last_card) {
        std::cout << "The cards were the same (" << random_card << ")! No win or lose." << std::endl;
    }
    else if ((guess_is_higher && random_card > last_card) || (!guess_is_higher && random_card < last_card)) {
        std::cout << "You win! Card Drawn: " << random_card << std::endl;
        wins += 1;
    }  
    else {
        std::cout << "You Lose! Card Drawn:" << random_card << std::endl;
        losses += 1;
    }
    last_card = random_card;
    return false;
}

int main() {
    std::srand(std::time(nullptr));
    last_card = rand() % 15 + 1;
    std::cout << "Card Drawn: " << last_card << std::endl;

    while (true) if (game_loop()) break;
    std::cout << "Wins:" << wins << "\nLosses:" << losses << "\nThankyou for playing!";
    return 0;
}