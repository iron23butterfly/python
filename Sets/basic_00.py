def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)
    # The order in which the set is printed will vary in each run
    print ('set(a|b) {}'.format(set(a | b)))
    print (f'Set_a.Union(Set_b): {a.union(b)}')
    union1 = set(a | b)
    union2 = a.union(b)
    print ("Same length") if len(union1) == len(union2) else print('Not the same length')
    print (f'difference between union1 and union2: {union1 - union2}')

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()

# OUTPUT
# {tiWb nadg.e'or}
# {cd,D.o'tiameI fvyrnsh}
# set(a|b) {'c', 'd', ' ', 'f', ',', 'v', 'D', '.', "'", 'o', 'y', 'r', 't', 'i', 'W', 'b', 'a', 'n', 's', 'g', 'm', 'e', 'I', 'h'}
# Set_a.Union(Set_b): {'c', 'd', ',', 'D', '.', "'", 'o', 't', 'i', 'a', 'm', 'e', 'I', ' ', 'f', 'v', 'y', 'r', 'W', 'b', 'n', 's', 'g', 'h'}
# Same length
# difference between union1 and union2: set()

