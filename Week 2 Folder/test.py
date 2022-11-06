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





print("All tests passed")