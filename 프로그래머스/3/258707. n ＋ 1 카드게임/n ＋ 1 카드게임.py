from collections import deque
def check(cards1,cards2,target):
    for card1 in cards1:
        if (target-card1) in cards2:
            cards1.remove(card1)
            cards2.remove(target-card1)
            return True
    return False

def solution(coin, cards):
    hand=cards[:len(cards)//3]
    deck=deque(cards[len(cards)//3:])
    pending=[]
    
    target=len(cards)+1
    turn=1
    
    while coin>=0 and hand:
        pending.append(deck.popleft())
        pending.append(deck.popleft())
        
        if check(hand,hand,target):
            pass
        elif coin>=1 and check(hand,pending,target):
            coin-=1
        elif coin>=2 and check(pending,pending,target):
            coin-=2
        else: 
            break
        
        turn+=1

    return turn