#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for k, i in a_dictionary.items():
            if i == value:
                del a_dictionary[k]
                break

    return (a_dictionary)
