#!/usr/bin/env python3

def return_hexsum(*args, rem=0):
    """ Return's  sum of hex with carray """

    nums = list(args) + [rem]
    nums = [int(str(num), 16) for num in nums]
    max_dig = len(str(hex(max(nums))).strip('0x'))
    max_sum = str(hex(sum(nums)))
    print(max_sum)

    return '0x' + max_sum[len(max_sum) - max_dig :len(max_sum)], max_sum[:len(max_sum)-max_dig]

hex_sum, rem = return_hexsum(hex(256), hex(16))
print(hex_sum, rem)