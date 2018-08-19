'''
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
'''


class Solution(object):
    seen = {}

    def find_equations(self, number_string, target):
        matches = []
        stack = [(0, None, number_string[0], number_string[1:], number_string[0])]
        while stack:
            running_total, multiplier, operand, remainder, equation = stack.pop()

            # compute the realized total so far, if there's no remainder then
            # that's the answer to our equation, else we can use this
            # value as the 'running_total' for the next iteration
            total_with_multiplication = running_total + (int(operand) if multiplier is None else multiplier * int(operand))
            if not remainder:
                if total_with_multiplication == target:
                    matches.append(equation)
                continue

            digit = remainder[0]
            remainder = remainder[1:]

            # okay, we still have more digits, so we have 3 options here:

            # 1. start a new addition or subtraction. multiplications will be moved to the total
            stack.append((total_with_multiplication, None, '+' + digit, remainder, equation + '+' + digit))
            stack.append((total_with_multiplication, None, '-' + digit, remainder, equation + '-' + digit))

            # 2. start a new multiplication. running multiplications will not yet be moved to the total
            new_multiplier = int(operand) * (multiplier if multiplier is not None else 1)
            stack.append((running_total, new_multiplier, digit, remainder, equation + '*' + digit))

            # 3. instead of starting a new addition/subtraction/multiplication, just append to current operand
            if int(operand) != 0:
                stack.append((running_total, multiplier, operand + digit, remainder, equation + digit))
        return matches

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # check for some short circuits so we can avoid doing the full computation
        if not num or num == str(-target):
            return []
        if num == str(target):
            return [num]

        # GO!
        return self.find_equations(num, target)
