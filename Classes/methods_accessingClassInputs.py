#!/usr/bin/env python3
class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['value_type'] if 'value_type' in kwargs else 'VOID'
        self._name = kwargs['value_name'] if 'value_name' in kwargs else 'VOID'
        self._sound = kwargs['value_sound'] if 'value_sound' in kwargs else 'VOID'

    def typeMethod(self, t = None):
        if t: self._type = t
        return self._type

    def nameMethod(self, n = None):
        if n: self._name = n
        return self._name

    def soundMethod(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self): # This is a special method name, used for printing
        return f'The {self.typeMethod()} is named "{self.nameMethod()}" and says "{self.soundMethod()}".'

def main():
    a0 = Animal(value_type='kitten', value_name='fluffy', value_sound='rwar')
    print(a0)
    a0.soundMethod('blah-blah-blah'.upper())
    print(a0)
    a1 = Animal(value_type='duck', value_name='donald', value_sound='quack')
    print(a1)
    print(f'\n {Animal()}')
    print (dir(a0))

if __name__ == '__main__': main()

# OUTPUT
# The kitten is named "fluffy" and says "rwar".
# The kitten is named "fluffy" and says "BLAH-BLAH-BLAH".
# The duck is named "donald" and says "quack".
#
#  The VOID is named "VOID" and says "VOID".
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_name', '_sound', '_type', 'nameMethod', 'soundMethod', 'typeMethod']

