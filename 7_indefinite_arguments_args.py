# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).

# def sum_squares(*args):
#     sum=0
#     for num in args: #iterate through each argument, squaring the number and add it up
#         sum += num ** 2
#     return sum

# print(sum_squares(1,2,4,4,5,6,7)) #returns: 147

# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments,
#  and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together,
#  in other words, considers them all - negative and positive - as positive).

# def absolute_sum(*args): 
#     sum=0 
#     for num in args: 
#         sum += abs(num)
#     return sum 
# list_of_numbers =[-10, 2, 4, -12, 2] 
# print(absolute_sum(*list_of_numbers)) #return 30 

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

def personal_numbers (name, *args): 
    sum=0 
    for num in args: 
        sum += num 
    return (f"{name}, the sum of your numbers is {sum}")

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"

# def tea_order(customer_name, tea_type, *args):
#     print(customer_name, "ordered a", tea_type, "tea")
#     for arg in args:
#         print("  -Add:", arg) 

# tea_order("Alice", "chamomile")
# tea_order("Bob", "black", "oat")
# tea_order("Tony", "black", "oat", "honey") 

#args allows you to add extra arguments in lists 

# def tea_order(customer_name, tea_type, **kwargs):
#     print(customer_name, "ordered a", tea_type, "tea")
#     for key, value in kwargs.items():
#         print("  -Add", key, ":", value)

# # tea_order("Alice", "chamomile")
# # tea_order("Bob", "black", "oat")
# tea_order("Tony", "black", milk="oat", sweetener="honey")