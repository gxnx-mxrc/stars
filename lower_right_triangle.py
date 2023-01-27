def main(size):
    i = size
    while i>=1:
        print(" "* (size-i) + "*" * i)
        i-=1
main(5)