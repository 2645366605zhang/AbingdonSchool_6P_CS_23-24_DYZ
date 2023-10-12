import random

class Card: # A class to describe cards in a pack

    cardValue = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cardSuits = ["S", "H", "D", "C"] # Spades, Hearts, Diamonds, Clubs

    valueDict = {
        "A" : "Ace", 
        "2" : "Two", 
        "3" : "Three", 
        "4" : "Four", 
        "5" : "Five", 
        "6" : "Six", 
        "7" : "Seven", 
        "8" : "Eight", 
        "9" : "Nine", 
        "10" : "Ten", 
        "J" : "Jack", 
        "Q" : "Queen", 
        "K" : "King"
    }
    suitDict = {
        "S" : "Spades", 
        "H" : "Hearts", 
        "D" : "Diamonds", 
        "C" : "Clubs"
    }

    def __init__(self, cardID): # cardID: Type = int, range = 0-51(inclusive)
        self._cardID = cardID
        self._value = Card.cardValue[cardID % 13]
        self._suit = Card.cardSuits[cardID // 13]
        if not(cardID in range(0, 52)):
            print("Card ID out of range.")

    def getSuit(self): # return a string 'C', 'S', 'H', 'D'
        return (self._suit)

    def getValue(self): # return a string 'A'..'10', 'J', 'Q', 'K'
        return (self._value)

    def getShortName(self): # return card name eg '10D' '8C' 'AH'
        return (self._value + self._suit)

    def getLongName(self): # return card name eg 'Ten of Diamonds'
        return (f"{Card.valueDict[self._value]} of {Card.suitDict[self._suit]}")


class Deck: # A class to contain a pack of cards with methods for shuffling, adding or removing cards etc.

    def __init__(self):
        self._cardList = []
        for i in range(52):
            self._cardList.append(Card(i))

    def length(self): # returns the number of cards still in the deck
        return (len(self._cardList))

    def shuffleDeck(self): # shuffles the cards
        random.shuffle(self._cardList)

    def takeTopCard(self): # removes the top card from the deck and returns it (as a card object)
        removedCard = self._cardList[-1]
        self._cardList.pop(-1)
        return removedCard


card = Card(1)
print(card.getLongName())
deck = Deck()
deck.shuffleDeck()
for thisCardIndex in range(deck.length()):
    card = deck.takeTopCard()
    print(card.getLongName())