def number_compare(num1, num2):
    answer = {0:"First is greater", 1:"Second is greater"}
    
    if num1 == num2:
        return "Numbers are equal"
    return answer.get(num1 < num2)
    
print(number_compare(1, 2))
print(number_compare(2, 1))
print(number_compare(3, 3)) 