#card_deck = [4, 8, 8, 5, 13, 2, 11, 10]
card_deck =[5,7,5,8,3,2]
hand = []

while sum(hand) <= 17:  # i.e, stops when the sum is 18       
    hand.append(card_deck.pop())
    
print(hand)
