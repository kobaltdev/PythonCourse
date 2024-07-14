def love_meet(l1, l2):
    common = []
    for a in l1:
        if a in l2:
            common.append(a) 
    
    return set(common)


def affair_meet(l1, l2, l3):
    common_l2_l3 = love_meet(l2, l3)
    for v in l1:
        if v in common_l2_l3:
            common_l2_l3.remove(v)
    return common_l2_l3



alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']

bob = ['IV', 'III', 'II', 'XX', 'II', 'XX']

silvester = ['XVIII', 'XIX', 'III', 'I', 'III', 'XVIII']


print(love_meet(bob, alice))

print(affair_meet(bob, alice, silvester))

