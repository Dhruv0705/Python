#expand the key

def ordinal(letter):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    return alpha.index(letter)

def alphabet(number):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    return alpha[number]

def expandKey(message, key):
    if len(message) == len(key):
        return key
    else: 
        i = 0
        while len(key) < len(message):
            key += key[i % len(key)]
            i += 1
        return key

def encrypt(message, key):
    encrypted = ''
    for i in range(len(message)):
        x = (ordinal(message[i]) + ordinal(key[i])) % 26
        encrypted += alphabet(x)
    return encrypted

def main():
    message = 'alliswell'
    key = 'cake'
    expanded = expandKey(message,key)
    print(encrypt(message,expanded))
    
main()