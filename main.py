from time import sleep
import random

room_1_right_wall_broken = False
room_2_right_wall_broken = False
room_2_left_enemy_killed = False
npc_house_npc_killed = False
room_2_right_wall_hp = 3
player_hp = 5
room_2_left_enemy_hp = 2
boss_hp = 12
player_dmg = 1
player_move = ""
player_reaction_move = ""
dodged = None
word_delay = 0.#05
current_room = ""

def create_save():
    global room_1_right_wall_broken
    global room_2_right_wall_broken
    global npc_house_npc_killed
    global player_hp
    global player_dmg
    global current_room
    current_room = "start_game"
    save_1 = open(f"saves\\save_1.txt", "w")

    save_1.write("room_1_right_wall_broken:" + str(room_1_right_wall_broken) + " \n")
    save_1.write("room_2_right_wall_broken:" + str(room_2_right_wall_broken) + " \n")
    save_1.write("npc_house_npc_killed:" + str(npc_house_npc_killed) + " \n")
    save_1.write("player_hp:" + str(player_hp) + " \n")
    save_1.write("player_dmg:" + str(player_dmg) + " \n")
    save_1.write("current_room:" + str(current_room) + " \n")
    save_1.close()
    start_game()

def save_game():
    global room_1_right_wall_broken
    global room_2_right_wall_broken
    global npc_house_npc_killed
    global player_hp
    global player_dmg
    global current_room
    save_1 = open(f"saves\\save_1.txt", "w")

    save_1.write("room_1_right_wall_broken:" + str(room_1_right_wall_broken) + " \n")
    save_1.write("room_2_right_wall_broken:" + str(room_2_right_wall_broken) + " \n")
    save_1.write("npc_house_npc_killed:" + str(npc_house_npc_killed) + " \n")
    save_1.write("player_hp:" + str(player_hp) + " \n")
    save_1.write("player_dmg:" + str(player_dmg) + " \n")
    save_1.write("current_room:" + str(current_room) + " \n")
    save_1.close()

def load_game():
    global room_1_right_wall_broken
    global room_2_right_wall_broken
    global npc_house_npc_killed
    global player_hp
    global player_dmg
    global current_room
    save_1 = open(f"saves\\save_1.txt", "r")
    saved_variables = save_1.readlines()
    for i in saved_variables:
        if "room_1_right_wall_broken:" in i:
            room_1_right_wall_broken = eval(i[25:])
        elif "room_2_right_wall_broken:" in i:
            room_2_right_wall_broken = eval(i[25:])
        elif "npc_house_npc_killed:" in i:
            npc_house_npc_killed = eval(i[21:])
        elif "player_hp:" in i:
            player_hp = int(i[10:])
        elif "player_dmg:" in i:
            player_dmg = float(i[11:])
        elif "current_room:" in i:
            current_room = i[13:]
    save_1.close()
    eval(current_room)()

def play_game():
    choice = valid_input("What would you like to do?\n Start New Save\n Load a Save", ["new", "load", "start"]).lower()
    if "new" in choice or "start" in choice:
        create_save()
    else:
        load_game()

def available_commands():
    global current_room
    global npc_house_npc_killed
    if current_room == "npc_house" and "npc_house_npc_killed" == False:
        delayed_print_words("Available Commands:\n Jump to the Left\n Jump to the Right\n Move Left\n Move Right\n Jump Up\n Attack\n Talk\n Exit to Title\n Help")
        current_room()
    elif current_room == "room_3_town":
        delayed_print_words("Available Commands:\n Jump to the Left\n Jump to the Right\n Move Left\n Move Right\n Jump Up\n Attack\n Enter House\n Exit to Title\n Help")
        current_room()
    else:
        delayed_print_words("Available Commands:\n Jump to the Left\n Jump to the Right\n Move Left\n Move Right\n Jump Up\n Attack\n Exit to Title\n Help")
        current_room()

def exit_to_title():
    global current_room
    answer = valid_input("Are you sure you want to exit the game?\n Yes\n No", ["yes", "no"])
    if "yes" in answer:
        save_game()
        title_screen()
    else:
        delayed_print_words(f"goes to {current_room}")
        eval(current_room)()

def delayed_print_words(text):
    for char in text:
        sleep(word_delay)
        print(char, end="")
    sleep(0.5)
    print("")
    return ""

def valid_input(input_text, options=[]):
    while True:
        sleep(word_delay)
        response = input(delayed_print_words(input_text)).lower()
        for option in options:
            if option in response:
                return response
        delayed_print_words("That isn't a response i know what to do with. \nPlease check your spelling and try again.")
        delayed_print_words("For a list of Commands enter Help")

def title_screen():
    delayed_print_words("Title Screen:")
    choice = valid_input("What would you like to do?\n Play Game\n Settings\n Close Game", ["play", "play game", "settings", "close", "close game"]).lower()
    if  "play" in choice:
        play_game()
    elif "settings" in choice:
        settings()
    else:
        exit()

def is_float(user_input):
    try:
        float(user_input)
    except ValueError:
        return False
    return True

def settings():
    delayed_print_words("Settings:")
    choice = valid_input("What would you like to do?\n Change The Text Speed\n Exit to the Title Screen", ["text", "speed", "exit"]).lower()
    if "text" in choice or "speed" in choice:
        set_text_speed()
    else:
        title_screen()

def set_text_speed():
    global word_delay
    delayed_print_words("Please input the text speed you want:")
    text_speed = input()
    if text_speed > 2:
        delayed_print_words("That number is to High")
        set_text_speed()
    elif is_float(text_speed):
        word_delay = float(text_speed)
        settings()
    else:
        delayed_print_words("That isn't a number.\nPlease enter a number.")
        set_text_speed()

def room_1():
    global current_room
    current_room = "room_1"
    delayed_print_words("""You find yourself in the middle of a decently sized, but dimly-lit cavern.\nOn each side of this cavern a wall seems to extend upwards forever.""")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("""You leap towards the left side of the cavern.""")
        room_1_left()
    elif "right" in action and "jump" in action:
        delayed_print_words("""You leap towards the right of the cavern.""")
        room_1_right()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("""You walk to the left side of the cavern.""")
        room_1_left()
    elif "right" in action:
        delayed_print_words("""You walk to the right side of the cavern.""")
        room_1_right()
    elif "jump" in action:
        delayed_print_words("""You leap high into the air and land right where you jumped from.""")
        room_1()
    elif "exit" in action:
        exit_to_title()
    else:
        delayed_print_words("You swing your sword out in front of you.")
        room_1()

def room_1_left():
    global current_room
    current_room = "room_1_left"
    delayed_print_words("""You look at the wall.\nIt seems to be of sturdy construction.""")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("""You leap to the left as your face smashes against the wall.""")
        room_1_left()
    elif "right" in action and "jump" in action:
        delayed_print_words("""You leap towards the middle of the cavern.""")
        room_1()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("Walks into wall goes to room 1 left")
    elif "right" in action:
        delayed_print_words("""You walk into the wall.""")
        room_1()
    elif "jump" in action:
        delayed_print_words("""You leap high into the air and land right where you jumped from.""")
        room_1_left()
    elif "exit" in action:
        exit_to_title()
    else:
        delayed_print_words("""You swing your sword at the wall.\nA piece of the stone chips off.""")
        room_1_left()

def room_1_right():

    global room_1_right_wall_broken
    global current_room
    current_room = "room_1_right" 

    if room_1_right_wall_broken == False:
        delayed_print_words("""You look at the wall.\nPart of the wall has large cracks down it.\nPeering through the largest crack, you notice on the other side there is something moving.""")
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "right", "left", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("""You leap towards the middle of the cavern.""")
            room_1()
        elif "right" in action and "jump" in action:
            delayed_print_words("""You leap to the right as your face smashes against the wall.""")
            room_1_right()
        elif "help" in action:
            available_commands()
        elif "right" in action:
            delayed_print_words("""You walk into the wall.""")
            room_1_right()
        elif "left" in action:
            delayed_print_words("""You walk to the middle of the cavern.""")
            room_1()
        elif "jump" in action:
            delayed_print_words("""You leap high into the air and land right where you jumped from.""")
            room_1_right()
        elif "exit" in action:
            exit_to_title()
        else:
            delayed_print_words("""You swing your sword at the wall.\nWhen your sword makes contact with the wall, the cracks begin to widen!\nAs the cracks in the wall rapidly get bigger a portion of the wall crumbles to the ground.\nWith the wall broken you can probably squeeze through.""")
            room_1_right_wall_broken = True
            room_1_right()

    if room_1_right_wall_broken == True:
        delayed_print_words("""You are standing on the right side of a dimly lit cavern.\nThe wall to your right seems to have been broken.\nThe hole looks large enough to squeeze through.""")
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("""You leap towards the middle of the cavern.""")
            room_1()
        elif "right" in action and "jump" in action:
            delayed_print_words("""You leap to the right as your face smashes against the wall.""")
            room_1_right()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("""You walk to the middle of the cavern.""")
            room_1()
        elif "jump" in action:
            delayed_print_words("""You leap high into the air and land right where you jumped from.""")
            room_1_right()
        elif "attack" in action:
            delayed_print_words("""You swing your sword at the wall.\nA bit of the stone around the hole chips off.""")
            room_1_right()
        elif "exit" in action:
            exit_to_title()
        else:
            delayed_print_words("""You squeeze your way through the hole in the wall.""")
            room_2_far_left()
            
def room_2_far_left():
    global current_room
    current_room = "room_2_far_left"
    if room_2_left_enemy_killed == False:
        delayed_print_words("""You look around and see a long cavern ahead.\nYou notice the ceiling in here is a little way above your head.\nYou see something moving farther along the cavern.""")
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("""You leap to the left as your head smashes into the ceiling.""")
            room_2_far_left()
        elif "right" in action and "jump" in action:
            delayed_print_words("""You leap to the right as your head smashes into the ceiling.""")
            room_2_far_left()
        elif "help" in action:
            available_commands()
        elif "right" in action:
            delayed_print_words("""You walk to the right of the long cavern.""")
            room_2_left()
        elif "left" in action:
            delayed_print_words("""You squeeze your way through the hole in the wall.""")
            room_1_right()
        elif "jump" in action:
            delayed_print_words("""You leap into the air as your head smashes into the ceiling.""")
            room_2_far_left()
        elif "exit" in action:
            exit_to_title()
        else:
            delayed_print_words("""You swing your sword out in front of you.""")
            room_2_far_left()
    else:
        delayed_print_words("""You look around and see a long cavern ahead.\nYou notice the ceiling in here is a little way above your head.""")
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("""You leap to the left as your head smashes into the ceiling.""")
            room_2_far_left()
        elif "right" in action and "jump" in action:
            delayed_print_words("""You leap to the right as your head smashes into the ceiling.""")
            room_2_far_left()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("""You squeeze your way through the hole in the wall.""")
            room_1_right()
        elif "right" in action:
            delayed_print_words("""You walk to the right of the long cavern.""")
            room_2_left()
        elif "jump" in action:
            delayed_print_words("""You leap into the air as your head smashes into the ceiling.""")
            room_2_far_left()
        elif "exit" in action:
            exit_to_title()
        else:
            delayed_print_words("""You swing your sword out in front of you.""")
            room_2_far_left()
    
def room_2_left():
    global current_room
    current_room = "room_2_left"
    delayed_print_words("You look around and see a long cavern ahead.\nYou notice the ceiling in here is a little way above your head.")
    if room_2_left_enemy_killed == False:
        first_combat_players_turn()
    else:
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("""You leap to the left as your head smashes into the ceiling.""")
            room_2_left()
        elif "right" in action and "jump" in action:
            delayed_print_words("""You leap to the right as your head smashes into the ceiling.""")
            room_2_left()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("""You walk to the left of the long cavern.""")
            room_2_far_left()
        elif "right" in action:
            delayed_print_words("""You walk to the right of the long cavern.""")
            room_2_right()
        elif "jump" in action:
            delayed_print_words("""You leap into the air as your head smashes into the ceiling.""")
            room_2_left()
        elif "exit" in action:
            exit_to_title()
        else:
            delayed_print_words("""You swing your sword out in front of you.""")
            room_2_left()

def first_combat_players_turn():
    global player_dmg
    global player_hp
    global room_2_left_enemy_hp
    global room_2_left_enemy_killed
    global player_move
    global current_room
    current_room = "first_combat_players_turn"

    if player_hp <= 0:
        delayed_print_words("""As you take that last hit you know this is the end of you.\nYour limbs begin to feel weak as the last bit of your lifeforce fades away.\n\nYou have lost.""")
        save_1 = open(f"saves\\save_1.txt", "w")
        save_1.write("Dead")
        save_1.close()
        title_screen()
    elif room_2_left_enemy_hp <= 0:
        delayed_print_words("""As your sword connects with the beast, its thick carapace splits.\nBlack foul-smelling blood pours out of the gaping wound and the giant bug’s lifeless corpse falls to the ground.""")
        room_2_left_enemy_killed = True
        room_2_left()
    delayed_print_words("In front of you, you see a large bug-like creature come barreling towards you.")
    delayed_print_words(f"Your HP:{player_hp}")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("You leap out of the way of the beasts attack.")
        player_move = "jump"
        first_combat_enemies_turn()
    elif "right" in action and "jump" in action:
        delayed_print_words("""You leap over the beast.\nAs you get to the other side of the beast you see the ground isnt at the same level you jumped from, and you fall into a hole in the ground.""")
        in_pit()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("You run to the left of the long cavern away from the beast.")
        room_2_far_left()
    elif "right" in action:
        delayed_print_words("""You walk to the right going headfirst into the beasts attack.\nYou feel a sharp pain run through your body""")
        player_hp -= 1
        player_move = "right"
        first_combat_enemies_turn()
    elif "jump" in action:
        delayed_print_words("""You leap out of the way of the beasts attack.""")
        player_move = "jump"
        first_combat_enemies_turn()
    elif "attack" in action:
        delayed_print_words("""You swing your sword at the beast.""")
        room_2_left_enemy_hp -= player_dmg
        player_move = "attack"
        first_combat_enemies_turn()
    else:
        exit_to_title()
      
def first_combat_enemies_turn():

    global player_hp
    global room_2_left_enemy_hp
    global room_2_left_enemy_killed
    global player_move

    if player_hp <= 0:
        delayed_print_words("""As you take that last hit you know this is the end of you.\nYour limbs begin to feel weak as the last bit of your lifeforce fades away.\n\nYou have lost.""")
        save_1 = open(f"saves\\save_1.txt", "w")
        save_1.write("Dead")
        save_1.close()
        title_screen()
    elif room_2_left_enemy_hp <= 0:
        delayed_print_words("""As your sword connects with the beast, its thick carapace splits.\nBlack foul-smelling blood pours out of the gaping wound and the giant bug’s lifeless corpse falls to the ground.""")
        room_2_left_enemy_killed = True
        room_2_left()
    if player_move == "attack":
        delayed_print_words("As your sword connects the beast screeches out in pain.")
        first_combat_players_turn()
    elif player_move == "jump":
        delayed_print_words("""The beast charges right past you.""")
        first_combat_players_turn()
    else:
        delayed_print_words("""The bug-like creature’s hulking body slams into you.\nYou feel a sharp pain run through your body.""")
        player_hp -= 1
        first_combat_players_turn()

def room_2_right():
    global current_room
    current_room = "room_2_right"
    delayed_print_words("""You look around and see a long cavern ahead.\nYou notice the ceiling in this part of the cavern is a good ways above your head.\nA few steps away from you, you see a deep pit.""")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("""You leap towards the left of the long cavern.""")
        room_2_left()
    elif "right" in action and "jump" in action:
        delayed_print_words("""You leap over the pit.""")
        room_2_far_right()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("""You walk to the left of the long cavern.""")
        room_2_left()
    elif "right" in action:
        delayed_print_words("""You walk forward and fall into the pit.""")
        in_pit()
    elif "jump" in action:
        delayed_print_words("""You leap high into the air and land right where you jumped from.""")
        room_2_right()
    elif "attack" in action:
        delayed_print_words("""You swing your sword out in front of you.""")
        room_2_right()
    else:
        exit_to_title()

def in_pit():
    global current_room
    current_room = "in_pit"
    delayed_print_words("""You are in a deep pit.""")
    if room_2_right_wall_broken == False: 
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("""You leap out of the pit.""")
            room_2_right()
        elif "right" in action and "jump" in action:
            delayed_print_words("""You leap out of the pit.""")
            room_2_far_right()
        if "left" in action:
            delayed_print_words("""You walk to the left side of the pit.""")
            in_pit()
        elif "right" in action:
            delayed_print_words("""You walk to the right side of the pit.""")
            in_pit()
        elif "help" in action:
            available_commands()
        elif "jump" in action:
            delayed_print_words("""You leap high into the air, as you get to the apex of your jump you see out of the pit.""")
            in_pit()
        elif "attack" in action:
            delayed_print_words("""You swing your sword out in front of you.""")
            in_pit()
        else:
            exit_to_title()

def room_2_far_right():

    global room_2_right_wall_hp
    global room_2_right_wall_broken
    global current_room
    current_room = "room_2_far_right"

    if room_2_right_wall_broken == False:
        if room_2_right_wall_hp == 0:
            delayed_print_words("""The cracks in the wall widen faster and faster!\nSuddenly pieces of the wall start falling down.\nYou jump out of the way narrowly dodging the falling debris.\nLight starts pouring in!\nAs the dust settles you see the source of the light, the moon shining beautifully.""")
            room_2_right_wall_broken = True
            room_2_far_right()
        delayed_print_words("""You are in a large cavern\nUnlike the other caverns you’ve been in this one very well lit.\nLight in this cavern is coming from a large wall on the right\nThe wall has large cracks running down it.""")
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "jump" in action and "left" in action:
            delayed_print_words("""You leap over the pit to the left.""")
            room_2_right()
        elif "right" in action and "jump" in action:
            delayed_print_words("""You leap to the right as you smash into the wall.\nAs you impact the wall the cracks widen.""")
            room_2_right_wall_hp -= 1
            room_2_far_right()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("""You walk to the left and fall into the pit.""")
            in_pit()
        elif "right" in action:
            delayed_print_words("""You walk into the wall.""")
            room_2_far_right()
        elif "jump" in action:
            delayed_print_words("""You leap high into the air and land back where you leaped from.""")
            room_2_far_right()
        elif "attack" in action:
            delayed_print_words("""You swing your sword at the large wall\nAs you do the cracks in the wall widen.""")
            room_2_right_wall_hp -= 1
            room_2_far_right()
        else:
            exit_to_title()
    else:
        delayed_print_words("""You are in a large cavern\nUnlike the other caverns you’ve been in this one extremely well lit.\nMoon light is pouring in from a ginormous hole on the right side of the cavern.""")
        action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "right", "left", "jump", "attack", "exit"])
        if "jump" in action and "left" in action:
            delayed_print_words("""You leap over the pit to the left.""")
            room_2_right()
        elif "right" in action and "jump" in action:
            delayed_print_words("""You leap to the right out of the large hole in the wall.""")
            room_3_cliff()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("""You walk to the left and fall into the pit.""")
            in_pit()
        elif "right" in action:
            delayed_print_words("""You walk to the right out the hole in the wall.""")
            room_3_cliff()
        elif "jump" in action:
            delayed_print_words("""You leap high into the air and land back where you leaped from.""")
            room_2_far_right()
        elif "attack" in action:
            delayed_print_words("You swing your sword out in front of you.")
            room_2_far_right()
        else:
            exit_to_title()

def room_3_cliff():
    global current_room
    current_room = "room_3_cliff"

    delayed_print_words("""You stand at the edge of a cliffside.\nTo the right the earth has been broken away.\n Looking over the edge of the cliff you see a long way down the ground can be seen.\nOff in the distance a small town can be seen.""")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("""You leap into the cavern.""")
        room_2_far_right()
    elif "right" in action and "jump" in action:
        delayed_print_words("""You leap off the cliff.\nYou fall for a few seconds and land on the ground below.\nWeirdly you felt no pain when you impacted the ground.""")
        room_3_left()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("""You walk into the cavern.""")
        room_2_far_right()
    elif "right" in action:
        delayed_print_words("""You walk off the cliff.\nYou fall for a few seconds and land on the ground below.\nWeirdly you felt no pain when you impacted the ground.""")
        room_3_left()
    elif "jump" in action:
        delayed_print_words("""You leap high into the air and land back where you leaped from.""")
        room_3_cliff()
    elif "attack" in action:
        delayed_print_words("""You swing your sword out in front of you.""")
        room_3_cliff()
    else:
        exit_to_title()

def room_3_left():
    global current_room
    current_room = "room_3_left"

    delayed_print_words("""You are in a large barren flat piece of land, large chunks of the broken wall are scattered along the ground.\nThe moon shining down upon you.\nOff in the distance a small town can be seen.""")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("""You leap to the left as your face smashes against the wall.""")
        room_3_left()
    elif "right" in action and "jump" in action:
        delayed_print_words("""You leap to the right.""")
        room_3_left()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("""You walk into the wall.""")
        room_3_left()
    elif "right" in action:
        delayed_print_words("""You walk off in the direction of the town.\nAfter a long walk you finally enter the town.""")
        room_3_town()
    elif "jump" in action:
        delayed_print_words("""You leap high into the air and land back where you leaped from.""")
        room_3_left()
    elif "attack" in action:
        delayed_print_words("""You swing your sword out in front of you.""")
        room_3_left()
    else:
        exit_to_title()

def room_3_town():
    global current_room
    current_room = "room_3_town"

    delayed_print_words("""You are in a small town with unlit street lamps scattered about.\nLooking at all the houses you notice only one has light shining from within.""")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit", "go into", "enter", "house"])
    if "left" in action and "jump" in action:
        delayed_print_words("""You leap to the left.""")
        room_3_left()
    elif "right" in action and "jump" in action:
        delayed_print_words("""You leap to the right.""")
        room_3_left()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("""You walk off in the direction of the cliff.\nAfter a long walk you finally reach the cliffside.""")
        room_3_left()
    elif "right" in action:
        delayed_print_words("""You walk off to the right.\nAfter a long walk you see a large opened iron gateway.""")
        room_3_right()
    elif "jump" in action:
        delayed_print_words("""You leap high into the air and land back where you leaped from.""")
        room_3_town()
    elif "attack" in action:
        delayed_print_words("""You swing your sword out in front of you.""")
        room_3_town()
    elif "enter" in action or "go into" in action or "house" in action:
        delayed_print_words("""You go up to the one house with its lights on.\nYou go to check the door and notice it is unlocked.\nYou open the door and go into the house.""")
        npc_house()
    else:
        exit_to_title()

def npc_house():
    global npc_house_npc_killed
    global player_dmg
    global current_room
    current_room = "npc_house"
    if npc_house_npc_killed == False:
        delayed_print_words("""You are standing inside a small house with swords and armor hanging on the walls.\nTo the right you see an old man sitting in a chair.""")
        action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit", "talk", "speak"])
        if "left" in action and "jump" in action:
            delayed_print_words("""You leap to the left hitting your head on the ceiling of the house.""")
            npc_house()
        elif "right" in action and "jump" in action:
            delayed_print_words("""You leap to the right hitting your head on the ceiling of the house.""")
            npc_house()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("""You walk out the door of the house.""")
            room_3_town()
        elif "right" in action:
            delayed_print_words("""You walk to the right of the house.""")
            npc_house()
        elif "jump" in action:
            delayed_print_words("""You leap into the air hitting your head on the ceiling of the house.""")
            room_3_town()
        elif "attack" in action:
            delayed_print_words("""You swing your sword out at the old man, decapitating him.\nHis lifeless body falls to the ground.""")
            npc_house_npc_killed = True
            npc_house()
        elif "talk" in action or "speak" in action and player_dmg == 1:
            delayed_print_words("""You go up to the old man, as he sees you, he says\n\"Why hello there fella, haven’t seen many people around here in a while.\nThat monster has come by and killed all but me.\nI see you’ve got yourself a sword there\nYou wouldn’t happen to be going to slay that terrible beast, would ya?\nHmm the silent type ay.\nWell if you are, he stays at the edge of town, his lair lies behind a large iron gateway...\n Or so i have been told, i haven’t left my house in years.\nBack when i was younger i was a quite the fierce warrior, but now im just an old man.\nHere take this sword with ya, its much sharper than your own.\nShould help you make short work of the beast!\"""")
            player_dmg = 1.5
            npc_house()
        elif "talk" in action or "speak" in action:
            delayed_print_words("""You go up to the old man, he looks up and says to you\n\"I’m afraid i have nothing left to give ya.\nOnce that beast has been slain you are welcome to live here in the town.\nPlenty of places for you to choose from since he’s killed everyone other than me.\"""")
            npc_house()
        else:
            exit_to_title()
    else:
        delayed_print_words("""You are standing inside a small house with swords and armor hanging on the walls.\nTo the right you see the decapitated corpse of an old man laying on the floor.""")
        action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
        if "left" in action and "jump" in action:
            delayed_print_words("""You leap to the left hitting your head on the ceiling of the house.""")
            npc_house()
        elif "right" in action and "jump" in action:
            delayed_print_words("""You leap to the right hitting your head on the ceiling of the house.""")
            npc_house()
        elif "help" in action:
            available_commands()
        elif "left" in action:
            delayed_print_words("""You walk out the door of the house.""")
            room_3_town()
        elif "right" in action:
            delayed_print_words("""You walk to the right of the house.""")
            npc_house()
        elif "jump" in action:
            delayed_print_words("""You leap into the air hitting your head on the ceiling of the house.""")
            room_3_town()
        elif "attack" in action:
            delayed_print_words("""You swing your sword out in front of you.""")
            npc_house()
        else:
            exit_to_title()

def room_3_right():
    global current_room
    current_room = "room_3_right"

    delayed_print_words("""You see a large iron gateway\nWhat looks to be castle walls extend from the left and right side of the gateway.""")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("""You leap to the left.""")
        room_3_right()
    elif "right" in action and "jump" in action:
        delayed_print_words("""You leap to the right through the iron gateway.""")
        room_4_left()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("""You walk off to the left.\nAfter a long walk you finally reach the town.""")
        room_3_town()
    elif "right" in action:
        delayed_print_words("""You walk through the iron gateway""")
        room_4_left()
    elif "jump" in action:
        delayed_print_words("""You leap high into the air and land back where you leaped from.""")
        room_3_right()
    elif "attack" in action:
        delayed_print_words("""You swing your sword out in front of you.""")
        room_3_right()
    else:
        exit_to_title()

def room_4_left():
    global current_room
    current_room = "room_4_left"

    delayed_print_words("room 4 left description")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps to the left, goes to room 3 right")
        room_3_right()
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps slightly to the right, goes to room 4 left")
        room_4_left()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes to room 3 right")
        room_3_right()
    elif "right" in action:
        delayed_print_words("goes to room 4 boss room")
        room_4_boss_room()
    elif "jump" in action:
        delayed_print_words("jumps, goes to room 4 left")
        room_4_left()
    elif "attack" in action:
        delayed_print_words("swings nail, goes to room 4 left")
        room_4_left()
    else:
        exit_to_title()

def room_4_boss_room():
    global current_room
    current_room = "room_4_boss_room"

    delayed_print_words("room 4 boss room description")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps to the left, goes to room 4 boss room")
        room_4_boss_room()
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps slightly to the right, goes to room 4 boss room")
        room_4_boss_room()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes to room 4 left")
        room_4_left()
    elif "right" in action:
        delayed_print_words("goes to room 4 boss fight")
        room_4_boss_fight()
    elif "jump" in action:
        delayed_print_words("jumps, goes to room 4 boss room")
        room_4_boss_room()
    elif "attack" in action:
        delayed_print_words("swings nail, goes to room 4 boss room")
        room_4_boss_room()
    else:
        exit_to_title()

def room_4_boss_fight():
    delayed_print_words("boss fight starting description")
    boss_fight_players_turn_boss_right()

def boss_fight_players_turn_boss_right():
    global current_room
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    current_room = "boss_fight_players_turn_boss_right"

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        save_1 = open(f"saves\\save_1.txt", "w")
        save_1.write("Dead")
        save_1.close()
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen() 
    delayed_print_words("boss on right description")
    delayed_print_words(f"Your Hp: {player_hp}")
    action = valid_input("What would you like to do?", ["jump"and"left", "jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("goes to boss turn player on left")
        boss_fight_boss_turn_player_left()
    elif "right" in action and "jump" in action:
        delayed_print_words("takes 1 damage, goes to boss turn player on left")
        player_hp -= 1
        boss_fight_boss_turn_player_left()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes to boss turn player on left")
        boss_fight_boss_turn_player_left()
    elif "right" in action:
        delayed_print_words("takes 1 damage, goes to boss turn player on left")
        player_hp -= 1
        boss_fight_boss_turn_player_left()
    elif "jump" in action:
        delayed_print_words("goes to boss turn player on left")
        boss_fight_boss_turn_player_left()
    elif "attack" in action:
        delayed_print_words("boss takes player damage goes to boss turn player on left")
        boss_hp -= player_dmg
        boss_fight_boss_turn_player_left()
    else:
        exit_to_title()

def boss_fight_players_turn_boss_left():
    global current_room
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    current_room = "boss_fight_players_turn_boss_left"

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        save_1 = open(f"saves\\save_1.txt", "w")
        save_1.write("Dead")
        save_1.close()
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen()
    delayed_print_words("boss on left description")
    delayed_print_words(f"Reads Player Hp: {player_hp}")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("player takes 1 damage, goes to boss turn player right")
        player_hp -= 1
        boss_fight_boss_turn_player_right()
    elif "right" in action and "jump" in action:
        delayed_print_words("goes to boss turn player right")
        boss_fight_boss_turn_player_right()
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("player takes 1 damage, goes to boss turn player right")
        player_hp -= 1
        boss_fight_boss_turn_player_right()
    elif "right" in action:
        delayed_print_words("goes to boss turn player right")
        boss_fight_boss_turn_player_right()
    elif "jump" in action:
        delayed_print_words("goes to boss turn player right")
        boss_fight_boss_turn_player_right()
    elif "attack" in action:
        delayed_print_words("boss takes player damage goes to boss turn player on right")
        boss_hp -= player_dmg
        boss_fight_boss_turn_player_right()
    else:
        exit_to_title()

def boss_fight_boss_turn_player_left():
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    global dodged
    global player_reaction_move

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        save_1 = open(f"saves\\save_1.txt", "w")
        save_1.write("Dead")
        save_1.close()
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen()

    boss_move = random.choice(["Slam", "Jump Crush"])
    if boss_move == "Slam":
        delayed_print_words("boss winds up slam")
        dodged = boss_fight_player_reaction_boss_right()
        if dodged:
            boss_fight_players_turn_boss_right()
        else:
            player_hp -= 1
            boss_fight_players_turn_boss_right()
    else:
        delayed_print_words("boss jumps above player")
        dodged = boss_fight_player_reaction_boss_in_air()
        if dodged:
            if player_reaction_move == "left":
                boss_fight_players_turn_boss_right()
            elif player_reaction_move == "right":
                boss_fight_players_turn_boss_left()
            else:
                player_reaction_move = random.choice(["left", "right"])
                if player_reaction_move == "left":
                    boss_fight_players_turn_boss_right()
                else:
                    boss_fight_players_turn_boss_left()
        else:
            player_hp -= 1
            if player_reaction_move == "left":
                boss_fight_players_turn_boss_right()
            elif player_reaction_move == "right":
                boss_fight_players_turn_boss_left()
            else:
                player_reaction_move = random.choice(["left", "right"])
                if player_reaction_move == "left":
                    boss_fight_players_turn_boss_right()
                else:
                    boss_fight_players_turn_boss_left()

def boss_fight_boss_turn_player_right():
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    global dodged
    global player_reaction_move

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        save_1 = open(f"saves\\save_1.txt", "w")
        save_1.write("Dead")
        save_1.close()
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen()

    boss_move = random.choice(["Slam", "Jump Crush"])
    if boss_move == "Slam":
        delayed_print_words("boss winds up slam")
        dodged = boss_fight_player_reaction_boss_left()
        if dodged:
            boss_fight_players_turn_boss_left()
        else:
            player_hp -= 1
            boss_fight_players_turn_boss_left()
    else:
        delayed_print_words("boss jumps above player")
        dodged = boss_fight_player_reaction_boss_in_air()
        if dodged:
            if player_reaction_move == "left":
                boss_fight_players_turn_boss_right()
            elif player_reaction_move == "right":
                boss_fight_players_turn_boss_left()
            else:
                player_reaction_move = random.choice(["left", "right"])
                if player_reaction_move == "left":
                    boss_fight_players_turn_boss_right()
                else:
                    boss_fight_players_turn_boss_left()
        else:
            player_hp -= 1
            if player_reaction_move == "left":
                boss_fight_players_turn_boss_right()
            elif player_reaction_move == "right":
                boss_fight_players_turn_boss_left()
            else:
                player_reaction_move = random.choice(["left", "right"])
                if player_reaction_move == "left":
                    boss_fight_players_turn_boss_right()
                else:
                    boss_fight_players_turn_boss_left()

def boss_fight_player_reaction_boss_in_air():
    global current_room
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    global player_reaction_move
    current_room = "boss_fight_player_reaction_boss_in_air"

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        save_1 = open(f"saves\\save_1.txt", "w")
        save_1.write("Dead")
        save_1.close()
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen()
    delayed_print_words("boss in air description")
    delayed_print_words(f"Your Hp: {player_hp}")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps to the left")
        player_reaction_move = "left"
        return False
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps to the right")
        player_reaction_move = "right"
        return False
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes left")
        player_reaction_move = "left"
        return True
    elif "right" in action:
        delayed_print_words("goes right")
        player_reaction_move = "right"
        return True
    elif "jump" in action:
        delayed_print_words("jumps")
        player_reaction_move = "under"
        return False
    elif "attack" in action:
        delayed_print_words("attacks")
        boss_hp -= player_dmg
        player_reaction_move = "under"
        return False
    else:
        exit_to_title()

def boss_fight_player_reaction_boss_left():
    global current_room
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    current_room = "boss_fight_player_reaction_boss_left"

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        save_1 = open(f"saves\\save_1.txt", "w")
        save_1.write("Dead")
        save_1.close()
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen()
    delayed_print_words("boss on left winding up slam attack description")
    delayed_print_words(f"Your Hp: {player_hp}")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps to the left")
        return False
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps to the right")
        return True
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes left")
        return False
    elif "right" in action:
        delayed_print_words("goes right")
        return True
    elif "jump" in action:
        delayed_print_words("jumps")
        return False
    elif "attack" in action:
        delayed_print_words("attacks")
        boss_hp -= player_dmg
        return False
    else:
        exit_to_title()

def boss_fight_player_reaction_boss_right():
    global current_room
    global player_hp
    global player_dmg
    global boss_hp
    global player_move
    current_room = "boss_fight_player_reaction_boss_right"

    if player_hp <= 0:
        delayed_print_words("Describe Death and los, goes to title")
        save_1 = open(f"saves\\save_1.txt", "w")
        save_1.write("Dead")
        save_1.close()
        title_screen()
    elif boss_hp <= 0:
        delayed_print_words("Describe bosses death and win, goes to title")
        title_screen()
    delayed_print_words("boss on right winding up slam attack description")
    delayed_print_words(f"Your Hp: {player_hp}")
    action = valid_input("What would you like to do?", ["jump"and"left","jump"and"right", "help", "left", "right", "jump", "attack", "exit"])
    if "left" in action and "jump" in action:
        delayed_print_words("jumps to the left")
        return True
    elif "right" in action and "jump" in action:
        delayed_print_words("jumps to the right")
        return False
    elif "help" in action:
        available_commands()
    elif "left" in action:
        delayed_print_words("goes left")
        return True
    elif "right" in action:
        delayed_print_words("goes right")
        return False
    elif "jump" in action:
        delayed_print_words("jumps")
        return False
    elif "attack" in action:
        delayed_print_words("attacks")
        boss_hp -= player_dmg
        return False
    else:
        exit_to_title()

def start_game():
    delayed_print_words("reads intro")
    room_1()

title_screen()