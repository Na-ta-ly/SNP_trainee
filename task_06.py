class WrongNumberOfPlayersError(BaseException):
    pass


class NoSuchStrategyError(BaseException):
    pass


def rps_game_winner(test_combination: list[list[str]]) -> str:
    if len(test_combination) != 2:
        raise WrongNumberOfPlayersError

    combo_code = {'P': 0,
                  'S': 1,
                  'R': 2}
    if (test_combination[0][1] not in combo_code.keys() or
            test_combination[1][1] not in combo_code.keys()):
        raise NoSuchStrategyError

    for item in test_combination:
        item.append(combo_code[item[1]])

    if (test_combination[0][2] >= test_combination[1][2] or
            (test_combination[0][2] == 0 and test_combination[1][2] == 2)):
        result = ' '.join([test_combination[0][0], test_combination[0][1]])
    else:
        result = ' '.join([test_combination[1][0], test_combination[1][1]])

    return result
