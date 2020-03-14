from re import search

def password_checker(passwords):
    '''
        From a sequence of comma separated passwords inputed, only prints those that meet the following criteria, separated by commas:
            1. Are between 6 - 12 characters long
            2. Contain atleast 1 number
            3. Contain atleast 1 lower and 1 upper case letter
            4. Contain atleast 1 special character / non-alphanumeric character
            5. Contain no spaces
    '''

    password_list = passwords.split(',')
    validation_patterns = ['[0-9]+', '[a-z]+', '[A-Z]+', r'\W+']
    checks_passed = 0
    results_list = []

    for password in password_list:
        clean_password = password.strip()

        for pattern in validation_patterns:
            if 6 <= len(clean_password) <= 12:
                if search(pattern, clean_password):
                    checks_passed += 1

        if checks_passed == 4:
            results_list.append(password)

        checks_passed = 0

    return ','.join([str(x) for x in results_list])
