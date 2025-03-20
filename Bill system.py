Goods = 0
G = 0
Q =0
tot =0
tot1 = 0
payment = 0
price = []

def add (x,y):
    return x+y
    
def subtract (x,y):
    return x-y

def display_menu():
 print("********WEL COME TO DISINI STORES***********")

 file=open("data.txt")
 contents=file.read()
 print(contents)
 
price = [0,150,120,150,50,300,300,1200,2000,100,70]


while True:
    tot1=0
    display_menu()

    while True :
            Goods=int(input("enter your goods number:"))
            G = price [Goods]
            Q =int(input("How many want for you :")) 
            tot=G*Q
            print (G, "*" ,Q , "= ",tot)
            tot1 = add(tot,tot1)
            choice=input("add a next good (y/n): " ).lower()
            if choice != "y" :
                            break
            else :
                            continue
        
    print("your bill is :",tot1)
    payment = input("card or cash :")
    if payment == "card" :
                        print(" bill is successfully")
    else:
                        cash = int(input("enter cash payment : "))
                        print("your balance is : ",subtract(cash,tot1))
    print ("Your bill is sucessfully")
    print("========THANK YOU COME AGAIN========")

    next_customer =str(input("Have a next customer (y/n) ?")).lower()
    if next_customer !="y" :
            print("Thank you for shopping with us")
            break

        