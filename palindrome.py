import unittest

def palindrome(word):
    aux = ""

    for letra in word:
        if letra != ' ':
            aux += letra
    
    if (aux[::-1] == aux):
        return True
    else:
        return False
    
if __name__ == '__main__':
    unittest.main()