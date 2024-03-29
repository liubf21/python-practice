import copy
from game import State, Player
from mcts import MCTS
import random # add this line


class AlphaZero(MCTS):
    """
    A modification based on pure MCTS, replacing randomly playout with using an evaluation function.
    """
    def __init__(self, start_state: State, evaluation_func, c=5, n_playout=10000):
        """
        Parameters:
            evaluation_func: a function taking a state as input and
                outputs the value in the current player's perspective.
        """
        super().__init__(start_state, c, n_playout)
        self.evaluation_func = evaluation_func

    def get_leaf_value(self, state: State):
        # TODO
        # 注意要考虑结束的情况
        # 注意此时是落子后的局面，而
        end, winner = state.game_end()
        value = None
        player = state.get_current_player()
        if end:
            if winner == -1:
                value = 0
            else:
                value = (1 if winner == player else -1)
        else:
            value = self.evaluation_func(state)
        # 在 expand 中会以AI视角进行转换(取反)
        return value


class AlphaZeroPlayer(Player):
    """AI player based on MCTS"""
    def __init__(self, evaluation_func, c=5, n_playout=2000):
        super().__init__()
        self.evaluation_func = evaluation_func
        self.c = c
        self.n_playout = n_playout

    def get_action(self, state: State):
        mcts = AlphaZero(state, self.evaluation_func, self.c, self.n_playout)
        # print("n_playout",self.n_playout)
        for n in range(self.n_playout):
            # print("n",n)
            state_copy = copy.deepcopy(state)
            mcts.playout(state_copy)
        return max(mcts.root.children.items(),
                   key=lambda act_node: act_node[1].n_visits)[0]
