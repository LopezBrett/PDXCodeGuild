print('Enter Player One Name:')
pl1_nam_var = input()
print('Enter Player Two Name:')
pl2_nam_var = input()
# character select
orc_cha_var = 'Orc'
bar_cha_var = 'Barbarian'
# player 1 select


class pl1_cho:
    print('Player One select Hero. ', {orc_cha_var}, ' or the ', {bar_cha_var}, '?',)
pl1_cha_sel = input()
# Find Hero
fin_her_1 = pl1_cha_sel


class pla_1_her:
    if fin_her_1.capitalize() in ['Orc',]:
        print("You have chosen the Orc! WaaaAaaaag!")
    elif fin_her_1.capitalize() in ['Barbarian',]:
        print('You have chose have The Barbarian! Smash all the stuff!')
    else:
        print('Try again'), pla_1_her.



#print('Player Two select Hero. ', {orc_cha_var}, ' or the ', {bar_cha_var}, '?',)
#pl2_cha_sel = input()
#
#print(pl1_nam_var,'the',pl1_cha_sel,)
#print({pl2_nam_var},'the',{pl2_cha_sel},)

# select dungeon size
# start of player turn random tile flip
# player choose flip
# player move
# win conditions / first to reach the center