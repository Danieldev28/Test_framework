# test to check if two values are equal
def test_for_equal(actual,expected):
    assert actual == expected, "So here {} was not equal to {} as expected".format(actual,expected)

# test to check if an actual value is not equal to the unexpected value.    
def test_for_not_equal(actual, unexpected):
    assert actual != unexpected, "So here {} was equal to {} as unexpected".format(actual,unexpected)

# test to check if an item exists in a collection or list    
def test_for_existance(my_list, item):
    assert item in my_list, "So here {} is not present inside the {}".format(item, my_list)


