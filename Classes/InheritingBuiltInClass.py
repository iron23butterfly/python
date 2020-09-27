# Inheriting from built-in class - str

class RevStr(str):
    def __str__(self):
        return self[::-1]

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__': main()

# OUTPUT
# .dlroW ,olleH
