#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string is None:
        return None

    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_int = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = rom_val.get(char, 0)
        if not rom_val:
            return None
        if value >= prev_value:
            rom_int += value
        else:
            rom_int -= value
        prev_value = value

    return rom_int
