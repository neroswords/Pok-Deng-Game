import random

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

def getPoint(points):
    for i in range(2):
        if points[i] in range(10,14):
            points[i] = 0
    return points[0]+points[1]

def readCard(card):
    if card == 11:
        return "Jack"
    elif card == 12:
        return "Queen"
    elif card == 13:
        return "King"
    else: return card

def newDeck():
    colors = ['heart', 'diamonds', 'spades', 'clubs']
    deck = [Card(value, color) for value in range(1, 14) for color in colors]
    return deck

def playCard(bet):
    player = []
    dealer = []
    deck = newDeck()
    random.shuffle(deck)
    for i in range(2):
        player.append(deck.pop())
        dealer.append(deck.pop())
    player_points = getPoint([player[0].value,player[1].value])
    dealer_points = getPoint([dealer[0].value,dealer[1].value])
    print("You got ",player[0].color,"-",readCard(player[0].value),",",player[1].color,"-",readCard(player[1].value))
    print("The dealer got ",dealer[0].color,"-",readCard(dealer[0].value),",",dealer[1].color,"-",readCard(dealer[1].value))
    if player_points > dealer_points:
        print("You won!!!, received ",bet," chips")
        return bet
    elif player_points < dealer_points:
        print("You lose, pay ",bet," chips")
        return bet * (-1)
    elif player_points == dealer_points:
        print("You draw with him, get nothing")
        return 0
    

def main():
    total_recives = 0
    while True:
        while True:
            try:
                bet = int(input('Please put your bet : '))
            except ValueError:
                print('you can input only integers')
                continue
            break
        received = playCard(bet)
        total_recives += received
        inp = input("Wanna play more (Yes(y) / No(n) or input anything else for exit)?")
        if  inp in ["Yes","y","yes"]:
            continue
        else:
            if total_recives >= 0 :
                print("You got total ", total_recives, " chips")
            else:
                print("You loss total ", total_recives*(-1), " chips")
            break


if __name__ == '__main__':
    main()