import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    score = sum(ranks[card[0]] for card in hand)
    # Adjust for Aces
    aces = sum(1 for card in hand if card[0] == 'A')
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

def display_hand(hand, hide_first=False):
    if hide_first:
        return "[??] " + " ".join([f"[{r} of {s}]" for r, s in hand[1:]])
    return " ".join([f"[{r} of {s}]" for r, s in hand])

def player_turn(deck, player_hand):
    while True:
        print("\nYour hand:", display_hand(player_hand))
        print("Score:", calculate_score(player_hand))
        if calculate_score(player_hand) > 21:
            print("You busted!")
            return
        move = input("Do you want to [H]it or [S]tand? ").lower()
        if move == 'h':
            player_hand.append(deck.pop())
        elif move == 's':
            break
        else:
            print("Invalid choice. Enter H or S.")

def dealer_turn(deck, dealer_hand):
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

def determine_winner(player_hand, dealer_hand):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    print("\nFinal Hands:")
    print("Your hand:", display_hand(player_hand), "-", player_score)
    print("Dealer hand:", display_hand(dealer_hand), "-", dealer_score)

    if player_score > 21:
        return "You busted. Dealer wins!"
    elif dealer_score > 21:
        return "Dealer busted. You win!"
    elif player_score > dealer_score:
        return "You win!"
    elif player_score < dealer_score:
        return "Dealer wins!"
    else:
        return "It's a tie!"

def play_blackjack():
    print("=== Welcome to Blackjack ===")
    while True:
        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print("\nDealer's hand:", display_hand(dealer_hand, hide_first=True))
        player_turn(deck, player_hand)

        if calculate_score(player_hand) <= 21:
            dealer_turn(deck, dealer_hand)

        print(determine_winner(player_hand, dealer_hand))

        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_blackjack()
