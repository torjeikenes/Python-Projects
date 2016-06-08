from random import randint
import os
def playAgain():
    input = raw_input("press [Enter] if you want another suggestion?")
    if(input == ""):
        main()
    else:
        exit()

def getInput():
    input = raw_input("What advice do you want?")
    return input

def side():
    rand = randint(0,1)
    if(rand == 1):
        print '''
$$$$$$$$\ 
\__$$  __|
   $$ |   
   $$ |   
   $$ |   
   $$ |   
   $$ |   
   \__| 
   
   '''

    elif(rand == 0):
        print '''   
 $$$$$$\  $$$$$$$$\ 
$$  __$$\ \__$$  __|
$$ /  \__|   $$ |   
$$ |         $$ |   
$$ |         $$ |  
$$ |  $$\    $$ |   
\$$$$$$  |   $$ |   
 \______/    \__|  
 
 ''' 
    else:
        print "Shit messed up"

def yesNo():
    if(randint(0,9) > 2): 
        print '''
       _   _   ___  ___ 
      | | | | / _ \/ __|
      | |_| ||  __/\__ \\
       \__, | \___||___/
        __/ |           
       |___/            
                        
                        '''
    else:
        print '''
         _ __    ___  
        | '_ \  / _ \ 
        | | | || (_) |
        |_| |_| \___/ 
          
          '''

def createJoin():
    if(randint(0, 9) > 3):
       print '''
    _         _        
   (_)       (_)       
    _   ___   _  _ __  
   | | / _ \ | || '_ \ 
   | || (_) || || | | |
   | | \___/ |_||_| |_|
  _/ |                 
 |__/                  

       '''
    else:
        print '''
                            _         
                           | |        
    ___  _ __   ___   __ _ | |_   ___ 
   / __|| '__| / _ \ / _` || __| / _ \\
  | (__ | |   |  __/| (_| || |_ |  __/
   \___||_|    \___| \__,_| \__| \___|

        '''
                                                                                                                                
def main():
    #input = getInput()
    os.system('clear')
    print "Your side must be:"
    side()
    print "Do I believe?"
    yesNo()
    print "Create or Join?"
    createJoin()
    playAgain()
"""
    if(input == "side"):
        side()
    elif(input == "believe"):
        print "YES"
    else:
        print "Thats none of my business" """
    
    
main()
