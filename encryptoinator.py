import random

class Cryptografy:

    def __init__(self, message, key):
        self.__message = message
        self.__key = key

    @property
    def message(self):
        return self.__message
    @message.setter    
    def message(self, message):
        self.__message = message

    @property
    def key(self):
        return self.__key
    @key.setter    
    def key(self, key):
        self.__key = key
        
    def encrypt(key, message):
        start = 0
        message = str(message)
        messagelist = list(message.replace(" ", ""))
        finalstr = ""

        for i in range(start, len(messagelist) // 10):
            keylist = messagelist[start:start + 10]
            for i in range(10):
                finalstr += keylist[key[i]]
                start += 1
        finalstr += "".join(messagelist[start:start + 10])
        return(finalstr)

    def keygen():
        print("Generate key? no = 0, yes = 1")
        trigger = input()
        if trigger == "0":
            return(diya.input_key())
        else:
            key = [0,1,2,3,4,5,6,7,8,9]
            random.shuffle(key)
            print(f"yours key - {key}")
            return(key)
        
    def input_key():
        print('Type a key in  "0123456789" format')
        while True:
            try:
                key = input()
                if len(key) == 10:
                    key = list(map(int, key))
                    print(f"yours key - {key}")
                    return(key)
                else:
                    print("key is not 10 digits long")
                    continue
            except:
                print("key is not a number")
                continue

    def input_message():
        print("type a message")
        text = input()
        return(text)
    
def whatToDo():
    print("encryptoinator 2000")
    print("encrypt = 0, decrypt = 1")
    
    try:
        n = input()
        if int(n) == 0:
            diya.key = diya.keygen()
            diya.message = diya.input_message()
            print(diya.encrypt(diya.key, diya.message))
        elif int(n) == 1:
            diya.key = diya.input_key()
            diya.message = diya.input_message()
            print(diya.encrypt(diya.key, diya.message))
        else:
            0/0
    except:
        print("type 0 or 1")    

diya = Cryptografy

while True:
    whatToDo()








'''
some cool code that write my friend
but it not what i needed
'''

# import random

# print("enter message")
# message = input()
# messagelist = list(message.replace(" ", ""))
# key = [9,8,7,4,5,1,2,3,6,0]
# # random.shuffle(key)
# keylist = []
# finalstr = ""
# start = 0
# end = len(messagelist)

# for i in range(start, (end + 10 ) // 10):
#     keylist = messagelist[start:start + 10]

#     for j in range(10):
#         if (len(finalstr) % 10) == (len(keylist)):
#             break
#         if key[j] > len(keylist)-1:
#             continue

#         finalstr += keylist[key[j]]
#         start += 1

# print(finalstr) 