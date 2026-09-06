-- name: juli
-- desc: random_card

-- CONSTS
local STARTING_PROMPT = "1. The next card will be higher\n2. The next card will be lower\n3. Quit\n"

-- vars
local last_card = math.random(1, 15)
local wins, losses = 0, 0

-- funcs
local function input(input_prompt)
    io.write(input_prompt)
    return io.read()
end

-- init
print("Card Drawn:", last_card)

while true do
    local selected_option = tonumber(input(STARTING_PROMPT .. "What option would you like to choose: "))
    if not selected_option or selected_option < 1 or selected_option > 3 then print("Invalid option!") goto continue end
    if selected_option == 3 then break end

    local guess_is_higher = selected_option == 1
    local random_card = math.random(1, 15)

    if random_card == last_card then print("The cards were the same (" .. tostring(random_card) .. ")! No win or lose.")
    elseif (guess_is_higher and random_card > last_card) or (not guess_is_higher and random_card < last_card) then
        print("You win! Card Drawn:", random_card)
        wins = wins + 1
    else
        print("You Lose! Card Drawn:", random_card)
        losses = losses + 1
    end

    last_card = random_card
    ::continue::
end
print("Wins:", wins, "\nLosses:", losses, "\nThankyou for playing!")