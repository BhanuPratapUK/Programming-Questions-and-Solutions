'''How to use LAMBDA Method + Use of lambda method with function'''
Result=lambda x,y:x**y
print('Here the anser is =>>>',Result(2,3))
print('********************************************')
'''USe with function'''
def comparison(a,b):
    if a>b:
        return a
    else:
        return b
A = lambda x,y: x**y# same as top one i am taking...here not to confuse 
B = lambda x,y: x+y
print('The GREATER one is ---->',comparison(A(4,3),B(7,4)))
