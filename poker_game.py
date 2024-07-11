import random

# Define the suits and ranks of the cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Create the deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Deal hands to two players
player1_hand = [deck.pop() for _ in range(5)]
player2_hand = [deck.pop() for _ in range(5)]

# Function to evaluate the hand (simplified)
def evaluate_hand(hand):
    ranks_in_hand = [card[0] for card in hand]
    if len(set(ranks_in_hand)) == 2:
        return 'Four of a Kind'
    elif len(set(ranks_in_hand)) == 3:
        return 'Full House'
    elif len(set(ranks_in_hand)) == 4:
        return 'Three of a Kind'
    elif len(set(ranks_in_hand)) == 5:
        return 'Pair'
    else:
        return 'High Card'

# Evaluate both hands
player1_result = evaluate_hand(player1_hand)
player2_result = evaluate_hand(player2_hand)

# Determine the winner
def determine_winner(player1_result, player2_result):
    ranking = ['High Card', 'Pair', 'Three of a Kind', 'Full House', 'Four of a Kind']
    if ranking.index(player1_result) > ranking.index(player2_result):
        return 'Player 1 wins!'
    elif ranking.index(player1_result) < ranking.index(player2_result):
        return 'Player 2 wins!'
    else:
        return 'It\'s a tie!'

# Print the hands and the winner
print(f"Player 1's hand: {player1_hand} - {player1_result}")
print(f"Player 2's hand: {player2_hand} - {player2_result}")
print(determine_winner(player1_result, player2_result))
