def main():
    try:
        x = int('foo')
    except ValueError:
        print('I caught an error using exceptions!')
    except:
        print('Spend you time learning or praying!!')

    try:
        x = str('foo')
    except ValueError:
        print('I caught an error using exceptions!')
    except:
        print('Spend you time learning or praying!!')
    else:
        print ('Good job - No eerors')

if __name__ == '__main__': main()

# OUTPUT
# I caught an error using exceptions!
# Good job - No eerors
