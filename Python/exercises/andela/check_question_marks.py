def q_mark_checker(input):
    check = False

    if input != '' and isinstance(input, str):
        analysis_list = []
        num_bounds = []
        q_marks = ''

        for ch in input:
            if ch.isdigit() and len(num_bounds) == 0:
                num_bounds.append(ch)

            elif ch.isdigit() and len(num_bounds) == 1:
                if int(num_bounds[0]) + int(ch) == 10:
                    analysis_list.append(((int(num_bounds[0]) + int(ch)), len(q_marks)))
                num_bounds = [ch]
                q_marks = ''

            elif ch == '?' and len(num_bounds) == 1:
                q_marks += ch

        for index, (sum, q_count) in enumerate(analysis_list):
            if q_count == 3:
                check = True
            else:
                check = False

    return check