import re

# test_phrase = 'riya riya@gmail.com'
# details_list = []
# details_list.append(re.split(' ', test_phrase))
# print(details_list)

# for person in details_list:
# 	if re.search('gmail', person[1]):
# 		print(person[0])

people = [['alice', 'alice@gmail.com']]

def re_search(people):

    for person in people:
        email_split = re.split('@', person[1])

        if email_split[1] == 'gmail.com':
            print(person[0])

re_search(people)