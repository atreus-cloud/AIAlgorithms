# benchmark.py
import chess
import time
from minimax import minimax, alphabeta, minimax_nodes, alphabeta_nodes

board = chess.Board()
depth = 3

# --- Minimax ---
minimax_nodes = 0
start = time.time()
_, move1 = minimax(board, depth, board.turn)
minimax_time = time.time() - start

# --- Alpha-Beta ---
alphabeta_nodes = 0
start = time.time()
_, move2 = alphabeta(board, depth, -float('inf'), float('inf'), board.turn)
alphabeta_time = time.time() - start

# --- Results ---
print(f"Minimax move: {move1}")
print(f"AlphaBeta move: {move2}")
print("-----")
print(f"Minimax time: {minimax_time:.4f}s | Nodes: {minimax_nodes}")
print(f"AlphaBeta time: {alphabeta_time:.4f}s | Nodes: {alphabeta_nodes}")
