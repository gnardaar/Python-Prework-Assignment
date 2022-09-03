#question 1:
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    user_name = "paul"
    if user_name == "andy".title():
        print("hello, " + user_name)
    else:
        print("kick rocks! your not him!")
hello_name("Andy")

#question 2:
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def get_odd_numbers(numbers):
    odd_numbers = []

    for number in numbers:
        if number % 2 == 1:
            odd_numbers.append(number)

    return odd_numbers
get_odd_numbers(numbers=range(100))

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list( a_list ):  
    max = a_list[ 0 ]  
    for num in a_list:  
        if num > max:  
            max = num  
    return max  
print(max_num_in_list([43, 28, 67, 90])) 

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100,
# unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    a_year = int(input('Enter year : '))
 
    if (a_year%4 == 0 and a_year%100 != 0) or (a_year%400 == 0) :
        print(a_year, "is a leap year.")
    else :
        print(a_year, "is not a leap year.")
        
is_leap_year(a_year=0)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example,
# [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(nums):
   if len(nums) < 1:
      return False
   min_num = min(nums)
   max_num = max(nums)
   if max_num - min_num + 1 == len(nums):
      for i in range(len(nums)):
         if nums[i] < 0:
            j = -nums[i] - min_num
         else:
            j = nums[i]- min_num
            if nums[j] > 0:
               nums[j] = -nums[j]
            else:
               return False
      return True
   return False
nums = [6, 8, 3, 5, 4, 7]
print(is_consecutive(nums))
