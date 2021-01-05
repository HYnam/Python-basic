# addition_str is a string with a list of numbers separated by the + sign. Write code that uses the 
# accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You 
# should use the .split("+") function to split by "+" and int() to cast to an integer).

accumulation = []
sum_val = []

addition_str = "2+5+10+20"
str_nums = (addition_str.split("+"))
for i in str_nums:
    sum_val.append(int(i))
    accumulation.append(sum(sum_val))
    print(sum_val)