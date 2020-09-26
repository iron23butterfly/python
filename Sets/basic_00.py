def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)
    # The order in which the set is printed will vary in each run

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()

# OUTPUT
# {.W gonbreadti'}
# {IrhyDdvf,ecnatmo s.i'}
