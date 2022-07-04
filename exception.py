


from logging import exception


try:
    def additoin(x,y):
        x = 10
        y =20
        print("Addition:", x + y)
        additoin(10,20)

except exception:
    print(exception)
finally:
    print('the operation is successful')