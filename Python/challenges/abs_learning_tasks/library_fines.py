'''
Determine the fine for a book returned late to a library based on the following:
1. If returned on or before the expected day, fine = 0
2. If returned after expected day but within the expected month, fine = 15 * days late
3. If returned after expected month but within expected year, fine = 30 * days late
4. If returned after the expeced year, fine = 30000
'''

days_of_months = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }

def leap_year_check(year):
    result = 28

    if year % 100 != 0: # Check non-century leap year
        if year % 4 == 0:
            result = 29
    else: # Check century leap year
        if year % 400 == 0:
            result = 29

    return result

def days_between_months(date_a, date_e):
    # Less than 1 full month
    if date_a[1] - date_e[1] < 2:
        total_days = (days_of_months[date_e[1]] - date_e[0]) + date_a[0]

    # late by more than 1 full month but less than 12 months
    elif date_a[1] - date_e[1] >= 2:
        full_months = (date_a[1] - date_e[1]) - 1
        start_month = date_e[1] + 1

        full_months_days = 0

        for month in range(start_month, (start_month+full_months)):
            if month == 2:
                days_of_months[2] = leap_year_check(date_e[2])

            full_months_days += days_of_months[month]

        total_days = full_months_days + date_a[0] + (
            days_of_months[date_e[1]] - date_e[0])

    return total_days

def calculate_fine(date_a, date_e):
    fine = 0

    # fine == 0; if returned on of before due date: NO ACTION REQUIRED
    # ie: Ya == Ye, Ma == Me, Da <= De

    # fine == 15 hackos * days late; if returned after due date but within calendar month and year of due date.
    # ie: Ya == Ye, Ma == Me, Da > De
    if date_a[2] == date_e[2] and date_a[1] == date_e[1] and date_a[0] > date_e[0]:
        fine = 15 * (date_a[0] - date_e[0])

    # fine == 500 hackos * days late; if returned after calendar month but within calendar year of due date.
    # ie: Ya == Ye, Ma > Me: straddling two months or late by more than 1 full month
    elif date_a[2] == date_e[2] and date_a[1] > date_e[1]:
        fine = 50 * days_between_months(date_a, date_e)

    # fine == 1000 hackos; if returned after calendar year of due date
    # ie: Ya > Ye: late by more than 1 full year (> 12 months)
    elif date_a[2] > date_e[2]:
        months_in_first_year = 12 - date_e[1]
        months_in_second_year = date_a[1]
        total_months = months_in_first_year + months_in_second_year

        if total_months > 12 or (date_a[2] - date_e[2]) >= 2:
            fine = 30000
        else:
            # Months between straddled years are less than 12
            fine = 500 * days_between_months(date_a, date_e)

    return fine

if __name__ == '__main__':
    date_a = list(map(int, input().split(' ')))
    date_e = list(map(int, input().split(' ')))
    print(calculate_fine(date_a, date_e))