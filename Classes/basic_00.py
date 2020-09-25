class Duck:
    def quack(self):
        print('Quaaack!')

    walking = 'Walks like a duck.'
    def walk(self):
        print(self.walking)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()


# OUTPUT
# Quaaack!
# Walks like a duck.
