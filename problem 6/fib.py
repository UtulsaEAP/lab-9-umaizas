def fibonacci(n):
    
    if n < 0:
        return -1
    
    a = 0
    b = 1

    for n in range(0, n):
        fib = a + b 
        b = a
        a = fib
        
        

    
    
    #write your code here
    return a

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')