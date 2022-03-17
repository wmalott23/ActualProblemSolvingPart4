# Problem 1 Leap Year
# accept the user input
# use a for loop 83 times to determine if those years are leap years
# assign years to a list
# print list

# def leap_year():
#     leap_list = []
#     user_year = int(input("Enter your year and I will print the following 20 leap years!"))
    # for add_year in range(1, 81):
#         user_year += 1
#         if user_year % 4 == 0:
#             leap_list.append(user_year)
#     print(leap_list)

# leap_year()

# Problem 2 Palindromic Substring
# accept an input from the user
# create the palindrome checker
# use for loop to analyze every potential substring
# print palindromes to a list
# identify the largest palindrome
# print the largest palindrome substring



# def palindrome_check(check_input):
#     input_str = str(check_input)
#     rev_input = ""
#     for char in input_str:
#         neg_char_pos = (-(input_str.index(char)+1))
#         rev_char = input_str[neg_char_pos]
#         rev_input += rev_char
#     if check_input == rev_input:
#         pal_answer = "true"
#     else:
#         pal_answer = "false"
#     return pal_answer

# def palindrome_substring():
#     pal_list = []
#     len_list = []
#     user_input = input("Please enter a word you would like me to check for palindromes")
#     counter = 0
#     big_len = 0
#     for letter in user_input:
#         sub_string = user_input[counter:len(user_input)]
#         counter += 1
#         len_sub = len(sub_string)
#         for sub_letter in sub_string:
#             sub_sub_string = sub_string[0:(len_sub)]
#             len_sub -= 1
#             if palindrome_check(sub_sub_string) == "true":
#                 pal_list.append(sub_sub_string)
#                 len_list.append(len(sub_sub_string))
#     for len_num in len_list:
#         if len_num > big_len:
#             big_len = len_num
#     len_ind = len_list.index(big_len)
#     print(pal_list[len_ind])
    
# palindrome_substring()


# Problem 3 hours and minutes
# accept user input
# modulus input by 3600
# remove remainder from input and set that to hour seconds
# divide hour seconds by 3600 and set that to total hours
# set remainder from first modulus to modulus 60
# remove new remainder from first remainder
# divide that total by 60 and set to minutes
# print hours and minutes

# def div_evenly(use_input,use_div):
#     remain = use_input % use_div
#     even_div = use_input - remain
#     total = even_div / use_div
#     return total

# def hour_and_minute():
#     user_input = int(input("How many seconds would you like me to calculate in hours and minutes?"))
#     tot_hour = div_evenly(user_input, 3600)
#     tot_mins = div_evenly(user_input - 3600 * tot_hour, 60)
#     print(f' That is {tot_hour} hours and {tot_mins} minutes')

# hour_and_minute()

# Problem 4 difference between a number and 13
# accept a user input
# identify if the input is greater than or less than 13
# if less than, subtract the number from 13
# if greater than, subtract 13 from the number and double the result
# print the result

# def thirteen_checker():
#     user_input = int(input("Enter a number you want to check against 13"))
#     if user_input < 13:
#         total = 13 - user_input
#     if user_input > 13:
#         total = (user_input - 13) * 2
#     print(total)

# thirteen_checker()



# Problem 5 Check if numbers end the same
# accept three numbers from the user
# if end of number 1 is equal to end of number 2, add one to counter
# if end of number 1 is equal to end of number 3, add one to counter
# if end of number 2 is equal to end of number 3, add ont to counter
# if counter is 2 or more, print true

# def check_three_nums():
#     num_list = []
#     counter = 0
#     for num in [1, 2, 3]:
#         user_input = input("Please enter a number")
#         num_list.append(user_input[-1])
#     if num_list[0] == num_list[1]:
#         counter += 1
#     if num_list[0] == num_list[2]:
#         counter += 1
#     if num_list[2] == num_list[1]:
#         counter += 1
#     if counter >= 1:
#         print("true")
#     else:
#         print("false")

# check_three_nums()


# Problem 6 A and B checker
# Accept input from user
# Find position numbers for "a" in string
# put position numbers in a list
# find position numbers for "b" in string
# put position numbers in a list
# for each number in "a" list, subtract number from each number in "b" list
# see if any result is 3
# print true if a result is 3 and false if not