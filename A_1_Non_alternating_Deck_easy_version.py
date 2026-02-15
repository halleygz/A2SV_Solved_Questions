t = int(input())

for i in range(t):
    n = int(input())
    alice, bob = 0, 0
    turn = 1
    cards_left = n
    current_step = 1
    while cards_left > 0:
        take = min(current_step, cards_left)
        if (current_step - 1) % 4 == 0 or (current_step - 1) % 4 == 3:
            alice += take
        else:
            bob += take
        cards_left -= take
        current_step += 1
    print(alice, bob)

        
