#catch the division by 0 error
def action (a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError as ex:
        print(f'An error accured: {ex}')
print("Enter the number a and b separated by space")
a, b= map(int, input().split())
print(action (a,b))