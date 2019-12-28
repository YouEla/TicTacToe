import random as rand


board=[ "-" , "-" , "-" ,
        "-" , "-" , "-" ,
        "-" , "-" , "-" ,
       ]

#Define the player that will play, first or second player 
giocatore = rand.randint(1,2)

primo= True if giocatore==1 else False 
# Interesting to know that you can check with tuplesif 1 in {x, y, z}:

croce='x'

cerchio='o'


def start_game():
    table(giocatore)
   
    
    player(giocatore)



def finito():
    ancora=int(input("premi Enter se vuoi giocare ancora, altro pulsante e finisce il gioco"))
    if ancora==0:
        start_game()
    else:
        print("Finito il gioco")
        



#Here I define the table,which checks if the player have won
def table(primo):
    print('\n\n\n\n\n\n\n\n\n\n','Tavolo di gioco\n\n',board[0:3],'\n',board[3:6],'\n',board[6:9],'\n\n\n\n\n\n\n\n\n\n\n\n',)
    #Checks what draw o or x has been drown, and the does the comparison
    if(primo==True):
        confronto='x'
    else:
        confronto='o'
    
    print(confronto)
        
    if  (board[0]==confronto and board[1]==confronto and board[2]==confronto) or (board[3]==confronto and board[4]==confronto and board[5]==confronto  )or (board[6]==confronto and board[7]==confronto and board[8]==confronto  ):
        if primo==True:
            print('il giocatore 1 ha vinto per via orizzontale, quindi con ',confronto,'\n\n')
        else:
            print('il giocatore 2 ha vinto per via orizzontale, quindi con', confronto,'\n\n')     
            
        finito()
        
    if (board[0]==confronto and board[3]==confronto  and board[6]==confronto)or (board[1]==confronto and board[4]==confronto  and board[7]==confronto ) or (board[2]==confronto and board[5]==confronto  and board[8]==confronto ):
        if primo==True:
            print('il giocatore 1 ha vinto per via verticale, quindi con ',confronto,'\n\n')
        else:
            print('il giocatore 2 ha vinto per via verticale, quindi con', confronto,'\n\n')     
            
        finito()
        
    if  (board[0]==confronto and board[4]==confronto and board[8] ==confronto ) or (board[2]==confronto and board[4]==confronto and board[6]==confronto  ):
        if primo==True:
            print('il giocatore 1 ha vinto per via obliqua, quindi con ',confronto,'\n\n')
        else:
            print('il giocatore 2 ha vinto per via obliqua, quindi con', confronto,'\n\n')     
            
        finito()
    


#Here I define the player
def gioco(disegno,primo):
    if primo==True:
        print('il giocatore 1 ha questo disegno',disegno)
    else:
        print('il giocatore 2 ha questo disegno',disegno)
        
    posizione=int(input("Digita un valori da 1:9:\t"))-1
    
    if(posizione <= 8 and posizione >= 0 and (board[posizione]!= 'o' and board[posizione]!= 'x')):
        board[posizione]=disegno   #Qua disegno nella tabella
        table(primo)
        giocatore=2 if primo else 1 #Player =2 if primo = true, so it means that the player is equal to 1 else the player(giocatore in Italian) is 2
        
        player(giocatore)#I resend the value so I can change the player
    else:
        print('errore di',OverflowError,'o hai digitato una posizione già piena') 
    


def player(giocatore):
    if(giocatore==1):
        primo=True
        gioco(croce,primo)
        
    else:
        primo=False
        gioco(cerchio,primo)
        
        


start_game()

