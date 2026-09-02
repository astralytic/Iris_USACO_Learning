#Tue Sep 1, 2026


def cache_coins(final_day):
  day = 1
  total = 1
  while day < final_day:
    print(f"Day {day}: {total}"
    day += 1
    total *= 2
  return total

print(f"Day 10: {cache_coins(10)}"
