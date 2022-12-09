# Suppose we have coin denominations of [1, 2, 5] and the total amount is 7. We can make changes in the following 6 ways:
def solve_coin_change(denominations, amount):
  solution = [0] * (amount + 1)
  solution[0] = 1
  for den in denominations:
    for i in range(den, amount + 1):
      solution[i] += solution[i - den] 

  return solution[len(solution) - 1]
    
denominations = [1, 2, 5]
amount = 7
result = solve_coin_change(denominations, amount)
# printing the answer
print("solve_coin_change(" + str(denominations) + ', ' + str(amount) + ') = ', end = '' )
print(result)