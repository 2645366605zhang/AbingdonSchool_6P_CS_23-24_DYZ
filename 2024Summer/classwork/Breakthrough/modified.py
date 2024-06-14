# Skeleton Program code for the AQA A Level Paper 1 Summer 2022 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.9 programming environment

import random
import os

def Main():
    ThisGame = Breakthrough()
    ThisGame.PlayGame()

class Breakthrough():
    def __init__(self):
        self.__Deck = CardCollection("DECK")
        self.__Hand = CardCollection("HAND")
        self.__Sequence = CardCollection("SEQUENCE")
        self.__Discard = CardCollection("DISCARD")
        self.__Score = 0
        self.__Locks = []
        self.__GameOver = False
        self.__CurrentLock = Lock()
        self.__LockSolved = False
        self.__LoadLocks()
        self.__notification = "None"
        self.__MulliganUsed = False
        self.__QuitGame = False
    
    def clearNotification(self):
        self.__notification = "None"

    def PlayGame(self):
        if len(self.__Locks) > 0:
            self.__SetupGame()
            while not self.__GameOver:
                self.__LockSolved = False
                while not self.__LockSolved and not self.__GameOver:
                    os.system("cls")
                    print(f"System Message: {self.__notification}\n")
                    self.clearNotification()
                    print("Current score:", self.__Score)
                    print(self.__CurrentLock.GetLockDetails())
                    print(self.__Sequence.GetCardDisplay())
                    print(f"{self.__Deck.GetNumberOfCards()} cards left in the deck.\n")
                    print(self.__Hand.GetCardDisplay())
                    MenuChoice = self.__GetChoice()
                    if MenuChoice == "D":
                        print(self.__Discard.GetCardDisplay())
                        temp = input("Press Enter to go back to the menu.\n")
                    elif MenuChoice == "U":
                        CardChoice  = self.__GetCardChoice()
                        DiscardOrPlay = self.__GetDiscardOrPlayChoice()
                        if DiscardOrPlay == "D":
                            self.__MoveCard(self.__Hand, self.__Discard, self.__Hand.GetCardNumberAt(CardChoice - 1))
                            self.__GetCardFromDeck(CardChoice)
                        elif DiscardOrPlay == "P":
                            self.__PlayCardToSequence(CardChoice)
                    elif MenuChoice == "P" and not(self.__CurrentLock.GetPeekUsed()):
                        self.__CurrentLock.usePeek()
                        displayedCardNumber = 0
                        print(f"\nThe next three cards in the deck are:")
                        while self.__Deck.GetNumberOfCards() > 0 and displayedCardNumber < 3:
                            print(f"\n{self.__Deck.GetCardDescriptionAt(displayedCardNumber)}")
                            displayedCardNumber += 1
                        temp = input("\nPress Enter to go back to the menu.\n")
                    elif MenuChoice == "M" and not(self.__MulliganUsed):
                        self.__MulliganUsed = True
                        self.__Mulligan()
                    elif MenuChoice == "S":
                        saveDirectory = input("Please enter the name you want to save as:> ")
                        self.__SaveGame(saveDirectory)
                        self.__notification = f"Game saved at {f"save/{saveDirectory}.sav"}!"
                    elif MenuChoice == "Q":
                        quitConfim = input("Are you sure you want to quit? y/n:> ").upper()
                        if quitConfim == "Y":
                            self.__Score += self.__Deck.GetNumberOfCards()
                            self.__QuitGame = True
                            self.__GameOver = True
                        else:
                            self.__notification = "Phew! 'twas a mistype innit?"
                    if self.__CurrentLock.GetLockSolved():
                        self.__LockSolved = True
                        self.__ProcessLockSolved()
                self.__GameOver = self.__CheckIfPlayerHasLost()
        else:
            print("No locks in file.")

    def __ProcessLockSolved(self):
        self.__Score += 10
        print("Lock has been solved. Your score is now:", self.__Score)
        while self.__Discard.GetNumberOfCards() > 0:
            self.__MoveCard(self.__Discard, self.__Deck, self.__Discard.GetCardNumberAt(0))
        self.__TryAddGeniusCardToDeck()
        self.__Deck.Shuffle()
        self.__CurrentLock = self.__GetRandomLock()

    def __CheckIfPlayerHasLost(self):
        if self.__Deck.GetNumberOfCards() == 0:
            print("You have run out of cards in your deck. Your final score is:", self.__Score)
            return True
        elif self.__QuitGame:
            print("You have chosen to quit the game. Your final score is:", self.__Score)
            return True
        else:
            return False
    
    def __SetupGame(self):
        Choice = input("Enter L to load a game from a file, anything else to play a new game:> ").upper()
        if Choice == "L":
            saveName = input("Enter the name of the save file you want to load(without filename extension):> ")
            if not self.__LoadGame(f"save/{saveName}.sav"):
                self.__GameOver = True
        else:
            self.__CreateStandardDeck()
            self.__Deck.Shuffle()
            for Count in range(5):
                self.__MoveCard(self.__Deck, self.__Hand, self.__Deck.GetCardNumberAt(0))
            self.__AddDifficultyCardsToDeck()
            self.__TryAddGeniusCardToDeck()
            self.__Deck.Shuffle()
            self.__CurrentLock = self.__GetRandomLock()
    
    def __PlayCardToSequence(self, CardChoice):
        self.__notification = f'You have just played card "{self.__Hand.GetCardDescriptionAt(CardChoice - 1)}".'
        if self.__Sequence.GetNumberOfCards() > 0:
            if self.__Hand.GetCardDescriptionAt(CardChoice - 1)[0] != self.__Sequence.GetCardDescriptionAt(self.__Sequence.GetNumberOfCards() - 1)[0]:
                self.__Score += self.__MoveCard(self.__Hand, self.__Sequence, self.__Hand.GetCardNumberAt(CardChoice - 1))
                self.__GetCardFromDeck(CardChoice)
            else:
                self.__notification = "You cannot play two cards with the same type in a row."
        else:
            self.__Score += self.__MoveCard(self.__Hand, self.__Sequence, self.__Hand.GetCardNumberAt(CardChoice - 1))
            self.__GetCardFromDeck(CardChoice)
        if self.__CheckIfLockChallengeMet():
            print()
            print("A challenge on the lock has been met.")
            print()
            self.__Score += 5

    def __CheckIfLockChallengeMet(self):
        SequenceAsString = ""
        for Count in range(self.__Sequence.GetNumberOfCards() - 1, max(0, self.__Sequence.GetNumberOfCards() - 3) -1, -1):
            if len(SequenceAsString) > 0:
                SequenceAsString = ", " + SequenceAsString
            SequenceAsString = self.__Sequence.GetCardDescriptionAt(Count) + SequenceAsString
            if self.__CurrentLock.CheckIfConditionMet(SequenceAsString):
                return True
        return False
    
    def __SetupCardCollectionFromGameFile(self, LineFromFile, CardCol):
        if len(LineFromFile) > 0:
            SplitLine = LineFromFile.split(",")
            for Item in SplitLine:
                if len(Item) == 5:
                    CardNumber = int(Item[4])
                else:
                    CardNumber = int(Item[4:6])
                if Item[0: 3] == "Dif":
                    CurrentCard = DifficultyCard(CardNumber)
                    CardCol.AddCard(CurrentCard)
                else:
                    CurrentCard = ToolCard(Item[0], Item[2], CardNumber)
                    CardCol.AddCard(CurrentCard)
    
    def __SetupLock(self, Line1, Line2):
        SplitLine = Line1.split(";")
        for Item in SplitLine:
            Conditions = Item.split(",")
            self.__CurrentLock.AddChallenge(Conditions)
        SplitLine = Line2.split(";")
        for Count in range(0, len(SplitLine)):
            if SplitLine[Count] == "Y":
                self.__CurrentLock.SetChallengeMet(Count, True)
    
    def __LoadGame(self, FileName: str) -> bool:
        try:
            with open(FileName) as f:          
                LineFromFile = f.readline().rstrip() # Line 1
                self.__Score = int(LineFromFile)
                LineFromFile = f.readline().rstrip() # Line 2
                LineFromFile2 = f.readline().rstrip() # Line 3
                self.__SetupLock(LineFromFile, LineFromFile2)
                LineFromFile = f.readline().rstrip() # Line 4
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Hand)
                LineFromFile = f.readline().rstrip() # Line 5
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Sequence)
                LineFromFile = f.readline().rstrip() # Line 6
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Discard)
                LineFromFile = f.readline().rstrip() # Line 7
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Deck)
                return True
        except:
            print("File not loaded")
            return False

    def __LoadLocks(self):
        FileName = "locks.txt"
        self.__Locks = []
        try:
            with open(FileName) as f: 
                LineFromFile = f.readline().rstrip()
                while LineFromFile != "":
                    Challenges = LineFromFile.split(";")
                    LockFromFile = Lock()
                    for C in Challenges:
                        Conditions = C.split(",")
                        LockFromFile.AddChallenge(Conditions)
                    self.__Locks.append(LockFromFile)
                    LineFromFile = f.readline().rstrip()
        except:
            print("File not loaded")
        
    def __GetRandomLock(self):
        return self.__Locks[random.randint(0, len(self.__Locks) - 1)]

    def __GetCardFromDeck(self, CardChoice):
        if self.__Deck.GetNumberOfCards() > 0:
            if self.__Deck.GetCardDescriptionAt(0) == "Dif":
                CurrentCard = self.__Deck.RemoveCard(self.__Deck.GetCardNumberAt(0))
                print("\nDifficulty encountered!")
                print(self.__Hand.GetCardDisplay())
                print("To deal with this you need to either lose a key or discard all the cards in your hand", end='')
                print(self.__Deck.DisplayStats())
                Choice = input("(enter 1-5 to specify position of key) or (D)iscard five cards from the deck:> ")
                self.__Discard.AddCard(CurrentCard)
                CurrentCard.Process(self.__Deck, self.__Discard, self.__Hand, self.__Sequence, self.__CurrentLock, Choice, CardChoice)
            elif self.__Deck.GetCardDescriptionAt(0) == "Gen":
                CurrentCard = self.__Deck.RemoveCard(self.__Deck.GetCardNumberAt(0))
                print("\nGenius encountered!\nYou can choose to either solve a challenge immediatly or discard this genius card!")
                validChoice = False
                while not(validChoice):
                    choice = input("(enter the ID of the challenge you wish to solve) or (D)iscard the genius card:> ").strip().upper()
                    if choice == "D":
                        validChoice = True
                        self.__Discard.AddCard(CurrentCard)
                    elif choice in "".join(range(1, self.__CurrentLock.GetNumberOfChallenges() + 1)):
                        validChoice = True
                        self.__CurrentLock.SetChallengeMet(int(choice) - 1, True)
        while self.__Hand.GetNumberOfCards() < 5 and self.__Deck.GetNumberOfCards() > 0:
            if self.__Deck.GetCardDescriptionAt(0) == "Dif":
                self.__MoveCard(self.__Deck, self.__Discard, self.__Deck.GetCardNumberAt(0))
                self.__notification = "A difficulty card was discarded from the deck when refilling the hand."
            elif self.__Deck.GetCardDescriptionAt(0) == "Gen":
                self.__MoveCard(self.__Deck, self.__Discard, self.__Deck.GetCardNumberAt(0))
                self.__notification = "A genius card was discarded from the deck when refilling the hand."
            else:
                self.__MoveCard(self.__Deck, self.__Hand, self.__Deck.GetCardNumberAt(0))
        if self.__Deck.GetNumberOfCards() == 0 and self.__Hand.GetNumberOfCards() < 5:
            self.__GameOver = True

    def __GetCardChoice(self):
        Choice = None
        while Choice is None:
            try: 
                Choice = int(input("Enter a number between 1 and 5 to specify card to use:> "))
            except:
                pass
        return Choice

    def __GetDiscardOrPlayChoice(self):
        Choice = input("(D)iscard or (P)lay?:> ").upper()
        return Choice

    def __GetChoice(self):
        print()
        prompt = "(D)iscard inspect, (U)se card"
        if not(self.__CurrentLock.GetPeekUsed()):
            prompt += ", (P)eek"
        if not(self.__MulliganUsed):
            prompt += ", (M)ulligan"
        Choice = input(f"{prompt}, (S)ave, (Q)uit:> ").upper()
        return Choice
    
    def __GetDeck(self):
        return self.__Deck

    def __GetHand(self):
        return self.__Hand
    
    def __GetSequence(self):
        return self.__Sequence
    
    def __GetDiscard(self):
        return self.__Discard

    def __AddDifficultyCardsToDeck(self):
        for Count in range(5):
            self.__Deck.AddCard(DifficultyCard())

    def __CreateStandardDeck(self):
        for Count in range(5):
            NewCard = ToolCard("P", "a")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("P", "b")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("P", "c")
            self.__Deck.AddCard(NewCard)
        for Count in range(3):
            NewCard = ToolCard("F", "a")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("F", "b")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("F", "c")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("K", "a")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("K", "b")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("K", "c")
            self.__Deck.AddCard(NewCard)
    
    def __MoveCard(self, FromCollection, ToCollection, CardNumber):
        Score  = 0
        if FromCollection.GetName() == "HAND" and ToCollection.GetName() == "SEQUENCE":
            CardToMove = FromCollection.RemoveCard(CardNumber)
            if CardToMove is not None:
                ToCollection.AddCard(CardToMove)
                Score = CardToMove.GetScore()
        else:
            CardToMove = FromCollection.RemoveCard(CardNumber)
            if CardToMove is not None:
                ToCollection.AddCard(CardToMove)
        return Score
    
    def __Mulligan(self) -> None:
        for index in range(self.__GetHand().GetNumberOfCards()):
            self.__MoveCard(self.__GetHand(), self.__GetDeck(), self.__GetHand().GetCardNumberAt(0))
        for index in range(self.__GetSequence().GetNumberOfCards()):
            self.__MoveCard(self.__GetSequence(), self.__GetDeck(), self.__GetSequence().GetCardNumberAt(0))
        for index in range(self.__GetDiscard().GetNumberOfCards()):
            self.__MoveCard(self.__GetDiscard(), self.__GetDeck(), self.__GetDiscard().GetCardNumberAt(0))
        self.__GetDeck().Shuffle()
        for index in range(5): # Can be modified to use a variable for range() for different number of hand cards allowed
            while self.__GetDeck().GetCardDescriptionAt(0) == "Dif":
                self.__MoveCard(self.__GetDeck(), self.__GetDiscard(), self.__GetDeck().GetCardNumberAt(0))
            self.__MoveCard(self.__GetDeck(), self.__GetHand(), self.__GetDeck().GetCardNumberAt(0))
        self.__notification = "You have used Mulligan!"

    def __SaveGame(self, saveDirectory: str) -> None:
        saveDataList = [str(self.__Score), "\n", self.__CurrentLock.GetChallengeString(), self.__GetHand().GetCardString(), self.__GetSequence().GetCardString(), self.__GetDiscard().GetCardString(), self.__GetDeck().GetCardString()]
        with open(f"save/{saveDirectory}.sav", "w") as saveFile:
            saveFile.writelines(saveDataList)

    def __TryAddGeniusCardToDeck(self):
        if random.randint(0, 3) == 0:
            self.__Deck.AddCard(GeniusCard())

    def TestS(self):
        self.__SetupGame()
        print(self.__CurrentLock.GetChallengeString())
        print(self.__Hand.GetCardString())
        self.__SaveGame("testtest")

    def TestL(self):
        self.__SetupGame()
        print(self.__CurrentLock.GetChallengeString())
        print(self.__Hand.GetCardString())

class Challenge():
    def __init__(self):
        self._Met = False
        self._Condition = []
    
    def GetMet(self): 
        return self._Met
    
    def GetMetString(self) -> str:
        if self.GetMet():
            return "Y"
        else:
            return "N"

    def GetCondition(self):
        return self._Condition

    def SetMet(self, NewValue):
        self._Met = NewValue

    def SetCondition(self, NewCondition):
        self._Condition = NewCondition

class Lock():
    def __init__(self):
        self._Challenges = []
        self.__peekUsed = False
        
    def AddChallenge(self, Condition):
        C = Challenge()
        C.SetCondition(Condition)
        self._Challenges.append(C)

    def __ConvertConditionToString(self, C):
        ConditionAsString = ""
        for Pos in range(0, len(C) - 1):
            ConditionAsString += C[Pos] + ", "
        ConditionAsString += C[len(C) - 1]
        return ConditionAsString

    def usePeek(self) -> None:
        self.__peekUsed = True

    def GetLockDetails(self):
        LockDetails = "\n" + "CURRENT LOCK" + "\n" + "------------" + "\n"
        for C in self._Challenges:
            if C.GetMet():
                LockDetails += "Challenge met: "
            else:
                LockDetails += "Not met:       "
            LockDetails += self.__ConvertConditionToString(C.GetCondition()) + "\n"
        LockDetails += "\n"
        return LockDetails

    def GetLockSolved(self):
        for C in self._Challenges:
            if not C.GetMet():
                return False
        return True
    
    def GetPeekUsed(self):
        return self.__peekUsed
    
    def CheckIfConditionMet(self, Sequence):
        for C in self._Challenges:
            if not C.GetMet() and Sequence == self.__ConvertConditionToString(C.GetCondition()):
                C.SetMet(True)
                return True
        return False

    def SetChallengeMet(self, Pos, Value):
        self._Challenges[Pos].SetMet(Value)
    
    def GetChallengeMet(self, Pos): 
        return self._Challenges[Pos].GetMet()
    
    def GetNumberOfChallenges(self): 
        return len(self._Challenges)
    
    def GetChallengeString(self):
        challengeDescList = []
        challengeStatList = []
        for challenge in self._Challenges: challengeDescList.append(",".join(challenge.GetCondition()))
        for challenge in self._Challenges: challengeStatList.append(challenge.GetMetString())
        return f"{";".join(challengeDescList)}\n{";".join(challengeStatList)}\n"

class Card():
    _NextCardNumber = 0
    
    def __init__(self):
        self._CardNumber = Card._NextCardNumber
        Card._NextCardNumber += 1
        self._Score = 0

    def GetScore(self):
        return self._Score

    def Process(self, Deck, Discard, Hand, Sequence, CurrentLock, Choice, CardChoice):
        pass

    def GetCardNumber(self): 
        return self._CardNumber

    def GetDescription(self):
        if self._CardNumber < 10:
            return " " + str(self._CardNumber)
        else:
            return str(self._CardNumber)

class ToolCard(Card):
    def __init__(self, *args):
        self._ToolType = args[0]   
        self._Kit = args[1]
        if len(args) == 2:
            super(ToolCard, self).__init__()
        elif len(args) == 3:
            self._CardNumber = args[2]
        self.__SetScore()
        
    def __SetScore(self):
        if self._ToolType == "K":
            self._Score = 3
        elif self._ToolType == "F":
            self._Score = 2
        elif self._ToolType == "P":
            self._Score = 1
            
    def GetDescription(self):
        return self._ToolType + " " + self._Kit

class DifficultyCard(Card):
    def __init__(self, *args):
        self._CardType = "Dif"   
        if len(args) == 0:
            super(DifficultyCard, self).__init__()
        elif len(args) == 1:
            self._CardNumber = args[0]
        
    def GetDescription(self):
        return self._CardType

    def Process(self, Deck, Discard, Hand, Sequence, CurrentLock, Choice, CardChoice):
        ChoiceAsInteger = None
        try:
            ChoiceAsInteger = int(Choice)
        except:
            pass
        if ChoiceAsInteger is not None:
            if ChoiceAsInteger >= 1 and ChoiceAsInteger <= 5:
                if ChoiceAsInteger >= CardChoice:
                    ChoiceAsInteger -= 1
                if ChoiceAsInteger > 0:
                    ChoiceAsInteger -= 1
                if Hand.GetCardDescriptionAt(ChoiceAsInteger)[0] == "K":
                    CardToMove = Hand.RemoveCard(Hand.GetCardNumberAt(ChoiceAsInteger))
                    Discard.AddCard(CardToMove)
                    return
        Count = 0
        while Count < 5 and Deck.GetNumberOfCards() > 0:
            CardToMove = Deck.RemoveCard(Deck.GetCardNumberAt(0))
            Discard.AddCard(CardToMove)
            Count += 1

class GeniusCard(Card):

    def __init__(self):
        self._CardType = "Gen"
        super.__init__()

    def GetDescription(self):
        return self._CardType

class CardCollection():
    def __init__(self, N):
        self._Name = N
        self._Cards = []
        self._NumPicks = 0
        self._NumFiles = 0
        self._NumKeys = 0

    def GetName(self):
        return self._Name

    def GetCardNumberAt(self, X):
        return self._Cards[X].GetCardNumber()

    def GetCardDescriptionAt(self, X):
        return self._Cards[X].GetDescription()

    def AddCard(self, C):
        self._Cards.append(C)
        self.UpdateNum()
    
    def GetNumberOfCards(self) -> int:
        return len(self._Cards)

    def Shuffle(self):
        for Count in range(10000):
            RNo1 = random.randint(0, len(self._Cards) - 1)
            RNo2 = random.randint(0, len(self._Cards) - 1)
            self._Cards[RNo2], self._Cards[RNo1] = self._Cards[RNo1], self._Cards[RNo2]

    def RemoveCard(self, CardNumber):
        CardFound  = False
        Pos  = 0
        while Pos < len(self._Cards) and not CardFound:
            if self._Cards[Pos].GetCardNumber() == CardNumber:
                CardToGet = self._Cards[Pos]
                CardFound = True
                self._Cards.pop(Pos)
            Pos += 1
        self.UpdateNum()
        return CardToGet

    def __CreateLineOfDashes(self, Size):
        LineOfDashes = ""
        for Count in range(Size):
            LineOfDashes += "------"
        return LineOfDashes
    
    def GetCardDisplay(self):
        CardDisplay = "\n" + self._Name + ":"
        if len(self._Cards) == 0:
            return CardDisplay + " empty" + "\n" + "\n"
        else:
            CardDisplay += "\n" + "\n"
        LineOfDashes = ""
        CARDS_PER_LINE = 10
        if len(self._Cards) > CARDS_PER_LINE:
            LineOfDashes = self.__CreateLineOfDashes(CARDS_PER_LINE)
        else:
            LineOfDashes = self.__CreateLineOfDashes(len(self._Cards))
        CardDisplay += LineOfDashes + "\n"
        Complete = False
        Pos  = 0
        while not Complete:
            CardDisplay += "| " + self._Cards[Pos].GetDescription() + " "
            Pos += 1
            if Pos % CARDS_PER_LINE == 0:
                CardDisplay += "|" + "\n" + LineOfDashes + "\n"
            if Pos == len(self._Cards):
                Complete = True
        if len(self._Cards) % CARDS_PER_LINE > 0:
            CardDisplay += "|" + "\n"
            if len(self._Cards) > CARDS_PER_LINE:
                LineOfDashes = self.__CreateLineOfDashes(len(self._Cards) % CARDS_PER_LINE)
            CardDisplay += LineOfDashes + "\n"
        return CardDisplay
    
    def GetCardString(self) -> str:
        cardStringList = []
        for card in self._Cards: cardStringList.append(f"{card.GetDescription()} {card.GetCardNumber()}")
        return f"{",".join(cardStringList)}\n"
    
    def UpdateNum(self):
        self._NumPicks, self._NumFiles, self._NumKeys = 0, 0, 0
        for card in self._Cards:
            if card.GetDescription()[0] == "K": self._NumKeys += 1
            elif card.GetDescription()[0] == "F": self._NumFiles += 1
            elif card.GetDescription()[0] == "P": self._NumPicks += 1

    def DisplayStats(self) -> str:
        return f"\nThere is a {round(((self._NumKeys / self.GetNumberOfCards()) * 100), 2)}% chance that the next card will be a key, a {round(((self._NumFiles / self.GetNumberOfCards()) * 100), 2)}% chance that it will be a file and a {round(((self._NumPicks / self.GetNumberOfCards()) * 100), 2)}% chance that it will be a pick.\n"

if __name__ == "__main__":
    Main()
