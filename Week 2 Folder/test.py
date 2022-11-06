#######################################################
#                  Exercise 3 Tests                   #
#                    Instructions                     #
#   1. Move this file the to exercise folder          #
#   2. Make sure there aren't any function calls      #
#      in your exercise files                         #
#   3. Run this file and check for errors or success  #
#######################################################


from ex3 import *


########################
#         A. 1         #
########################

# Test manually


########################
#         A. 2         #
########################

assert calc_the_inner_product([1, 2, 3], [1, 2, 3]) == 14
assert calc_the_inner_product([1, 2, 3], [10.5, -2, 0]) == 6.5
assert calc_the_inner_product([1, 2, 3], []) is None
assert calc_the_inner_product([0], [0]) == 0
assert calc_the_inner_product([-10], [-5]) == 50
assert calc_the_inner_product([], [1]) is None
assert calc_the_inner_product([], []) == 0


########################
#         A. 5         #
########################

assert primes_generator(0) == []
assert primes_generator(1) == [2]
assert primes_generator(2) == [2, 3]
assert primes_generator(7) == [2, 3, 5, 7, 11, 13, 17]
assert primes_generator(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                                41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                                89, 97, 101, 103, 107, 109, 113, 127, 131,
                                137, 139, 149, 151, 157, 163, 167, 173, 179,
                                181, 191, 193, 197, 199, 211, 223, 227, 229]


########################
#         A. 6         #
########################

assert vectors_list_sum([[1, 1], [1, 3]]) == [2, 4]

assert vectors_list_sum([[1, 1, 1], [1, 0, 0], [0, 0, 100]]) == [2, 1, 101]

assert vectors_list_sum([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == [2, 2, 2, 2, 2]

print("All tests passed")