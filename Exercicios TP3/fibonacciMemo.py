def fibonacci_memo(num, memo={}):
    if num<=1:
        return num
    if num not in memo:
        memo[num] = fibonacci_memo(num -1, memo) + fibonacci_memo(num -2, memo)
    return memo[num]