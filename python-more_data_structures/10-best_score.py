#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_value = max(a_dictionary.items(), key=lambda x: x[1])
    return max_value[0]
