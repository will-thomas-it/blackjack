import random

# Define a Card class to represent a single card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Define a Deck class to represent a deck of cards
class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for rank in range(2, 11):
                self.cards.append(Card(suit, str(rank)))
            for rank in ["J", "Q", "K", "A"]:
                self.cards.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        return self.cards.pop(0)

# Define a Hand class to represent a player's hand
class Hand:
    def __init__(self):
        self.cards = []
        
    def add_card(self, card):
        self.cards.append(card)
        
    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.rank == "A":
                num_aces += 1
                value += 11
            elif card.rank in ["K", "Q", "J"]:
                value += 10
            else:
                value += int(card.rank)
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value
    
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
    
# Define a Blackjack class to represent the game
class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
    def deal_cards(self):
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        
    def player_turn(self):
        while self.player_hand.get_value() < 21:
            print(f"Your hand: {self.player_hand}")
            choice = input("Do you want to hit or stand? ")
            if choice.lower() == "hit":
                self.player_hand.add_card(self.deck.deal())
            else:
                break
                
    def dealer_turn(self):
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal())
            
    def determine_winner(self):
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()
        if player_value > 21:
            return "Dealer wins!"
        elif dealer_value > 21:
            return "Player wins!"
        elif player_value > dealer_value:
            return "Player wins!"
        elif dealer_value > player_value:
            return "Dealer wins!"
        else:
            return "Tie!"
        
    def play(self):
        self.deal_cards()
        print(f"Dealer's up card: {self.dealer_hand.cards[0]}")
        self.player_turn()
        if self.player_hand.get_value() <= 21:
            self.dealer_turn()
        print(f"Dealer's hand: {self.dealer_hand}")
        print(self.determine_winner())

game = Blackjack()
game.play()