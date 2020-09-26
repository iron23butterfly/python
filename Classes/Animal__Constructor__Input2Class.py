class Animal:
    # __init__ is called constructor
    
    # def __init__(self, type_value, name_value, sound_value):
    #     self._type = type_value
    #     self._name = name_value
    #     self._sound = sound_value

    # can use dictionary here giving default values too
    def __init__(self, **kwargs):
        self._type = kwargs['value_type'] if 'value_type' in kwargs else 'void'.upper()
        self._name = kwargs['value_name'] if 'value_name' in kwargs else 'void'.upper()
        self._sound = kwargs['value_sound'] if 'value_sound' in kwargs else 'void'.upper()

    def typeMethod(self):
        return self._type

    def nameMethod(self):
        return self._name

    def soundMethod(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.typeMethod(), o.nameMethod(), o.soundMethod()))


def main():
    # a0 = Animal('kitten', 'fluffy', 'rwar')
    # a1 = Animal('duck', 'donald', 'quack')
    # print_animal(a0)
    # print_animal(a1)
    # print_animal(Animal('velociraptor', 'veronica', 'hello'))

    # using dictionary here:
    a0 = Animal(value_type='kitten', value_name='fluffy', value_sound='rwar')
    a1 = Animal(value_name='donald', value_type='duck', value_sound='quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(value_type='velociraptor', value_name='veronica', value_sound='hello'))
    print_animal (Animal())

if __name__ == '__main__': main()

# OUTPUT
# The kitten is named "fluffy" and says "rwar".
# The duck is named "donald" and says "quack".
# The velociraptor is named "veronica" and says "hello".
#
# OUTPUT dictionary use:
# The kitten is named "fluffy" and says "rwar".
# The duck is named "donald" and says "quack".
# The velociraptor is named "veronica" and says "hello".
# The VOID is named "VOID" and says "VOID".
