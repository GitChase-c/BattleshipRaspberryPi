import random
import time
import keyboard
import os
import msvcrt




def clear_keyboard():
    while msvcrt.kbhit():
        msvcrt.getch()


#generates board of selected size
def create_board(board_size):
    #dynamiclly sizes board
    board = []
    for row in range(board_size):
        board.append([])
        for column in range(board_size):
            board[row].append("0")
    return board


#displays the board
def display(board):
    print("\033[2J\033[H")
    for row in range(len(board)):
        for column in range(len(board)):
            # paints misses red
            if board[row][column] == "M":
                print("\x1B[31m", end="")
                if column == 0:
                    print("|", end="")
                    print(board[row][column],end="|")
                else:
                    print(board[row][column], end="|")
                print("\x1B[0m", end="")
            # paints hits green
            elif board[row][column] == "H":
                print("\x1B[32m", end="")
                if column == 0:
                    print("|", end="")
                    print(board[row][column],end="|")
                else:
                    print(board[row][column], end ="|")
                print("\x1B[0m", end="")
            # paints ships blue
            elif board[row][column] == "S":
                print("\x1B[46m", end="")
                if column == 0:
                    print("|", end="")
                    print(board[row][column],end="|")
                else:
                    print(board[row][column], end ="|")
                print("\x1B[0m", end="")
            elif board[row][column] == "P":
                print("\x1B[43m", end="")
                if column == 0:
                    print("|", end="")
                    print(board[row][column],end="|")
                else:
                    print(board[row][column], end ="|")
                print("\x1B[0m", end="")
            elif board[row][column] == "I":
                print("\x1B[41m", end="")
                if column == 0:
                    print("|", end="")
                    print(board[row][column],end="|")
                else:
                    print(board[row][column], end ="|")
                print("\x1B[0m", end="")
            # fills in sank ships
            elif board[row][column] == "-":
                print("\x1B[42m", end="")
                if column == 0:
                    print("|", end="")
                    print(board[row][column],end="|")
                else:
                    print(board[row][column], end ="|")
                print("\x1B[0m", end="")
            else:
                print("\x1B[0m", end="")
                if column == 0:
                    print("|", end="")
                    print(board[row][column],end="|")
                else:
                    print(board[row][column], end ="|")
        print("\n"+"— "*(len(board)+1))
       
def generate_ship(computer,board,num_ships, location = None, horizontal = None, ship_size = None):
    clear_keyboard()
    board_size = len(board)
    # types of ships
    ship_types = {"patrol":2,"gunboat":3,"submarine":3,"destroyer":4,"carrier":5}
    # sub-optimal method to limit the amount of ships based on board size
    for i in range(5-board_size):
       ship_types.pop(list(ship_types.keys())[-1])
    # sub-optimal method to keep track of possible ship locations
    possible_roots = []
    for i in range(board_size):
        for j in range(board_size):
            possible_roots.append([i,j])
    # branch to preform automatic or manual generation
    if computer:
        #swap_seqeunce(1,"PLACE")
        computer_ships = {}
        # create a list of already used points
        forbidden_roots = []
        for current_ship in range(num_ships):
            #randomizing the oreintation and size of a particular ship
            orientation = random.randint(0,1)
            gen_ship_type = random.sample(list(ship_types.keys()),1)[0]
            gen_ship_size = int(ship_types[gen_ship_type])
            gen_ship = []
            invalid_ship = True
            while invalid_ship:
                if orientation == 0: # horizontal
                    gen_ship_root = [random.randint(0,board_size-1),random.randint(0,board_size-gen_ship_size)]
                    for i in range(gen_ship_size):
                        gen_ship.append([gen_ship_root[0],gen_ship_root[1]+i])
                    if not False in [x not in forbidden_roots for x in gen_ship]:    
                        forbidden_roots.extend(gen_ship)
                        invalid_ship = False
                    else:
                        gen_ship = []
                        invalid_ship = True
                elif orientation == 1: # vertical
                    gen_ship_root = [random.randint(0,board_size-gen_ship_size),random.randint(0,board_size-1)]
                    for i in range(gen_ship_size):
                        gen_ship.append([gen_ship_root[0]+i,gen_ship_root[1]])
                    if not False in [x not in forbidden_roots for x in gen_ship]:  
                        forbidden_roots.extend(gen_ship)
                        invalid_ship = False
                    else:
                        gen_ship = []
                        invalid_ship = True
            ship_types.pop(gen_ship_type)
            computer_ships.update({f"ship: {current_ship+1}": gen_ship})
        print(computer_ships)
        return computer_ships


    elif not computer:
        gen_ship =[]
        if location[0] > board_size-1:
            location[0] -=1
        if location[0]< 0:
            location[0] +=1
        #preventing out of bounds for orientation
        if horizontal:
            if location[1] + ship_size > board_size:
                location[1] -=1
        elif not horizontal:
            if location[0] + ship_size > board_size:
                location[0] -=1
        #preventing out of bounds for column        
        if location[1] > board_size-1:
            location[1] -=1
        if location[1] <0:
            location[1] +=1



        # displaying new
        if horizontal:
            try:
                for i in range(ship_size):
                    board[abs(location[0])][location[1]+i] ="P"
                    gen_ship.append([location[0],location[1]+i])
            except(IndexError):
                location[1]=board_size-ship_size
                board[abs(location[0])][location[1]]="P"
        elif not horizontal:
            try:
                for i in range(ship_size):
                    board[location[0]+i][location[1]] ="P"
                    gen_ship.append([location[0]+i,location[1]])
            except(IndexError):
                location[0]=board_size-ship_size
                board[abs(location[0])][location[1]]="P"
        return gen_ship
                    
            

# get a guess
def generate_guess(computer,board, previous_guesses):
        board_size = len(board)
        computer_turn=True
        human_turn=True
        if(computer):
            while computer_turn:
                    strike = [random.randint(0, board_size-1), random.randint(0, board_size-1)]
                    if strike not in previous_guesses:
                        previous_guesses.append(strike)
                    return strike
        while human_turn:
            display(board)
            try:
                strike = input(f"Please input the location you would like to guess, with Rows A-{chr(board_size+64)} and Columns 1-{board_size} (Example: A,1) ").lower().split(",")
                strike[0], strike[1] = strike[0].strip(), strike[1].strip()
                # input validation, checks for out of bounds index of row and col
                if len(strike) != 2 or not strike[0].isalpha() or ord(strike[0]) -97 > board_size-1 or int(strike[1]) > board_size or int(strike[1]) < 1 :
                    raise ValueError
                strike[0], strike[1] = ord(strike[0]) -97, int(strike[1]) -1
                #checks if guess has already been made before
                if strike in previous_guesses:
                    print("You have already been here soldier", end = "\r")
                    time.sleep(.7)
                    continue
                # adds guess to list of previous guesses
                previous_guesses.append(strike)
                human_turn=False
                return strike
            except (ValueError,IndexError):
                if ValueError or IndexError:
                    print(f"invaild coordinates, Matey. Input coordnates in format A,3. Coordnates must also be in bounds of a {board_size}x{board_size} board")
                    time.sleep(.7)
               
# check if a guess is a hit or a  miss
def check_guess(strike, ships, board, previous_guesses):
    ships_list = list(ships.values())
    unpacked_ships = [x for ship in ships_list for x in ship]
    if strike in unpacked_ships:
        for i in range(len(ships)):
            if all(e in previous_guesses for e in ships_list[i]):
                print("Ship has been sunk!!")
                for piece in ships[f"ship: {i +1}"]:
                    board[piece[0]][piece[1]] = "-"
                return 2
        board[strike[0]][strike[1]] = "H"
        return 1
    else:
        board[strike[0]][strike[1]] = "M"
        return 0


#creates keyboard accessable menus
def keyboard_selection(iterable= None, reserved_keys= None, switch= None):
    i = 0
    y = 0
    key = ""
    clear_keyboard()
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
        if iterable:
            statment = ""
            for iter in range(len(iterable)):
                if iter == i:
                    statment += f">{str(iterable[iter])}<"
                else:
                    statment += str(iterable[iter])
                statment += "  "
            print(statment, end = "\r")
            if key == reserved_keys[0]:
                if i > 0:
                    i -=1
                    iterable[i] = f">{iterable[i]}<"
                    print(*iterable, sep="  ",end="\r")
                    try:
                        iterable[i]= int(str(iterable[i])[1:str(iterable[i]).index("<")])
                    except ValueError:
                        iterable[i]=str(iterable[i])[1:str(iterable[i]).index("<")]
            elif key == reserved_keys[1]:
                if i < len(iterable) -1:
                    i+= 1
                    iterable[i] = f">{iterable[i]}<"
                    print(*iterable, sep="  ",end="\r")
                    try:
                        iterable[i]= int(str(iterable[i])[1:str(iterable[i]).index("<")])
                    except ValueError:
                        iterable[i]=str(iterable[i])[1:str(iterable[i]).index("<")]
            elif key == reserved_keys[2]:
                print("\033[2J\033[H", end="")
                clear_keyboard()
                return(iterable[i])
            time.sleep(.15)
        else:
            submit = True # still selecting
            if key == reserved_keys[0]:
                    i-=1
            if key == reserved_keys[1]:
                    i+= 1
            if key == reserved_keys[2]:
                    y-=1
            if key == reserved_keys[3]:
                    y+=1
            if key == reserved_keys[4]:
                switch = not switch
            if key == reserved_keys[5]:
                submit = False
            clear_keyboard()
            return[i,y], switch, submit

    
   
# main game loop, combines all the functions into a playable game
def repeat_game(player_turn):
    if player_turn:
        print("Congrats Player 1! You win")
    else:
        print("Congrats Player 2! You win")
    invalid_input = True
    while invalid_input:
        invalid_input = False
        playing = input("Would you like to play again? ").lower().strip()
        if playing == "yes":
            return True
        elif playing == "no":
            return False
        else:
            invalid_input = True
            print("Please enter yes or no", end="\r")
            time.sleep(1.7)
def main ():
    playing = True
    while playing:
        previous_guesses_1, previous_guesses_2 = [], []
        print("Welcome to battle ship", end="\r" )
        time.sleep(1.5)
        print("Select your game mode ")
        computer = keyboard_selection(iterable = ["Singleplayer"], reserved_keys=["left","right","enter"])
        size = 10
        number_of_ships = 2

        # First Player's boards and ships (first player will always be human)
        board_1 = create_board(size)
        ships_1 = {}
        for ship in range(2):
            placing_ship = True
            location = [0,0]
            horizontal = True
            while placing_ship:
                gen_ship = generate_ship(False, board_1, number_of_ships, location, horizontal, 2)
                display(board_1)
                location_changes,horizontal, placing_ship = keyboard_selection(reserved_keys=["left", "right","down","up","r","enter"], switch=horizontal)
                location[0] -= location_changes[1]
                location[1] += location_changes[0]
                gen_ship = generate_ship(False,board_1, number_of_ships, location,horizontal,2)
                if placing_ship == False:
                    ships_1.update({ship: gen_ship})
                display(board_1)
                for i in range(size):
                        for j in range(size):
                            board_1[i][j] = 0
                for i in range(len(ships_1)):
                    for j in range(len(ships_1[i])):
                        board_1[ships_1[i][j][0]][ships_1[i][j][1]] ="S"


                
        for row in range(size):
                for column in range(size):
                    board_1[row][column] = 0
        # Second Player's boards and ships
        board_2= create_board(size)
        ships_2 = generate_ship(computer,board_1, number_of_ships)

        display(board_2)
        not_a_miss=True
        sink_count = 0
        while not_a_miss:
            clear_keyboard()
            player_turn=False
            while(not player_turn):
                print("Player 2 turn")
                time.sleep(1.5)
                strike = generate_guess(computer,board_1,previous_guesses_1)
                hit= check_guess(strike,ships_1, board_1,previous_guesses_1)
                display(board_1)
                time.sleep(1.3)
                if hit == 0:
                        player_turn=True
                elif hit == 2:
                    sink_count +=1
                    if sink_count == number_of_ships:
                        break
               
            while(player_turn):
                    print("Player 1 turn")
                    time.sleep(1.5)
                    strike=generate_guess(False,board_2,previous_guesses_2)
                    hit=check_guess(strike,ships_2,board_2,previous_guesses_2)
                    display(board_2)
                    time.sleep(1.2)
                    if hit == 0:
                        player_turn=False
                    elif hit == 2:
                        sink_count +=1
                        if sink_count == number_of_ships:
                            break
           
            if sink_count == number_of_ships:
                playing = repeat_game(player_turn)
                break
           #Its Done
main()