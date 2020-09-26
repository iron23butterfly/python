from Ex_Files_Python_EssT.ExerciseFiles.Chap09.constructor import Animal

class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

def main():
    donald = Duck()
    donald.quack()
    donald.move()
    print('_name' in dir(Animal))

if __name__ == '__main__': main()


# OUTPUT
# Quack quack.
# Walks like a duck.
# False
