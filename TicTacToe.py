
def display(arr):
        
    print("    |    |    ")
    print(f'  {arr[7]} |  {arr[8]} | {arr[9]} ')
    print("    |    |    ")
    print("----------------")
    print("    |    |    ")
    print(f'  {arr[4]} |  {arr[5]} | {arr[6]} ')
    print("    |    |    ")
    print("----------------")
    print("    |    |    ")
    print(f'  {arr[1]} | {arr[2]}  | {arr[3]} ')
    print("    |    |    ")
    

def full_check(arr):
    for i in range(1,9):
        if(arr[i]==' '):
            return False
        
    return True

def position_marker(arr,ans,turn):
    sim=int(ans)
    cha=''
    if(turn == 1):
        cha='X'
        arr[sim]=cha
    else:
        cha='O'
        arr[sim]=cha    


def check_game(arr):
    if(arr[1]==arr[2]==arr[3]!=' '):
        return 'Win'
    elif(arr[4]==arr[5]==arr[6]!=' '):
        return 'Win'
    elif(arr[7]==arr[8]==arr[9]!=' '):
        return 'Win'
    elif(arr[1]==arr[5]==arr[9]!=' '):
        return 'Win'
    elif(arr[7]==arr[5]==arr[3]!=' '):
        return 'Win'
    elif(arr[1]==arr[4]==arr[7]!=' '):
        return 'Win'
    elif(arr[2]==arr[5]==arr[8]!=' '):
        return 'Win'
    elif(arr[3]==arr[6]==arr[9]!=' '):
        return 'Win'


def game():
    count =1
    str=''
    while str not in ['Yes','yes','YES','No','no','NO'] :
        str=input("Do you wanna play the game?? (Type Yes/No): ")
        if str in ['Yes','yes','YES']:
            print("Welcome to Tic Tac Toe game!!")
            print("This game is created by Tahanish Vallepalli")
            print("This game is played on the basis of NumPad")
            choice=input("Choose the Symbol in 'X', 'O' :")
            arr=[' ']*10
            if choice in ['X','x','O','o']:
                if choice in ['X', 'x']:
                    print("Your Player No-1")
                else :
                    print("Your Player NO-2")
            status='started'
            ans=''
            turn =0
            acceptable_values = ['1','2','3','4','5','6','7','8','9']
            while(status!='Ended'):
                print(count)
                print("Player-1 turn")
                turn =1
                ans=input("Enter the position no :")
                while ans not in acceptable_values:
                    ans=input("Enter a correct position")
                if full_check(arr):
                    print("The Game has become Tie")
                    break
                position_marker(arr,ans,turn)
                display(arr)
                if full_check(arr):
                    print("The Game has become Tie")
                    break
                sam=check_game(arr)
                if (sam=="Win"):
                    print("Hurray!!, Game Completed")
                    print(f'Player {turn} Wins')
                    status='Ended'
                    break
                print("Player-2 turn")
                turn=2
                ans=input("Enter the position")
                while ans not in acceptable_values:
                    ans=input("Enter a correct position")
                if full_check(arr):
                    print("The Game has become Tie")
                    break
                position_marker(arr,ans,turn) 
                display(arr)
                if full_check(arr):
                    print("The Game has become Tie")
                    break
                sam=check_game(arr)
                if(sam=="Win"):
                    print("Hurray!!, Game Completed")
                    print(f'Player {turn} Wins')
                    status='Ended'
                    break
            str=''        
                
        elif str in ['No','no','NO']:
            print("Thanks for visiting!!")
         
        else :
            print("Enter a Vaild entry!! i.e 'Yes'/'NO' ")


if __name__ == '__main__':
    game()


