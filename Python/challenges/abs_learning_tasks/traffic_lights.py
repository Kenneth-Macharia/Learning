from time import sleep

market_2nd = {'ns': 'green', 'ew': 'red'}

def switch_lights(intersection):
    seq_list = []
    keys = list(intersection.keys())
    values = list(intersection.values())

    # Find the light that is green, save it as 1st and switch it to yellow
    seq_list.append(keys[values.index('green')])
    intersection[seq_list[0]] = 'yellow'

    print(f'{seq_list[0]} lights are yellow....')
    sleep(4)

    # Find the light that is red, save it as 2nd and switch it to yellow
    seq_list.append(keys[values.index('red')])
    intersection[seq_list[1]] = 'yellow'

    print(f'{seq_list[1]} lights are yellow....')
    sleep(2)

    # Find the light that was yellow first and switch to red
    intersection[seq_list[0]] = 'red'

    print(f'{seq_list[0]} lights are red!')
    sleep(5)

    # Find the light that was yellow second and switch to green
    intersection[seq_list[1]] = 'green'

    print(f'{seq_list[1]} lights are green.')
    sleep(10)

    assert 'red' in intersection.values(), 'Neither light is red! ' + str(intersection)
    assert 'green' in intersection.values(), 'Neither light is green! ' + str(intersection)

while True:
    print(f'\n-------- New Cycle---------')
    switch_lights(market_2nd)