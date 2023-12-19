#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            if isinstance(my_list_1[i], (int, float)):
                dividend = my_list_1[i]
            else:
                dividend = None
            if isinstance(my_list_2[i], (int, float)):
                divisor = my_list_2[i]
            else:
                divisor = None

            if dividend is None or divisor is None:
                result.append(0)
                if dividend is None or divisor is None:
                    print("wrong type")
            elif divisor == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(dividend / divisor)

        except IndexError as e:
            print(e)
            result.append(0)

    return result
