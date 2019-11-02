my_list = ["daniel", "hani", "mais"]

def find_even_num(list_of_num):
    if type(list_of_num) == list:
        count = 0
        for num in list_of_num:
            if type(num) == int or type(num) == float:
                if num % 2 == 0:
                    count += 1
        return count
    else:
        return 0
        
def look_for_string(my_string):
    if type(my_string) == str:
        return True
    else:
        return False

# def look_for_(my_number):
#     if type(my_number) == int:
#         return True
#     else:
#         return False 

thistuple = ("apple", "banana", "cherry")
thisset = {"appl", "ban", "cher"}

