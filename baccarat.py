import random

def draw_card():
    """Simulate drawing a card. Returns the card's value."""
    card = random.randint(1, 13)
    return min(card, 10)  # Face cards are worth 10, Ace is 1

def calculate_hand_value(hand):
    """Calculate the value of a Baccarat hand."""
    return sum(hand) % 10

def baccarat_round():
    """Simulate a round of Baccarat."""
    # Initial hands
    player_hand = [draw_card(), draw_card()]
    banker_hand = [draw_card(), draw_card()]

    player_total = calculate_hand_value(player_hand)
    banker_total = calculate_hand_value(banker_hand)

    # Player rules
    if player_total <= 5:
        player_hand.append(draw_card())
        player_total = calculate_hand_value(player_hand)

    # Banker rules
    if banker_total <= 5:
        # Banker draws based on Player's third card (if any)
        if len(player_hand) == 3:
            third_card = player_hand[2]
            if banker_total <= 2 or (banker_total == 3 and third_card != 8) or \
               (banker_total == 4 and third_card in range(2, 8)) or \
               (banker_total == 5 and third_card in range(4, 8)):
                banker_hand.append(draw_card())
        else:
            banker_hand.append(draw_card())
        banker_total = calculate_hand_value(banker_hand)

    # Determine the winner
    if player_total > banker_total:
        return "Player", player_hand, banker_hand
    elif banker_total > player_total:
        return "Banker", player_hand, banker_hand
    else:
        return "Tie", player_hand, banker_hand

def play_baccarat():
    """Interactive Baccarat game where the player bets on the outcome."""
    balance = 1000  # Starting balance
    print("Welcome to Baccarat! Starting balance: $1000")

    while True:
        print(f"\nCurrent balance: PHP{balance}")
        bet = 0

        # Get the player's bet
        while bet <= 0 or bet > balance:
            try:
                bet = int(input("Enter your bet amount: "))
                if bet <= 0 or bet > balance:
                    print("Invalid bet amount. Make sure it is positive and within your balance.")
            except ValueError:
                print("Please enter a valid number.")

        # Get the player's choice
        choice = ""
        while choice not in ["Player", "Banker", "Tie"]:
            choice = input("Bet on 'Player', 'Banker', or 'Tie': ").capitalize()
            if choice not in ["Player", "Banker", "Tie"]:
                print("Invalid choice. Please choose 'Player', 'Banker', or 'Tie'.")

        # Play a round
        winner, player_hand, banker_hand = baccarat_round()
        player_total = calculate_hand_value(player_hand)
        banker_total = calculate_hand_value(banker_hand)

        print(f"\nPlayer hand: {player_hand} (Total: {player_total})")
        print(f"Banker hand: {banker_hand} (Total: {banker_total})")
        print(f"Winner: {winner}")

        # Update balance based on the outcome
        if choice == winner:
            if winner == "Tie":
                balance += bet * 8  # Tie pays 8:1
            else:
                balance += bet  # Win pays 1:1
            print(f"You won! New balance: PHP{balance}")
        elif winner != "Tie":
            balance -= bet
            print(f"You lost. New balance: PHP{balance}")

        # Check if the player wants to continue
        if balance <= 0:
            print("You are out of money. Game over!")
            break

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing Baccarat! Goodbye!")
            break

if __name__ == "__main__":
    play_baccarat()