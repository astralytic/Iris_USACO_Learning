#Sat Sep 5, 2026


def ternary_coins(n):
  if n == 1:
    return 3
  if n == 2:
    return 4
  if n == 3:
    return 5
  return 3 * ternary_coins(n - 3)

ternary_coins(9)

#SO if I wanted to make it binary  coins...

def binary_coins(n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  return 2 * binary_coins(n - 2)

binary_coins(8)
