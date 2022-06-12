"""
GIT AND TEST REVISION
Simple assert test
"""
""" Original """

def factorial(num):
    assert type(num)==type(1),f"Expecting Natural number, got:{type(num)}"
    assert num>=0,f"Expecting num>=0, got:{num}"

    if (num==0):
        return 1
    else:
        return num*factorial(num-1)

if __name__=="__main__":
    print("!!")
    print(factorial(8))