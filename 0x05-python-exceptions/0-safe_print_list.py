#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list[:x]:
            print(i, end='')
            count += 1
        print()
        return count
    except TypeError as e:
        print("Error:", e)
        return 0
    except Exception as e:
        print("An error occurred:", e)
        return 0
