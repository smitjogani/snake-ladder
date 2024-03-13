from PIL import Image
import random

def reached_end(points):
    if points == end:
        return True
    else:
        return False

def checkSnake(points):
    if points == 34:
        print('snake')
        return 14
    elif points == 67:
        print('snake')
        return 53
    elif points == 23:
        print('snake')
        return 9
    elif points == 49:
        print('snake')
        return 25
    elif points == 92:
        print('snake')
        return 48
    elif points == 99:
        print('snake')
        return 1
    elif points == 89:
        print('snake')
        return 34
    elif points == 74:
        print('snake')
        return 87
    elif points == 94:
        print('snake')
        return 3
    return points

def checkLadder(points):
    if points == 8:
        print('Ladder')
        return 26
    elif points == 21:
        print('Ladder')
        return 45
    elif points == 6:
        print('Ladder')
        return 36
    elif points == 67:
        print('Ladder')
        return 96
    elif points == 74:
        print('Ladder')
        return 87
    elif points == 88:
        print('Ladder')
        return 100
    return points

def show_board():
    img = Image.open('./sl.jpg')
    img.show()

def play():
    p1_name = input("Enter player1 name : ")
    p2_name = input("Enter player2 name : ")

    pp1,pp2 = 0, 0

    turn = 0    

    while(1):
        if turn % 2 == 0:
            print(p1_name, 'Your Turn')
            c = input("Press 1 for continue and 0 for quite :")

            if c == 0:
                print(p1_name, 'scored - ', pp1)
                print(p2_name, 'scored - ', pp2)
                print("Thank you for playing")
                break
            dice = random.randint(1,6)
            pp1 += dice
            pp1 = checkLadder(pp1)
            pp1 = checkSnake(pp1)
            
            if pp1 > end:
                pp1 = end

            print(p1_name, ' Your Score ', pp1)
            
            if(reached_end(pp1)):
                print(p1_name, ' Won')
                break
        else:
            print(p2_name, 'Your Turn')
            c = input("Press 1 for continue and 0 for quite :")

            if c == 0:
                print(p1_name, ' scored ', pp1)
                print(p2_name, ' scored ', pp2)
                print("Thank you for playing")
                break
            
            dice = random.randint(1,6)
            pp2 += dice
            pp2 = checkLadder(pp2)
            pp2 = checkSnake(pp2)
            
            if pp2 > end:
                pp2 = end

            print(p2_name, ' Your Score', pp2)
            
            if(reached_end(pp2)):
                print(p2_name, 'Won')
                break      
        turn += 1        


end = 100
show_board()
play()