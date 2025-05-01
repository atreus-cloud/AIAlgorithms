# Chess AI: Minimax vs Alpha-Beta Pruning

This project compares two classical game tree search algorithms — **Minimax** and **Alpha-Beta Pruning** — in a simple chess environment using the [`python-chess`](https://pypi.org/project/python-chess/) library.

---

## Files

- `minimax.py`: Implements both Minimax and Alpha-Beta pruning algorithms with node counting and evaluation logic.
- `benchmark.py`: Measures and compares time and node counts for both algorithms.
- `AI.py`: Generates the video for both the Agents.

---

## Algorithms

- **Minimax**: Explores the full game tree up to a fixed depth assuming optimal opponent moves.
- **Alpha-Beta Pruning**: Prunes branches that cannot influence the final decision, reducing unnecessary computations.

---

## How to Run

### 1. Install Dependencies

```bash
pip install chess imageio pillow cairosvg 
```

### 2. Run for the benchmark

```
python3 benchmark.py
```

### 2. Run for the video generation

```
python3 AI.py
```

## Future Enhancements

- Add move ordering heuristics
- Introduce opening books
- Implement quiescence search or transposition tables



