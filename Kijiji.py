from collections import defaultdict
def findWinner(player1, player2):
    player1_cards = defaultdict(int)
    player2_cards = defaultdict(int)

    player1_parts = player1.split()
    player2_parts = player2.split()
    #print(player1_parts)

    for i in range(5):
        player1_cards[player1_parts[i][0]] += 1
        player2_cards[player2_parts[i][0]] += 1
    #print(player1_cards)

    for rank in (['A','K','Q','J','T', '9', '8', '7', '6', '5', '4', '3', '2']):
        # if rank in player1_cards and rank not in player2_cards:
        #     return 1
        # if rank in player2_cards and rank not in player1_cards:
        #     return 2
        
        # if rank in player1_cards and rank in player2_cards:
            if player1_cards.get(rank, 0) > player2_cards.get(rank, 0):
                return 1
            if player1_cards.get(rank, 0) < player2_cards.get(rank, 0):
                return 2
    
    return 0
        
print(findWinner("JH KS QC 3D 2D", "3H 4S KS QH AD"))
print(findWinner("5H 3S JC JD 2D", "JD 2H TH TH TS"))
print(findWinner("AH KS AC TD 2D", "AH 2C 3H 4S AH"))
print(findWinner("AH 2S 3C 4D 5D", "5C 3S 2H 4S AH"))



