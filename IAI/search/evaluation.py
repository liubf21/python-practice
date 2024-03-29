"""
Evaluation functions
"""


def dummy_evaluation_func(state):
    return 0.0


def distance_evaluation_func(state):
    player = state.get_current_player()
    info = state.get_info()
    score = 0.0
    for p, info_p in info.items():
        if p == player:
            score -= info_p["max_distance"] # The bigger is the max_distance, the worse is the state
        else:
            score += info_p["max_distance"]
    return score


def detailed_evaluation_func(state):
    # TODO
    player = state.get_current_player() # the score is calculated from the perspective of the current player
    info = state.get_info()
    score = 0.0 # score is [-1, 1]
    will_win = False
    will_loss = False
    for p, info_p in info.items():
        if p == player: # the probability to win
            if info_p["live_four"] > 0 or info_p["four"] > 0:
                will_win = True # return 0.99 # guarantee to win 
                # 不应当在此直接返回，会和对手的活四产生顺序问题
            score -= info_p["max_distance"]
            score += info_p["live_three"] * 15
            score += info_p["three"] * 2
            score += info_p["live_two"] * 3
        else: # the risk to lose
            # 从当前玩家的角度，对手有活四，那么当前玩家必输 
            if info_p["live_four"] > 0:
                will_loss = True # return -1
            score += info_p["max_distance"]
            # 对手有冲四或活三，都必须封堵
            score -= info_p["four"] * 16
            score -= info_p["live_three"] * 14 # very dangerous
            score -= info_p["three"] * 3
            score -= info_p["live_two"] * 5
    if will_win: # 己方优先级更高
        score = 99
    elif will_loss:
        score = -100
    # print("score",score)
    score = score / 100 # normalize to [-1, 1]
    return score


def get_evaluation_func(func_name):
    if func_name == "dummy_evaluation_func":
        return dummy_evaluation_func
    elif func_name == "distance_evaluation_func":
        return distance_evaluation_func
    elif func_name == "detailed_evaluation_func":
        return detailed_evaluation_func
    else:
        raise KeyError(func_name)
