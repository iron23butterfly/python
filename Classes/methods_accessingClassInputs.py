class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'VOID'
        self._name = kwargs['name'] if 'name' in kwargs else 'VOID'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'VOID'

    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self): # This is a special method name, used for printing
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    print(a0)
    a0.sound('blah-blah-blah'.upper())
    print(a0)
    a1 = Animal(type='duck', name='donald', sound='quack')
    print(a1)
    print(f'\n {Animal()}')

if __name__ == '__main__': main()

# OUTPUT
# The kitten is named "fluffy" and says "rwar".
# The kitten is named "fluffy" and says "BLAH-BLAH-BLAH".
# The duck is named "donald" and says "quack".
# 
 # The VOID is named "VOID" and says "VOID".
