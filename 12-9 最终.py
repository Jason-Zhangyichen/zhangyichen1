#21207360 JASON
def build_board():
    board=[]
    # This is a map formed by a 9*9 list, the actual requirement is 8*8 table, this is the first map!
# First, he is placing warships for player 1 and providing him with a display.
# Secondly, he will record player 1's placement data to provide a judgment basis for player 2's hitting.
# will never be changed by a 2 hit
#！！！！！ For each map, a corresponding function should be defined below for easy operation
    for x in range(9):
        board.append(['-']*9)

    board[1][0]="A"
    board[2][0]="B"
    board[3][0]="C"
    board[4][0]="D"
    board[5][0]="E"
    board[6][0]="F"
    board[7][0]="G"
    board[8][0]="H"
    Y=1
    for z in range (0,9):
        if z==1 or z==2 or z==3 or z==4 or z==5 or z==6 or z==7 or z==8 or z==9:
            board[0][z]=str(Y)
            Y+=1
    return board




dict1=dict({"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8})
dict2=dict({"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8})
dict3=dict({"H":1,"V":2})
# This is a dictionary, a common tool. Convert user input into an index. 1 is horizontal, 2 is vertical        
        
            


board=build_board()
# show p1 where to put , no evidence for the second shot
board2=build_board()
# show p2 where to put, give 1 hit no basis
board3=build_board()
# show p1 X or M
board4=build_board()
# show p2 X or M
board5=build_board()
# store the 5 ship positions of p1, they don't need to be shown, they just keep score silently, more like a pure list than a map
board6=build_board()
# store the 4 ship positions of p1
board7=build_board()
# store the 3 ship positions of p1
board8=build_board()
# store the 2 ship positions of p1
board9=build_board()
# store the 5 ship positions of p2
board10=build_board()
# store the 4 ship positions of p2
board11=build_board()
# store the 3 ship positions of p2
board12=build_board()
# store the 2 ship positions of p2


def print_board(board):
    for row in board:
        print(' '.join(row))
def print_board2(board2):
    for row in board2:
        print(' '.join(row))
def print_board3(board3):
    for row in board3:
        print(' '.join(row))
def print_board4(board4):
    for row in board4:
        print(' '.join(row))
#Present the current board to the user



# position warships, I just add size under each input (is a child of the position function)
size=0
def determine_direction():
    str1=location11[0]
    str2=location11[1]
    str3=location11[2]
    num1=dict1[str1]
    num2=dict2[str2]
    num3=dict3[str3]
    if num3==1:
        for i in range(size):
            board[num1][num2]="s"
            if size==5:
                board5[num1][num2]="r"
            if size==4:
                board6[num1][num2]="r"
            if size==3:
                board7[num1][num2]="r"
            if size==2:
                board8[num1][num2]="r"
                
            num2=num2+1
    if num3==2:
        for i in range(size):
            board[num1][num2]="s"
            if size==5:
                board5[num1][num2]="r"
            if size==4:
                board6[num1][num2]="r"
            if size==3:
                board7[num1][num2]="r"
            if size==2:
                board8[num1][num2]="r"
            num1=num1+1
    print_board(board)

# Player 1 swing warship function, lose a swing warship map display, which does not include the input action!
size=0
def determine_direction2():
    str1=location12[0]
    str2=location12[1]
    str3=location12[2]
    num1=dict1[str1]
    num2=dict2[str2]
    num3=dict3[str3]
    if num3==1:
        for i in range(size):
            board2[num1][num2]="s"
            if size==5:
                board9[num1][num2]="r"
            if size==4:
                board10[num1][num2]="r"
            if size==3:
                board11[num1][num2]="r"
            if size==2:
                board12[num1][num2]="r"
            num2=num2+1
    if num3==2:
        for i in range(size):
            board2[num1][num2]="s"
            if size==5:
                board9[num1][num2]="r"
            if size==4:
                board10[num1][num2]="r"
            if size==3:
                board11[num1][num2]="r"
            if size==2:
                board12[num1][num2]="r"
            num1=num1+1
    print_board2(board2)
#Player 2's swing battleship function


def check_input():
    if len(location11) !=3:
        return False
    elif location11[0] not in "ABCDEFGH":
        return False
    elif location11[1]not in "12345678":
        return False
    elif location11[2] not in "VH":
        return False
    else:
        return True
def check_input2():
    if len(location12) !=3:
        return False
    elif location12[0] not in "ABCDEFGH":
        return False
    elif location12[1]not in "12345678":
        return False
    elif location12[2] not in "VH":
        return False
    else:
        return True    
#Verify that the player input is formatted correctly




print('******Start《Battleships》Game******')


name1=input("***please input your name：")
print("***Hello commander",name1,"!!!")
print_board(board)
# start game




location11=input("***Please enter the coordinates and direction for the Carrier，which will take 5 grid squares: ")
#Player 1 swings the battleship


size=5  
while True:
    if check_input()==True:
        size=size
        determine_direction()
        break
    if check_input()==False:
        print("***Ship not placed , the location you entered could not be recognised")
        location11=input("***Please enter the coordinates and direction for the Carrier，which will take 5 grid squares: ")

# If the player returns to re-lose with the wrong format
# map will appear once after placing 5 tiles.


location11=input("***Please enter the coordinates and direction for the Battleship ，which will take 4 grid squares: ")

size=4
while True:
    if check_input()==True:
        size=size
        determine_direction()
        break
    if check_input()==False:
        print("***Ship not placed , the location you entered could not be recognised")
        location11=input("***Please enter the coordinates and direction for the Carrier，which will take 4 grid squares: ")
# If the player returns to re-lose with the wrong format
# map will appear once after placing 4 tiles.


location11=input("***Please enter the coordinates and direction for the Destroyer ，which will take 3 grid squares: ")

size=3
while True:
    if check_input()==True:
        size=size
        determine_direction()
        break
    if check_input()==False:
        print("***Ship not placed , the location you entered could not be recognised")
        location11=input("***Please enter the coordinates and direction for the Carrier，which will take 3 grid squares: ")
# If the player returns to re-lose with the wrong format
# map will appear once after placing 3 tiles.


location11=input("***Please enter the coordinates and direction for the Submarine，which will take 2 grid squares: ")

size=2
while True:
    if check_input()==True:
        size=size
        determine_direction()
        break
    if check_input()==False:
        print("***Ship not placed , the location you entered could not be recognised")
        location11=input("***Please enter the coordinates and direction for the Carrier，which will take 2 grid squares: ")
# If the player returns to re-lose with the wrong format
# map will appear once after placing 2 tiles.


print("******Is time to change the player!!!******")
name2=input("***please input your name：")
print("***Hello commander",name2,"!!!")
print_board2(board2)



location12=input("***Please enter the coordinates and direction for the Carrier，which will take 5 grid squares: ")
#Player 2 swings the battleship
size=5
while True:
    if check_input2()==True:
        size=size
        determine_direction2()
        break
    if check_input2()==False:
        print("***Ship not placed , the location you entered could not be recognised")
        location12=input("***Please enter the coordinates and direction for the Carrier，which will take 5 grid squares: ")
# If the player returns to re-lose with the wrong format
# map will appear once after placing 5 tiles.




location12=input("***Please enter the coordinates and direction for the Battleship ，which will take 4 grid squares: ")

size=4
while True:
    if check_input2()==True:
        size=size
        determine_direction2()
        break
    if check_input2()==False:
        print("***Ship not placed , the location you entered could not be recognised")
        location12=input("***Please enter the coordinates and direction for the Carrier，which will take 4 grid squares: ")
# If the player returns to re-lose with the wrong format
# map will appear once after placing 4 tiles.



location12=input("***Please enter the coordinates and direction for the Destroyer ，which will take 3 grid squares: ")

size=3
while True:
    if check_input2()==True:
        size=size
        determine_direction2()
        break
    if check_input2()==False:
        print("***Ship not placed , the location you entered could not be recognised")
        location12=input("***Please enter the coordinates and direction for the Carrier，which will take 3 grid squares: ")
# If the player returns to re-lose with the wrong format
# map will appear once after placing 3 tiles.



location12=input("***Please enter the coordinates and direction for the Submarine，which will take 2 grid squares: ")

size=2
while True:
    if check_input2()==True:
        size=size
        determine_direction2()
        break
    if check_input2()==False:
        print("***Ship not placed , the location you entered could not be recognised")
        location12=input("***Please enter the coordinates and direction for the Carrier，which will take 2 grid squares: ")

# If the player returns to re-lose with the wrong format
# map will appear once after placing 2 tiles.



print('******It is time to hit******')
print("Hittes will be shown as 'X'on the board")
print ("Misses will be shown as 'M' on the board")
#Began to hit


#1选一个位置，看看2表上该位置元素是不是“s”，若是则在两个新的空表上打X（命中），实际跟本不在上面两个表操作，只是判定(hard to translate)
print("***1ST PLAYER is your trun")
print_board3(board3)
hit11=input("***1ST PLAYER Enter the coordinate you would like to hit: ")

def check2_input():
    if len(hit11) !=2:
        return False
    elif hit11[0] not in "ABCDEFGH":
        return False
    elif hit11[1]not in "12345678":
        return False
    else:
        return True
def hit_direction():
    str1=hit11[0]
    str2=hit11[1]
    num1=dict1[str1]
    num2=dict2[str2]
    if board2[num1][num2]=='s':
        board3[num1][num2]='X'
        board9[num1][num2]="-"
        board10[num1][num2]="-"
        board11[num1][num2]="-"
        board12[num1][num2]="-"
        print("***!!!good shot!!!")
       
    if board2[num1][num2]=="-":
        board3[num1][num2]="M"
        print("***!!!u miss!!!")
        
    print_board3(board3)
while True:
    if check2_input()==True:
        hit_direction()
        break
    if check2_input()==False:
        print("The coordinates you entered could not be recognised , please try again")
        hit11=input("***1ST PLAYER Enter the coordinate you would like to hit: ")
        
#玩家2
print('***2ND PLAYER is your trun')
print_board4(board4)
hit12=input("***2ND PLAYER Enter the coordinate you would like to hit: ")

def check2_input2():
    if len(hit12) !=2:
        return False
    elif hit12[0] not in "ABCDEFGH":
        return False
    elif hit12[1]not in "12345678":
        return False
    else:
        return True
def hit_direction2():
    str1=hit12[0]
    str2=hit12[1]
    num1=dict1[str1]
    num2=dict2[str2]
    if board[num1][num2]=='s':
        board4[num1][num2]='X'
        board5[num1][num2]="-"
        board6[num1][num2]="-"
        board7[num1][num2]="-"
        board8[num1][num2]="-"
        print("***!!!good shot!!!")
        
    if board[num1][num2]=="-":
        board4[num1][num2]="M"
        print("***!!!u miss!!!")
    print_board4(board4)
while True:
    if check2_input2()==True:
        hit_direction2()
        break
    if check2_input2()==False:
        print("The coordinates you entered could not be recognised , please try again")
        hit12=input("***2ND PLAYER Enter the coordinate you would like to hit: ")       

#This step does not participate in the loop because it needs to show the player the original whiteboard and define the function
xunhuan=0
while True:
    if xunhuan%2==0:
        print('***1ST PLAYER is your trun')
        print_board3(board3)
        hit11=input("***1ST PLAYER Enter the coordinate you would like to hit: ")
        while True:
            if check2_input()==True:
                hit_direction()
                break
            if check2_input()==False:
                print("The coordinates you entered could not be recognised , please try again")
                hit11=input("***1ST PLAYER Enter the coordinate you would like to hit: ")
        xunhuan=xunhuan+1

        count1=0
        for i in board3:
            count1+=i.count("X")
            
        count7=0
        for i in board9:
            count7+=i.count("-")
        count8=0
        for i in board10:
            count8+=i.count("-")
        count9=0
        for i in board11:
            count9+=i.count("-")
        count10=0
        for i in board12:
            count10+=i.count("-")
        if count7==65:
            print("u sunk my Carrier" )
        count7=66
        if count8==65:
            print("u sunk my Battleship" )
        count8=66
        if count9==65:
            print("u sunk my Destroyer" )
        count9=66
        if count10==65:
            print("u sunk my Submarine" )
        count10=66
        if count1==14:
            print(name1,"win")
            break
        
    if xunhuan%2!=0:
        print('***2ND PLAYER is your trun')
        print_board4(board4)
        hit12=input("***2ND PLAYER Enter the coordinate you would like to hit: ")
        while True:
            if check2_input2()==True:
                hit_direction2()
                break
            if check2_input2()==False:
                print("The coordinates you entered could not be recognised , please try again")
                hit12=input("***2ND PLAYER Enter the coordinate you would like to hit: ") 
        xunhuan=xunhuan+1
   
        count2=0
        for i in board4:
            count2+=i.count("X")
        count3=0
        for i in board5:
            count3+=i.count("-")
        count4=0
        for i in board6:
            count4+=i.count("-")
        count5=0
        for i in board7:
            count5+=i.count("-")
        count6=0
        for i in board8:
            count6+=i.count("-")

        
        if count3==65:
            print("u sunk my Carrier" )
            count3=66
        if count4==65:
            print("u sunk my Battleship" )
            count4=66
        if count5==65:
            print("u sunk my Destroyer" )
            count5=66
        if count6==65:
            print("u sunk my Submarine" )
            count6=66
        if count2==14:
            print(name2,"win")
            break
    
    
        

        

