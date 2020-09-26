# LIST COMPREHENSION

def main():
    seq = range(11)
    print_list(seq)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

# OUTPUT
# 0 1 2 3 4 5 6 7 8 9 10
