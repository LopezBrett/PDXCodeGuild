import subprocess

class TruFal:
    no_var = ['n', 'no']
    yes_var = ['y', 'yes']
class Wordfind:
    def wordfind():
        import re

        my_string = cur_pla_inp.lower()
        re_word = re.escape(cur_wor_puz.lower())
        bou_wor = re_word
        global cur_mat
        cur_mat = re.findall(bou_wor, my_string)

def restart():
    print('''
    Would you like to play again?
    ''')
    exitdungeon = input('(Y or N): ')
    if exitdungeon.lower() in TruFal.no_var:
        import sys
        print("Press any key to exit")
        input()
        sys.exit()
    elif exitdungeon.lower() in TruFal.yes_var:
        subprocess.call('cls', shell=True)
        Story.story1()
    else:
        subprocess.call('cls', shell=True)
        restart()

class Story:

    def story1():
        print('''
        █████████████████████████████████████████████████████████████████████████████████████████████████████████████
        ███████▀▀▀░░░░░░░▀▀▀██████████████▀▀▀░░░░░░░▀▀▀███████████████▀▀▀░░░░░░░▀▀▀██████████████▀▀▀░░░░░░░▀▀▀███████
        ████▀░░░░░░░░░░░░░░░░░▀████████▀░░░░░░░░░░░░░░░░░▀█████████▀░░░░░░░░░░░░░░░░░▀████████▀░░░░░░░░░░░░░░░░░▀████
        ███│░░░░░░░░░░░░░░░░░░░│██████│░░░░░░░░░░░░░░░░░░░│███████│░░░░░░░░░░░░░░░░░░░│██████│░░░░░░░░░░░░░░░░░░░│███
        ██▌│░░░░░░░░░░░░░░░░░░░│▐████▌│░░░░░░░░░░░░░░░░░░░│▐█████▌│░░░░░░░░░░░░░░░░░░░│▐████▌│░░░░░░░░░░░░░░░░░░░│▐██
        ██░└┐░░░░░░░░░░░░░░░░░┌┘░████░└┐░░░░░░░░░░░░░░░░░┌┘░█████░└┐░░░░░░░░░░░░░░░░░┌┘░████░└┐░░░░░░░░░░░░░░░░░┌┘░██
        ██░░└┐░░░░░░░░░░░░░░░┌┘░░████░░└┐░░░░░░░░░░░░░░░┌┘░░█████░░└┐░░░░░░░░░░░░░░░┌┘░░████░░└┐░░░░░░░░░░░░░░░┌┘░░██
        ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░████░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░█████░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░████░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
        ██▌░│██████▌░░░▐██████│░▐████▌░│██████▌░░░▐██████│░▐█████▌░│██████▌░░░▐██████│░▐████▌░│██████▌░░░▐██████│░▐██
        ███░│▐███▀▀░░▄░░▀▀███▌│░██████░│▐███▀▀░░▄░░▀▀███▌│░███████░│▐███▀▀░░▄░░▀▀███▌│░██████░│▐███▀▀░░▄░░▀▀███▌│░███
        ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀████▀─┘░░░░░░░▐█▌░░░░░░░└─▀█████▀─┘░░░░░░░▐█▌░░░░░░░└─▀████▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
        ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄████▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄█████▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄████▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
        ████▄─┘██▌░░░░░░░▐██└─▄████████▄─┘██▌░░░░░░░▐██└─▄█████████▄─┘██▌░░░░░░░▐██└─▄████████▄─┘██▌░░░░░░░▐██└─▄████
        █████░░▐█─┬┬┬┬┬┬┬─█▌░░██████████░░▐█─┬┬┬┬┬┬┬─█▌░░███████████░░▐█─┬┬┬┬┬┬┬─█▌░░██████████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
        ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐█████████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
        █████▄░░░└┴┴┴┴┴┴┴┘░░░▄██████████▄░░░└┴┴┴┴┴┴┴┘░░░▄███████████▄░░░└┴┴┴┴┴┴┴┘░░░▄██████████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
        ███████▄░░░░░░░░░░░▄██████████████▄░░░░░░░░░░░▄███████████████▄░░░░░░░░░░░▄██████████████▄░░░░░░░░░░░▄███████
        ██████████▄▄▄▄▄▄▄████████████████████▄▄▄▄▄▄▄█████████████████████▄▄▄▄▄▄▄████████████████████▄▄▄▄▄▄▄██████████
        █████████████████████████████████████████████████████████████████████████████████████████████████████████████
        ''')
        print('''
        Welcome to the Dungeon of Doom.
        You awaken, standing, in a poorly lit room. A single torch in the center of the room flickers making the cold 
        stone walls dance eerily in silence. You hear approaching footsteps.
        What do you do? 
        ''')
        global cur_wor_puz
        cur_wor_puz = "torch"
        global cur_pla_inp
        cur_pla_inp = input(': ')
        Wordfind.wordfind()
        if cur_wor_puz in cur_mat:
            import config
            subprocess.call('cls', shell=True)
            print('''
            As you approach the torch a soft breeze crosses the back of your neck and you hear a faint whisper "You might just 
            survive this". When you lift the torch from the floor a dead spider falls from the handle. Not even the smallest 
            of creatures find comfort here. With the torch raised it becomes clear the situation you are in. There are no doors,
            no windows, the frigged stone walls are ancient... and lonely. 
            ''')
        else:
            print(
                'The torch dims to nothingness. The dark room somehow becomes more silent. You close your eyes to only never '
                'open them again.')
            restart()

    def storya():
        import playermod
        subprocess.call('cls', shell=True)
        playermod.Player1dash.Printplayer1dash()
        print('\nYou feel the soft touch of hands on your shoulder and a voice whispers from behind you \"', playermod.Getplayername.pla_nam,
              '\".\n')

    def story2():
        print('''
        Do you turn around?
        ''')
        cur_pla_inp = input('(Y or N): ')
        if cur_pla_inp.lower() in TruFal.yes_var:
            import playermod
            subprocess.call('cls', shell=True)
            playermod.Player1dash.Printplayer1dash()
            print('''
            As you turn your skin fills with goosebumps. You no longer feel the hands, the imaginary being dissipated back
            into the darkness and mysteriously the room has expanded. A small table now stands in front of you. The 
            table adorned with three animal hides. The room still only lit by your torch the shadows confine to watch and 
            dance.
            ''')
        elif cur_pla_inp.lower() in TruFal.no_var:
            subprocess.call('cls', shell=True)
            print('''
            no... it starts slowly. You feel the ghostly touch of a hand multiply into a horde. The hands crawling over your 
            backside. The remains of, what can best be described as, an arm reaches over your shoulder and grabs your torch
            by the flame; extinguishing the light. You still feel the presence of the fire as it quickly engulfs you. Your 
            screams echo within the room and fade to silence as you are never heard from again.
            ''')
            restart()
        else:
            print('Are you speaking human? Try Again')
            Story.story2()