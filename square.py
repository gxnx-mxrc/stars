def main(size):
        columns = 0
        rows = 0
        while columns != size:
            if columns != size:
                while rows != size:
                    print(" * ", end=' ')
                    rows += 1
                print()
                columns += 1
                rows = 0
            else:
                return

main(5)