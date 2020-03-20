# Use of get() and setdefault methods
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'pretzels': 4}}
totals = {}

def item_total():
    for persons_basket in allGuests.values():
        for item, count in persons_basket.items():
            if item not in totals:
                totals.setdefault(item, count)
            else:
                totals[item] = totals.get(item, 0) + count

    print(totals)

# item_total()

# Counting the char occurrences in a string
string = '#This is a string for the char count test 1'
char_count = {}

for char in string:
    char_count.setdefault(char, 0)
    char_count[char] += 1
char_count