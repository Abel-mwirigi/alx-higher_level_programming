#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            value_1 = my_list_1[i]
            value_2 = my_list_2[i]
            if type(value_1) not in (int, float):
                result.append(0)
                print("wrong type")
            elif type(value_2) not in (int, float):
                result.append(0)
                print("wrong type")
            elif value_2 == 0:
                result.append(0)
                print("division by 0")
            else:
                result.append(value_1 / value_2)
        except IndexError:
            result.append(0)
            print("out of range")
        except Exception as e:
            result.append(0)
            print(e)
    return result
