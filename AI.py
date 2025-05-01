# main.py
import chess
import chess.svg
import imageio
import cairosvg
from io import BytesIO
import chess
from minimax import minimax, alphabeta

def draw_board(board):
    svg_data = chess.svg.board(board=board, size=350)
    png_bytes = cairosvg.svg2png(bytestring=svg_data)
    image = imageio.v3.imread(png_bytes, extension='.png')
    return image

def play_game(use_alphabeta=True, depth=3):
    board = chess.Board()
    frames= []

    while not board.is_game_over():
        # print(board, "\n")
        
        frame = draw_board(board)
        frames.append(frame)

        if use_alphabeta:
            _, move = alphabeta(board, depth, -float('inf'), float('inf'), board.turn)
        else:
            _, move = minimax(board, depth, board.turn)

        print("Move played:", move)
        board.push(move)
    

    frames.append(draw_board(board))
    imageio.mimsave("minimax.mp4", frames, fps=1)
    print("video saved")
    print("Game Over:", board.result())

if __name__ == "__main__":
    # Set `use_alphabeta=False` to test minimax without pruning
    play_game(use_alphabeta=False, depth=3)

