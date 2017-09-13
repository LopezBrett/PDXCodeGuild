class Getplayername:
    print('''
    \"What is your name?\" demands a voice.
    ''')
    pla_nam = input(': ')

class player1:
    pla_1_char = {Getplayername.pla_nam: {'Health': 15, 'Power': 10, 'Defense': 7, 'Magic': 0,}, }
#class Player1equipment:
#    pla_1_qui_dict = {'Player1item': {'Head': 'empty', 'Neck': 'empty', 'Shoulders': 'empty','Chest': 'empty', 'Stomach': 'empty', 'Waist': 'empty', {'Arms':{'Left arm': 'empty', 'Right arm': 'empty',},}, {'Hands':{'Left hand': 'empty', 'Right hand': 'empty',},}, {'Legs':{'Left leg': 'empty', 'Right leg': 'empty',},},},}

#class player1itembag:

#    pla_1_ite = 'empty'
#    pla_2_ite = 'empty'
#    pla_3_ite = 'empty'
#    pla_4_ite = 'empty'
#    pla_5_ite = 'empty'
#    pla_6_ite = 'empty'
#    pla_7_ite = 'empty'
#    pla_8_ite = 'empty'

class Player1dash:

    def Printplayer1dash():
        print('-----------------------------------------------------------------')
        print(player1.pla_1_char)
        print('-----------------------------------------------------------------')
        print('============================ITEMS================================')
#       print(player1item.pla_1_ite_dict)
        print('-----------------------------------------------------------------')
        print('-----------------------------------------------------------------')