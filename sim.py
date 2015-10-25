# encoding: utf-8

import random

def play_game_do_not_change():
    rewards = [1,1,30]# 1 is goat, 30 is car
    random.shuffle(rewards)
    select = random.randint(0,2)
    open_gate = random.randint(0,2)
    while open_gate == select or rewards[open_gate] == 30:
        open_gate = random.randint(0,2)
    if rewards[open_gate] == 30:#used in a varietal test, in which the host will select randomly
        return 0
    else:
        if rewards[select] == 30:
            return 2
        else:
            return 1

def do_test():
    wins_car = 0
    wins_goat = 0
    total_times = 1000*1000
    effective_times = 0
    for i in range (0, total_times):
        result = play_game_do_not_change()
        if result == 2:
            effective_times += 1
            wins_car += 1
        elif result == 1:
            effective_times += 1
            wins_goat += 1
    print('effective_times:{}'.format(effective_times))
    print('wins car:{}, ({})'.format(wins_car, wins_car*1.0/effective_times))
    print('wins goat:{}, ({})'.format(wins_goat, wins_goat*1.0/effective_times))

if __name__ == '__main__':
    print(random.random())
    do_test()
