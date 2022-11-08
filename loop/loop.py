def add_address(user_msg):
    return user_msg + " programe"


def adduser (msg):
    user_msg = "Nanda "+msg
    return add_address(user_msg)

def message ():
    return adduser("hello world!") 

def main(num):
    for i in range(num):
        result = message()
        print(result)

num = int(input("enter number:"))
main(num)

