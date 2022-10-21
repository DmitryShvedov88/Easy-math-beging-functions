#catch the division by 0 error
def action (a,b):
    try:
        result=a/b
        print("result calculated")
        return result
    except ZeroDivisionError as ex:
        print(f'An error accured: {ex}')
    #except:
        #print("unknown error accured")
print("Enter the number a and b separated by space")
a, b= map(int, input().split())
print(action (a,b))