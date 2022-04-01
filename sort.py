def sort( arr ):
    
    comparingNum = 0 ;
    for i in range (len(arr)) :
        
        if (arr[comparingNum] > 0) :
            if (arr[i] < 0) :
                #swap
                temp = arr[comparingNum]
                arr[comparingNum] = arr[i]
                arr [i] = temp

                comparingNum += 1 
        
        else:
            comparingNum += 1
    
    return arr 
