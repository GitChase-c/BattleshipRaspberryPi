
import pyfiglet
import random, time
#deleted ship placement choice, added gamemode functions insdie main

def intro():
    print(pyfiglet.figlet_format("BATTLESHIP"))
    try:
        print("""
                                                                                                                                _.--"' |
                                                                                                                        _.--"'       |
                                                                                                                    _.--"'      _..,.  |
                                                                                                            _.--"'            .==; '.|
                                                                                                        _.--"'                     :   |'.
                                                                                                _.--"'                            ;  |  '.
                                                                                            _.--"'                                  :  |    '.
                                                                                    _.--"'                                         ; |      '.
                                                                                _.--"'                         _.                    : |        '.
                                                                        _.--"'                         _.--^"  :                   q I     --mmm--
                                                                    _.--"'                              ;      _,.;_                 |_I____._\___/___._.__
                                                            _.--"'                                    :_.--^"   :_]                |______|     ==" " "_|'
                                                    |__.--"'                                           ;         ;|                |;I H| |_______'(|)|
                                                .   | :                                                :     _   :|                |:I_H|_|______[ '._|    _.---.______
                                                I   | ;             ,    \                    \         ;__ [_]___;                |||____________| '_|    \|   ;""         |
                        ______.---._    ______ I  /|:        \     ;\    \                    \      ,d.-^'|| '-.b.     ___       L| I|  |"  |   |_[_|_X__[|___:_,.-^>_.---.______             /|
    ;                          "":"|'|/    _\--/  I_/_|;         \    :/\ __nm__                _nm   _d______||______b.__EEEE3       | I|__| m |___|__H_____|_ m__|'^|"  \|  ;""                //|
    ;      ______.---._<^-.,_____;___|]__\|____|_|I___|] .--_____nm____; |_dHH|_|.-           |dHH|_|,-======''==_===;===|====|______|_I|__|_W_|___|__H_____^__W__|__|____|___:___,.--._nnn__m__//_o
    :\         "":   |/ "|  |   __ m ___ .d88b. H m m || |_|-|-|-|-|-|-|  H*''|  .mmmmmmmmm^^" '|m[]H"m""""""|   |_| []  [_]   /*  *  * * * * *|_|'"7 | *  *   *   *   *  *  *  *  *  *     .V.    ;
    :_\__,.,_n_m_;___|]_I|_[|__[__]W_____'Y88P'_H_W_W_||_|_|_|_|_|_|_|_|__H&[]|_____^MMMM^______|W__H%$&$__I_____ -'________.-'                | | /  |                                    ^(8)-  ;
    |<    H  * * *  * *  * *  *  * *  * * * * * * * *  *  *  *  *  *   *   *  *  *  *                                                                                       *  *  *   *  *       :
    |  _|_H_|_                                           ___________________________________________________________________________________                 [KELLEN AND ALLIE]                 ;
    '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
    """)
    except ValueError:
        pass


    print("The computer will randomly generate a ship on the board, and your goal is to guess the right location.")
    input("Press enter to continue: ")
    

import time, os, random, pyfiglet, keyboard

rS = True
##Computer board function##
def createComputerBoard(lengthOfBoard, widthOfBoard):
    return [[' ' for _ in range(lengthOfBoard)] for _ in range(widthOfBoard)]

##Player board function##
def createPlayerBoard(lengthOfBoard, widthOfBoard):
    return [[' ' for _ in range(lengthOfBoard)] for _ in range(widthOfBoard)]

##Print Computer board##
def printComputerBoard(computerBoard, playerBoard):
    print("COMPUTER BOARD")
    size = len(playerBoard)
    # column_numbers = "    " + "   ".join([str(i + 1) for i in range(size)])
    for row in range(size):
        print(" +" + "---+" * size)  # Print the separator line
        print(" | " + " | ".join(computerBoard[row]) + " |")
    print(" +" + "---+" * size)

##print Player board##
def printPlayerBoard(playerBoard):
    print("PLAYER BOARD")
    size = len(playerBoard)
    # column_numbers = "    " + "   ".join([str(i + 1) for i in range(size)])
    for row in range(size):
        print(" +" + "---+" * size)  # Print the separator line
        print(" | " + " | ".join(playerBoard[row]) + " |")
    print(" +" + "---+" * size)

def nameShips():
    print("Would you like to name your ships?\n    [y] = YES\n    [n] = NO")
    while True:
        #Name first ship
        if keyboard.is_pressed('y'):
            x = input("Please name your carrier:\n    ")
            carrierName = x.strip()
            print(f"    Welcome to the fleet {carrierName}")
            time.sleep(1)
            os.system('cls')

        #Name second ship   
            x = input("Please name your cruiser:\n    ")
            cruiserName = x.strip()
            print(f"    Welcome to the fleet {cruiserName}")
            time.sleep(1)
            os.system('cls')
            break
        #Auto name pick
        if keyboard.is_pressed('n'):
            carrierName = "SS Silly Sailor"
            cruiserName = "USS Laughing Seagull"
            break

    return carrierName, cruiserName

###Place ships on board###
def placeShips(playerBoard):
    Size = 10
    placements = 0
    while placements == 0:
        print("SHIP CONTROLS:\n    [w] = UP\n    [s] = DOWN\n    [a] = LEFT\n    [d] = RIGHT\n    [q] = ROTATE LEFT\n    [e] = ROTATE RIGHT\n[enter] = PLACE SHIP\n  [esc] = QUIT")
        # placements += 1
        break

    playerShips = []
    for i in range(2):
        startPos = Size - Size//2
        curPosX = startPos
        curPosY = startPos
        shipLength = 2
        for j in range(shipLength):
            playerBoard[curPosX + j][curPosY] = "X"
        printPlayerBoard(playerBoard)

        while True:
            try:
                
                x = 1
                moved = False
                if keyboard.is_pressed('a') and curPosY > 0:
                    projectedMove = playerBoard[curPosX + x][curPosY]
                    moved = True
                    for x in range(shipLength):
                        playerBoard[curPosX + x][curPosY] = " "
                    curPosY -= 1
                    for x in range(shipLength):
                        playerBoard[curPosX + x][curPosY] = "X"
                        os.system('cls')
                if keyboard.is_pressed('d'):
                    moved = True
                    for x in range(shipLength):
                        playerBoard[curPosX + x][curPosY] = " "
                    curPosY += 1
                    for x in range(shipLength):
                        playerBoard[curPosX + x][curPosY] = "X"
                        os.system('cls')
                if keyboard.is_pressed('w') and curPosX > 0:
                    moved = True
                    for x in range(shipLength):
                        playerBoard[curPosX + x][curPosY] = " "
                    curPosX -= 1
                    for x in range(shipLength):
                        playerBoard[curPosX + x][curPosY] = "X"
                        os.system('cls')
                if keyboard.is_pressed('s'):
                    moved = True
                    for x in range(shipLength):
                        playerBoard[curPosX + x][curPosY] = " "
                    curPosX += 1
                    for x in range(shipLength):
                        playerBoard[curPosX + x][curPosY] = "X"
                        os.system('cls')
                if keyboard.is_pressed('enter'):
                    os.system('cls')
                    input(" ")
                    os.system('cls')
                    print("Ship Placed")
                    printPlayerBoard(playerBoard)
                    time.sleep(1.5)
                    keyboard.unhook_all
                    os.system('cls')
                    playerShips.append(curPosY + 1)
                    playerShips.append(curPosX + 1)
                    playerShips.append(curPosY + 1)
                    playerShips.append(curPosX + 2)
                    break
                if moved:
                    printPlayerBoard(playerBoard)
                    time.sleep(.2)
                    keyboard.unhook_all
                if not moved:
                    continue
            except ValueError:
                print("Nope")
    print(playerShips)
    return playerShips

####Player shot Function ####
def player(computerBoard, lengthOfBoard, widthOfBoard, playerShotCoordinates):
    while True:
        while True:
            try:
                #X coordinates
                movex = int(input("Pick X coordinate for shot: "))
                if movex > widthOfBoard or movex < 1:
                    print("Your out of range!")
                    continue
                else:
                    movex -=1
                    break
            except ValueError:
                print("Invalid Input")
                continue
        
        while True:
            #Y coordinates
            try:
                movey = int(input("Pick Y coordinate for shot: "))
                if movey > lengthOfBoard or movey < 1:
                    print("Your out of range!")
                    continue
                else:
                    movey -= 1
                    break
            except ValueError:
                print("Invalid Input")
                continue
        
        if computerBoard[movex][movey] != " ":
            print("\nSpot already taken, please try again\n")
            continue
        else:
            break

    computerBoard[movey][movex] = "O" 
    main_move = [movey, movex]

#Updates the list of shots
    playerShotCoordinates.append(main_move)
#Prints the coordinates (does not print them on the board) and the updated list
    return playerShotCoordinates
    
    
####Computer ship location###
def createComputerShipLocation(widthOfBoard, lengthOfBoard):
    #Ship 1
    computerShipX1 = random.randint(2, widthOfBoard)
    computerShipY1 = random.randint(2, lengthOfBoard)
    computership1 = [computerShipX1, computerShipY1]

    lay = random.randint(1,2)
    if lay ==1: 
        computerShipX1= computerShipX1 -1
        computership1.extend([computerShipX1, computerShipY1])
    else:
        computerShipY1 = computerShipY1 - 1
        computership1.extend([computerShipX1,computerShipY1])
    computerShipLocation1 = [computerShipX1, computerShipY1]
    computerShipLocationPrintable1 = [computerShipX1, computerShipY1]
        
    #Ship 2
    computerShipX2 = random.randint(2, widthOfBoard)
    computerShipY2 = random.randint(2, lengthOfBoard)
    computerShip2 = [computerShipX2, computerShipY2]
    lay = random.randint(1,2)
    if lay == 1 :
        computerShipX2 = computerShipX2 - 1 
        computerShip2.extend([computerShipX2, computerShipY2])
    
    else:
        computerShipY2 = computerShipY2 - 1
        computerShip2.extend([computerShipX2, computerShipY2])
    computerShipLocation2 = [computerShipX2, computerShipY2]
    computerShipLocationPrintable2 = [computerShipX2, computerShipY2]
    return computership1, computerShip2

 #Stores the Computer ships in a dicionary
    computerShips = {
                     "computerShip1": computerShipLocation1,
                     "computerShip2": computerShipLocation2,
                     }
    return computership1, computerShip2, computerShipLocationPrintable1, computerShipLocationPrintable2
    

computerShotCoordinates = []

####Computer shots ####    
def computer(playerBoard, lengthOfBoard, widthOfBoard):
    restart = True
    while(restart):
        computerMoveX = random.randint(1, widthOfBoard - 1)
        computerMoveY = random.randint(1, lengthOfBoard - 1)
        if playerBoard[computerMoveX][computerMoveY] not in [" ", "X"]:
            continue
        else:
            playerBoard[computerMoveX][computerMoveY] = "O"
            restart = False
    computerMainMove = [computerMoveY + 1, computerMoveX + 1]
    print(f"Computer's shot: {computerMainMove}")
    computerShotCoordinates.append(computerMainMove)
    print(computerShotCoordinates)
    printPlayerBoard(playerBoard)
    return computerShotCoordinates, computerMoveX, computerMoveY

####Player win####
def checkIfWin(computerShipLocation1, computerShipLocation2, playerShotCoordinates, computerBoard):
    movex = computerShipLocation1[0]
    movey = computerShipLocation1[1]
    move1x= computerShipLocation1[2]
    move1y = computerShipLocation1[3]
    compshiplist1= [movey - 1, movex - 1]
    compshiplist2= [move1y -1, move1x -1]
    move2x = computerShipLocation2[0]
    move2y = computerShipLocation2[1]
    move3x= computerShipLocation2[2]
    move3y = computerShipLocation2[3]
    compshiplist3= [move2y -1, move2x -1]
    compshiplist4= [move3y -1, move3x -1]
    print("test ", compshiplist1, compshiplist2, "\nplayer shots: ", playerShotCoordinates)
    output= False
    shiphitcount = 0
#Computer ship 1
    if  compshiplist1 in playerShotCoordinates:
        computerBoard[compshiplist1[0]][compshiplist1[1]] = "🔥" 
        print(f"Hit! Your opponents ship was at: {compshiplist1}")
        #printComputerBoard(computerBoard)
        shiphitcount = shiphitcount + 1
        output = True
    if  compshiplist2 in playerShotCoordinates:
        computerBoard[compshiplist2[0]][compshiplist2[1]]= "🔥" 
        print(f"Hit! Your opponents ship was at: {compshiplist2}")
        #printComputerBoard(computerBoard)
        shiphitcount = shiphitcount + 1
        output = True
#computer ship 2
    if compshiplist3 in playerShotCoordinates:
        computerBoard[compshiplist3[0]][compshiplist3[1]]= "🔥" 
        print(f"Hit! Your opponents ship was at: {compshiplist3}")
        #printComputerBoard(computerBoard)
        shiphitcount = shiphitcount + 1
        output = True
    if compshiplist4 in playerShotCoordinates:
        computerBoard[compshiplist4[0]][compshiplist4[1]] = "🔥" 
        print(f"Hit! Your opponents ship was at: {compshiplist4}")
        #printComputerBoard(computerBoard)
        shiphitcount = shiphitcount + 1
        output = True
    if shiphitcount == 4:
        print("You Win!")
        quit()
    return output


####Computer Win Function####
def checkComputerWin(playerships,playerBoard,computerShotCoordinates):
    ship1 = [playerships[0], playerships[1]]
    ship2 = [playerships[2], playerships[3]]
    ship3 = [playerships[4], playerships[5]]
    ship4 = [playerships[6], playerships[7]]
    print("player ships: ", ship1, ship2, ship3, ship4)
    output= False
    computershiphitcount = 0
    ##ship 1##
    if ship1 in computerShotCoordinates:
        playerBoard[ship1[1] - 1][ship1[0] - 1] = "🔥" 
        print(f"Hit! Your opponents ship was at: {ship1}")
        computershiphitcount = computershiphitcount + 1
        output = True
    if ship2 in computerShotCoordinates:
        playerBoard[ship2[1] - 1][ship2[0] - 1] = "🔥" 
        print(f"Hit! Your opponents ship was at: {ship2}")
        computershiphitcount = computershiphitcount + 1
        output = True

    ##ship 2 ##
    if ship3 in computerShotCoordinates:
        playerBoard[ship3[1] - 1][ship3[0] - 1] = "🔥" 
        print(f"Hit! Your opponents ship was at: {ship3}")
        computershiphitcount = computershiphitcount + 1
        output = True
    if ship4 in computerShotCoordinates:
        playerBoard[ship4[1] - 1][ship4[0] - 1] = "🔥" 
        print(f"Hit! Your opponents ship was at: {ship4}")
        computershiphitcount = computershiphitcount + 1
        output = True

    if computershiphitcount == 4:
        print("You Win!")
        quit()
    return output
    
####Main Function####
def main():
    lengthOfBoard, widthOfBoard = 10, 10
    nameShips()
    playerBoard = createPlayerBoard(lengthOfBoard, widthOfBoard)
    computerBoard = createComputerBoard(lengthOfBoard, widthOfBoard)
    playerships = placeShips(playerBoard)
    printComputerBoard(computerBoard, playerBoard)
    printPlayerBoard(playerBoard)
    ship1, ship2 = createComputerShipLocation(widthOfBoard, lengthOfBoard)
    playerShotCoordinates = []
    while True:
        print("computer ships: ", ship1, ship2)
        computer(playerBoard, lengthOfBoard, widthOfBoard)
        player(computerBoard, lengthOfBoard, widthOfBoard, playerShotCoordinates)
        checkIfWin(ship1, ship2, playerShotCoordinates, computerBoard)
        checkComputerWin(playerships,playerBoard,computerShotCoordinates)
        printPlayerBoard(playerBoard)
        printComputerBoard(computerBoard, playerBoard)
main()
