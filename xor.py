def findGrid(n):  
    arr = [[0 for k in range(n)]  
              for l in range(n)]  
    x = 0
    for i in range(n // 4):  
        for j in range(n // 4):  
            for k in range(4):  
                for l in range(4):  
                    arr[i * 4 + k][j * 4 + l] = x  
                    x += 1 
    for i in range(n):  
        for j in range(n):  
            print(arr[i][j], end = " ") 
        print() 
n = int(input('enter n: '))
findGrid(n) 
