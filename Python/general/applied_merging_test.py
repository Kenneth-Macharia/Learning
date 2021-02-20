records = [
    "Equipment ONLY - Lumiere Technologies",
    "Lumiere Technologies",
    "Lumiere Tech, Inc.",
    "Mendes Metal SA - Central Office",
    "*** DO NOT USE *** Mendes Metal",
    "Mendes Metal, SA",
    "Ship to Klapisch Aerospace gmbh",
    "Klapisch Aero, gmbh Munich",
    "Klapisch Aerospace tech (use Klapisch Aero, gmbh Munich acct 84719482-A)"
]


def merge_duplicates(records):

    if records:
        seen = {}

    for i in range(0, len(records)):
        word_list = []
        word_list = records[i].split()

        for j in range(0, len(records)):
            if i != j:
                for word in word_list:
                    if word in records[j] and word.isalpha() \
                            and word not in seen.keys():
                        if len(records[i]) > len(records[j]):
                            seen[word] = records[j]
                        else:
                            seen[word] = records[i]
                        break

                    elif word in records[j] and word.isalpha() \
                            and word in seen.keys():
                        if len(seen[word]) > len(records[j]):
                            seen[word] = records[j]
                        break

    return [v for v in seen.values()]


print(merge_duplicates(records))
