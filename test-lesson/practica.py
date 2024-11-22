import math

value = int(input('Enter number: '))
num = 1
value_2 = 0
while True:
        va = value//2
        v0 = value%2
        if va >= num:
            value_1 = math.cos(num)-math.cos(num+1)
            value_2 = value_2 + value_1    
            
            print(f'value: {value_2} num: {num}')
            num += 2
        elif v0!=0 and va+v0>=num:
            value_7 = math.cos(num)-math.cos(num+1)
            value_2 = value_2 + value_7    
            print(f'value: {value_2} num: {num}')
            num += 1
        else:
            break
        
   

    