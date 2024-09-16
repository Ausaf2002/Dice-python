import random

Dice = [1,2,3,4,5,6]
outcomes=[0, 0, 0, 0, 0, 0]

for i in range(1000):
    turn = random.choice(Dice)
    if turn == 1:
        outcomes[0]+=1
    elif turn == 2:
        outcomes[1]+=1
    elif turn == 3:
        outcomes[2]+=1
    elif turn == 4:
        outcomes[3]+=1
    elif turn == 5:
        outcomes[4]+=1
    else:
        outcomes[5]+=1
        
print("1 = "+ str(outcomes[0]))
print("2 = "+ str(outcomes[1]))
print("3 = "+ str(outcomes[2]))
print("4 = "+ str(outcomes[3]))
print("5 = "+ str(outcomes[4]))
print("6 = "+ str(outcomes[5]))
        
