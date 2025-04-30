import random

class MinimaxAI:
    def __init__(self, depth):
        self.depth = depth
    
    def evaluate(self, state):
        ball_x, ball_y = state["ball_pos"]
        slime1_x, slime1_y = state["slime1_pos"]
        slime2_x, slime2_y = state["slime2_pos"]

        # Prefer getting the ball closer to the opponent's goal
        return -(ball_x - slime2_x) ** 2 + (ball_x - slime1_x) ** 2

    def minimax(self, state, depth, maximizing_player):
        if depth == 0 or game_over(state):
            return self.evaluate(state)
        
        if maximizing_player:
            max_eval = float('-inf')
            for child in generate_children(state, maximizing_player):
                eval = self.minimax(child, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for child in generate_children(state, maximizing_player):
                eval = self.minimax(child, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def get_move(self, slime, ball):
        # Initial game state
        state = {
            "ball_pos": (ball.rect.x, ball.rect.y),
            "slime1_pos": (slime.rect.x, slime.rect.y),
            "slime2_pos": (SCREEN_WIDTH - slime.rect.x, SCREEN_HEIGHT - slime.rect.y)
        }

        best_move = None
        best_value = float('-inf')

        for move in ["left", "right"]:
            new_state = state.copy()
            new_state["slime1_pos"] = (state["slime1_pos"][0] - 5 if move == "left" else state["slime1_pos"][0] + 5, state["slime1_pos"][1])
            value = self.minimax(new_state, self.depth, False)
            if value > best_value:
                best_value = value
                best_move = move
        return best_move

class AlphaBetaAI(MinimaxAI):
    def __init__(self, depth):
        super().__init__(depth)
    
    def alpha_beta(self, state, depth, alpha, beta, maximizing_player):
        if depth == 0 or game_over(state):
            return self.evaluate(state)

        if maximizing_player:
            max_eval = float('-inf')
            for child in generate_children(state, maximizing_player):
                eval = self.alpha_beta(child, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for child in generate_children(state, maximizing_player):
                eval = self.alpha_beta(child, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_move(self, slime, ball):
        # Initial game state
        state = {
            "ball_pos": (ball.rect.x, ball.rect.y),
            "slime1_pos": (slime.rect.x, slime.rect.y),
            "slime2_pos": (SCREEN_WIDTH - slime.rect.x, SCREEN_HEIGHT - slime.rect.y)
        }

        best_move = None
        best_value = float('-inf')

        for move in ["left", "right"]:
            new_state = state.copy()
            new_state["slime1_pos"] = (state["slime1_pos"][0] - 5 if move == "left" else state["slime1_pos"][0] + 5, state["slime1_pos"][1])
            value = self.alpha_beta(new_state, self.depth, float('-inf'), float('inf'), False)
            if value > best_value:
                best_value = value
                best_move = move
        return best_move
