
test_candies_1 = [3, 8, 1, 3, 9, 5, 5, 3, 6, 9, 11, 4]

test_candies_2 = [1, 8, 2, 8, 5, 4]

test_candies_3 = [1, 2, 8, 3]

MINIMUM = - 65536

"""
The List 'candies' represent the List of the candle lengths. 
You can input different sequences to test
"""

candies = test_candies_3
candies_number = len(candies)

"""
'each_situation' is a state matrix.
The value of each_situation[x][y] represents the maximum length that the protagonist can obtain in the remaining candles
- When the indexes of remaining candles are from x to y
"""
each_situation = [[MINIMUM for col in range(candies_number)] for row in range(candies_number)]


def solution(col, row, turn):
    length = row - col + 1

    # 'a' represents the turn of the protagonist to take candle
    if turn == "a":
        if length == 1:
            each_situation[col][row] = candies[col]
            return candies[col]
        else:
            take_left = each_situation[col + 1][row] + candies[col] if each_situation[col + 1][row] > MINIMUM else solution(col + 1, row, 'b') + candies[col]
            take_right = each_situation[col][row - 1] + candies[row] if each_situation[col][row - 1] > MINIMUM else solution(col, row - 1, 'b') + candies[row]
            each_situation[col][row] = take_left if take_left > take_right else take_right
            return each_situation[col][row]

    # 'b' represents the opponent's turn to take candle
    elif turn == 'b':
        if length == 1:
            each_situation[col][row] = 0 - candies[col]
            return each_situation[col][row]
        else:
            take_left = each_situation[col + 1][row] - candies[col] if each_situation[col + 1][row] > MINIMUM else solution(col + 1, row, 'a') - candies[col]
            take_right = each_situation[col][row - 1] - candies[row] if each_situation[col][row - 1] > MINIMUM else solution(col, row - 1, 'a') - candies[row]
            each_situation[col][row] = take_left if take_left < take_right else take_right
            return each_situation[col][row]

    else:
        return 0


total_length = sum(candies)
d_value = solution(0, candies_number - 1, 'a')

# The final_length is the best length
final_length = (total_length - d_value)/2 + d_value

print("The maximum lenth difference is:")
print(solution(0, candies_number - 1, 'a'))

print("\nThe state matrix is:")
print(each_situation)

print("\nThe best length is:")
print(final_length)
