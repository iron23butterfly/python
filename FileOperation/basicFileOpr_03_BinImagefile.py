# This copies binary and image file
# image files are opened as binary files

def main():
    infile = open('berlin.jpg', 'rb')
    outfile = open('berlin-copy.jpg', 'wb')
    while True: #while will stop only at break!
        buf = infile.read(10240) #10K is the size of the buffer
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()

# OUTPUT
# ..........
# done.
