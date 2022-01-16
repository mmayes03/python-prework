#Question 1
def hello_name(user_name):
    print("hello_{}!".format(user_name))
hello_name(input("What is your name?\n"))

#Question 2
def first_odds():
    odd_numbers = []
    for i in range(100):
        if i % 2 == 0:
            continue
        if i % 2 == 1:
            odd_numbers.append(i)
    print(odd_numbers)

#Question 3
def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

#Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0 or a_year % 100 != 0 and a_year % 400 ==0:
        return True
    else:
        return False

#Question 5
def is_consecutive(a_list):
    #sort = sorted(a_list)
    A = min(sorted(a_list))
    B = max(sorted(a_list))
    new_list = []
    for i in range(A,B+1):
        new_list.append(i)
    if a_list == new_list:
        return True
    else:
        return False
   


