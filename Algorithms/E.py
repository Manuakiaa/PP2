"""Boris and Nursik play a drunkard card game. In the drunkard card game, all cards are divided equally between two players. Then they reveal one top card, and the one whose card is higher takes both of the revealed cards for himself, which are put under the bottom of his deck. The one who is left without cards loses.

The player who takes the cards for himself first puts the Boris’s card under the bottom of his deck, then the Nursik’s card (that is, the Nursik’s card is at the bottom of the deck).

Write a program that simulates the drunkard card game and determines who wins. The game involves 10 cards with values from 0 to 9, the larger card wins the smaller one. The one special thing is that the card with a value of 0 wins card 9."""

def compare(q,e):
    if q == 0 and e == 9:
        return 1
    elif q == 9 and e == 0:
        return 2
    elif q > e:
        return 3
    elif q < e:
        return 4

Boris = list(map(int, input().split()))
Nursik = list(map(int, input().split()))
Move = 0
while True:
    if not Boris:
        print("Nursik", end=' ')
        break
    if not Nursik:
        print("Boris", end=' ')
        break
    B = Boris.pop(0)
    N = Nursik.pop(0)
    Answer = compare(B, N)
    if Answer == 1:
        Boris.append(B)
        Boris.append(N)
    elif Answer == 2:
        Nursik.append(B)
        Nursik.append(N)
    elif Answer == 3:
        Boris.append(B)
        Boris.append(N)
    elif Answer == 4:
        Nursik.append(B)
        Nursik.append(N)
    Move += 1
print(Move) 