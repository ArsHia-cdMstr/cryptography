
#final part
def intToChar ( arr ):

    message = ""
    for i in range (len(arr) ):
        
        #upper-case words
        if 0 <= arr[i] <= 25 :
            message += chr(arr[i] + 65)
        
        #lower-case words
        elif 26 <= arr[i] <= 50 :
            message += chr(arr[i] + 71)

        elif arr[i] == 51 :
            message += " "
        
        elif arr[i] == 52 :
            message += "\n"
        
        elif arr[i] == 53 :
            message += ","
        
        elif arr[i] == 54 :
            message += "."
        
        elif arr[i] == 55 :
            message += "?"
        
        elif arr[i] == 56 :
            message += "!"
    
    return message ;
