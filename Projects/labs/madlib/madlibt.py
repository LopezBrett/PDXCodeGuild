import random
class Nountypes:
    inp_nou = input('Enter a noun: ')
    inp_col_nou = input('Enter a color: ')
    inp_body_nou_plu = input('Enter a plural body part noun: ')
    inp_bod_nou = input('Enter a body part noun: ')
    inp_ani_nou = input('Enter an animal: ')
class Adjectivetypes:
    inp_adj = input('Enter an adjective: ')
    inp_supr_adj = input('Enter a superlative adjective: ')
class Nouncount:
    inp_qua_nou = 0
    inp_qua_col_nou = 0
    inp_qua_body_nou_plu = 0
    inp_qua_bod_nou = 0
    inp_qua_ani_nou = 0
class Adjectivecount:
    inp_qua_adj = 0
    inp_qua_supr_adj = 0
class Listgen:
    adj_lis_var = [{adjective_b}, {adjective_c}, {adjective_d}, {adjective_e}, ]
    nou_qua_var = inp_qua_nou + inp_qua_col_nou + inp_qua_body_nou_plu + inp_qua_bod_nou + inp_qua_ani_nou
    adj_qua_var = inp_qua_adj + inp_qua_supr_adj
class madlib:
    madlib1 = Nouncount()
    inp_qua_nou = 1
    inp_qua_col_nou = 1
    inp_qua_body_nou_plu = 1
    inp_qua_bod_nou = 1
    inp_qua_ani_nou = 1
    inp_qua_adj = 4
    inp_qua_supr_adj = 1


# Story info nouns quantity

# Populate noun list size
pop_nou_lst_siz = nou_qua_var * 1 * [None]
# Deep Copy Count
# Populate noun list types
#inp_qua_nou * 1 *
# Populate list Nouns
nou_qua_var = [{pop_nou_lst_siz.append}, {}, {}, {},]
# Insert list Nouns

# make Noun list random
ran_nou_var = random.sample(nou_lis_var, 4)

# Story info adjectives quantity
#adj_cou_var = inp_adj = 4, inp_sup_adj = 1,
# Populate list for Adjectives
#adj_lis_var = [{adjective_b}, {adjective_c}, {adjective_d}, {adjective_e},]
# make Adjectives list random
#ran_adj_var = random.sample(adj_lis_var, 4)
# close program
