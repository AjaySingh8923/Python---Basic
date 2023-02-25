def winner(user , li):
    if user==0:
        li[key-1]="o"
    if user==1:
        li[key-1]="X"
    for i in range(0,7,3):
        if li[i]==li[i+1] and li[i+1]==li[i+2]:
            if user==0:
                print("user1 is winner")
                return 1 
            else :
                print("user 2 is winner")
                return 1 
        
             
    for i in range(0,3):        
        if li[i]==li[i+3] and li[i+3]==li[i+6]:
            if user==0:
                print("user1 is winner")
                return 1 
            else :
                print("user 2 is winner")
                return 1   
        
     
    if (li[0]==li[4] and li[4]==li[8]) or (li[2]==li[4] and li[4]==li[6]):
        if user==0:   
            print("user1 is winner")
            return 1 
        else :
            print("user 2 is winner")
            return 1 
                      
                  
   
   

def board(user,key,li):
    
    if user == 0:
       li[key-1]="O"
    if user == 1:
       li[key-1]="X"
    for i in range(0,7,3):
        print(" ",li[i]," "+"|"+" ",li[i+1]," "+"|"+" ",li[i+2]," ")
    #print(" _    _    ")   
        print(" ","_"," "+" "+" ","_" +" " ,"_"," " )
  
    win = winner(user, li)
    
    return li, win
   

user1 =0 
user2 =1
key = 0
win = 0
li =[1,2,3,4,5,6,7,8,9,10]
print("welcome to tik tack toe")
board(user1,key,li)
for i in range (1,10):
    if i == 9:
        print("Draw")
        break
    if win!=1:
        if i%2==0:
            print("\n user2 turn: choose any number:")
            key=int(input())
            li, win=board(user2,key,li)
        else:
            print("\n user1 turn: choose any number:")
            key=int(input())
            li, win=board(user1,key,li)
    else:
        break
    