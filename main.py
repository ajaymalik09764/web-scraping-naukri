from automation import sele 
i=str(input("Enter Search String:- "))
try:
    obj=sele()
    obj.driver(i)
    r=True
except:
    print("error ")
    r=False
    
    
while r:    
    s=str(input("scrap result y/n"))
    if "y".casefold()==s.casefold():
        try:
            obj.scrap()
            obj.b.close()
            r=True
        except:
            print("error (please check class and id in scrap function)")
            r=False
            break
        break
    elif "n".casefold()==s.casefold():
        print("thank you")
        r=False
        break
    else:
        print("Enter right keys")
    
while r:
    d=str(input("Save into csv(y/n):- "))
    if "y".casefold()==s.casefold():
        try:
            obj.savedata()
            break
        except:
            print("error")
            break
        break
    elif "n".casefold()==s.casefold():
        print("thank you")
        break
    else:
        print("Enter right keys(y/n)")


    