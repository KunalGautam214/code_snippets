# Find the minimum currency notes return to the customer.
# 2000, 500, 200, 100, 50, 20, 10, 5, 1
# Input: 4986
# Output: {2000: 2, 500: 1, 200: 2, 50: 1, 20: 1, 10: 1, 5: 1, 1: 1}

from collections import Counter

customer_notes = 4886
currency_notes = [2000, 500, 200, 100, 50, 20, 10, 5, 1]
exchange = Counter()
i = 0
while customer_notes != 0:
    if customer_notes >= currency_notes[i]:
        exchange[currency_notes[i]] += 1
        customer_notes -= currency_notes[i]
    elif customer_notes < currency_notes[i]:
        i += 1

print(dict(exchange))

