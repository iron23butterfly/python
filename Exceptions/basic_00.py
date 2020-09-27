def main():
    try:
        x = int('foo')
    except:
        print('I caught an error using exceptions!')

if __name__ == '__main__': main()

# OUTPUT
# I caught an error using exceptions!
