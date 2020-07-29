import time
print('This is a simple program tha tells you if you number is odd, even, prime or composite')

        
def run():
    print('Type an integer :')
    y = int(input())
    if y % 2 == int(0):
        print('This is an even number')
        
    else:
        print('This number is an odd number')    
        
    
    
    if y == 1 or y == 0:
        print('This number is neither odd nor composite')
    elif y == 2 :
        print('This is a prime number')
    
    for i in range(2, y):
        if y % i == int(0) :
            print('This number is a composite number')
            time.sleep(2)
            main()
            break
            
        elif y % i != int(0):
            print('This is a prime number')    
            time.sleep(2)
            main()
            break 
            
        else:
            print('This is a compp number')
    
    
def main():
    print('Do you want to procced?')
    time.sleep(0.25)
    print('Type "yes" or "no"')
    x = input()
    if x == 'yes' :
        print('Ok, wait for about 1 second!')
        time.sleep(1)
        run()
    elif x == 'no' :
        print('Get out of here!!!')
    else:
        print("Invalid statment. The program will start again in about 3 seconds.")
        time.sleep(2.25)
        main()
       
main()       

