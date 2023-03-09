def take_input(val): 
    chk =False
    while chk == False:
        try:
            if __name__  == "__main__":
                val =int(input("enter a whole number: ")) 
                # we get here only of everything is still okay
                chk,val = doing_work (val)
            else:
                if val/int (val)  != 1:
                    val=-1
                    raise  TypeError("")
                # we get here only of everything is still okay
                chk,val = doing_work (val)
        except Exception as e:             
            # we are here because something went wrong
            if __name__  == "__main__":
                print(e)
                chk  = False  # so we can carry on with while loop
            else:
               break
    return val


def  doing_work (v):
    v =v*5    
    chk=True
    return chk,v


def main(): 
    y=take_input(-1)
    print(y)
    
    
if __name__  == "__main__":
    main()