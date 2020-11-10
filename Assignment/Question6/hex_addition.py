#!/usr/bin/env python3 


def hex_add(num1, num2, rem=0):
    """ Adds two hex numbers with carry """

    num1 = int(str(num1), 16)
    num2 = int(str(num2), 16)
    max_val = str(hex(max(num1, num2)))
    max_val = max_val.replace('0x', '')
    dig = len(max_val)

    hex_sum = num1 + num2 + rem
    hex_sum = str(hex(hex_sum)).replace('0x', '')
    
    Sum = hex(int('0x' + hex_sum[-dig:], 16))
    Rem = hex(int('0x0' + hex_sum[:len(hex_sum) - dig], 16))

    return Sum, Rem

Sum, Rem = hex_add(hex(16), hex(16))
print(f'Sum is {Sum} and Reminder is {Rem}')












"""
var = 'hello, world'
print(var[-4:])
"""