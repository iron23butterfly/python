class Animal:
    # class variable
    class_variable = [1, 2, 3]

    # def __init__(self, **kwargs):
    #     self._type = kwargs['type_value'] if 'type_value' in kwargs else 'kitten'
    #     self._name = kwargs['name_value'] if 'name_value' in kwargs else 'fluffy'
    #     self._sound = kwargs['sound_value'] if 'sound_value' in kwargs else 'meow'

    def __init__(self, type_value, name_value, sound_value):
        self._type = type_value if 'type_value' != None else 'VOID'
        self._name = name_value if 'name_value' != None else 'VOID'
        self._sound = sound_value if 'sound_value' != None else 'VOID'

    def typeMethod(self, t = None):
        if t: self._type = t
        return self._type

    def nameMethod(self, n = None):
        if n: self._name = n
        return self._name

    def soundMethod(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.typeMethod()} is named "{self.nameMethod()}" and says "{self.soundMethod()}".'

def main():
    a1 = Animal(type_value = 'duck', name_value = 'donald', sound_value = 'quack')
    print(a1)
    a0 = Animal(type_value='kitten', name_value='fluffy', sound_value='rwar')
    print(a0)

    a0._name = 'WHAAATTTT'  # works not acceptable
    a0.type_value = 'WHYYY' # This will NOT change self._type nor give an error!!
    print(f'\na0.type_value: {a0.type_value}\n') # Prints above value

    # print(f'a0.name_value: {a0.name_value}') # This will give an error
                                               # AttributeError: 'Animal' object has no attribute 'type_value'
    a0.soundMethod('BLAH_BLAH_BLAH')
    print(a0)

    print()
    print (f'a0.class_variable: {a0.class_variable}')
    a1. class_variable[2] = 'QUACK'
    print(f'a0.class_variable: {a0.class_variable}')

if __name__ == '__main__': main()

# OUTPUT
# The duck is named "donald" and says "quack".
# The kitten is named "fluffy" and says "rwar".
#
# a0.type_value: WHYYY
#
# The kitten is named "WHAAATTTT" and says "BLAH_BLAH_BLAH".
#
# a0.class_variable: [1, 2, 3]
# a0.class_variable: [1, 2, 'QUACK']
