from main import *
from test import *


test_for_equal(find_even_num([2,3,4,5,6,7,8]),4)
test_for_equal(find_even_num([2,3,4,5,6,7,8, 10, 12]), 6)
test_for_not_equal(find_even_num([2,3,4,5,6,7,8, 10, 12]), 10)


test_for_equal(look_for_string("hello world"), True)
test_for_equal(look_for_string(123), False)
test_for_not_equal(look_for_string(123), True)

test_for_existance(my_list, "hani")
# test_for_existance(my_list, "abhay")
# test_for_not_equal(look_for_number(5),True)
test_for_existance(thisset,5)
print("all your tests passed")


my_file = open("myclass.txt", "w")
my_file.write("this is the text inside")
my_file.close()