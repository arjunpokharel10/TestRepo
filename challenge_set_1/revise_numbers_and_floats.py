# Write a Python function that takes two numbers (integers or floats) as input
# and returns:
# ● Their sum
# ● Their difference
# ● Their product
# ● Their division (handle the case where division by zero might occur).


from decimal import DivisionByZero


def take_numbers_for_calculation():
    num_digits = []
    for i in range(2):
        while True:
            try:
                x = int(input(f"enter {'your first' if i == 0 else 'your second'} number: "))
                num_digits.append(x)
                break
            except ValueError:
                print("enter a valid numeric digit and try again!")
    return num_digits

def calc_add():
    nums = take_numbers_for_calculation()
    result_sums = nums[0] + nums[1]
    return result_sums

def calc_sub():
    nums = take_numbers_for_calculation()
    result_diff = nums[0] - nums[1]
    return result_diff
    

def calc_prd():
    nums = take_numbers_for_calculation()
    result_mult = nums[0] * nums[1]
    return result_mult

def calc_div():
    while True:
        try:
            nums = take_numbers_for_calculation()
            result_divi = nums[0] / nums[1]
            break
        except ZeroDivisionError:
            print("cannot divide by zero!")
    return result_divi


result = calc_div()
print(result)





