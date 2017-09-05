# Story info generator

# Reader input
noun_a = input('Enter a color: ')
noun_b = input('Enter a plural body part noun: ')
noun_c = input('Enter a body part noun: ')
noun_d = input('Enter a noun: ')
noun_e = input('Enter an animal: ')
# insert a list input for adjective
adjective_a = input('Enter a superlative adjective: ')
adjective_b = input('Enter an adjective: ')
adjective_c = input('Enter an adjective: ')
adjective_d = input('Enter an adjective: ')
adjective_e = input('Enter an adjective: ')
# list for Adjectives
adj_lis_var = [{adjective_b}, {adjective_c}, {adjective_d}, {adjective_e},]
# make list random
import random
ran_adj_var = random.sample(adj_lis_var, 4)
# Story Loop
story_loop = input('Would you like to hear your story?: ')
# find yes or no
# mad lib output
print ('The', noun_a, 'Dragon is the', adjective_a, 'Dragon of all. It has',ran_adj_var[0],',',noun_b,',and a',noun_c,'shaped like a',noun_d,'.'
       ' It loves to eat ', noun_e, ', although it will feast on nearly anything. It is ', ran_adj_var[1], ' and ', ran_adj_var[2], '.'
       ' You must be ', ran_adj_var[3], ' around it, or you may end up as it\'s meal!')
