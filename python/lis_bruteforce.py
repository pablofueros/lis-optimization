import sys

from utils import load_sequence_from_json


def lis_bruteforce(sequence: list[int]) -> list[int]:
    """
    Compute the Longest Increasing Subsequence (LIS)
    using a naive backtracking approach (O(2^n)).

    Args:
        sequence: Input sequence of integers.

    Returns:
        List representing the LIS.
    """
    n = len(sequence)
    best = []

    def backtrack(index: int, current: list[int]) -> None:
        nonlocal best

        # Prune: if remaining elements cannot beat current best, stop exploring
        remaining: int = n - index
        if len(current) + remaining <= len(best):
            return

        # If we reached the end, record if it's better
        if index >= n:
            if len(current) > len(best):
                best = current.copy()
            return

        # Option 1: skip current element
        backtrack(index + 1, current)

        # Option 2: take current element if it keeps the sequence strictly increasing
        if not current or sequence[index] > current[-1]:
            current.append(sequence[index])
            backtrack(index + 1, current)
            current.pop()

    backtrack(0, [])
    return best


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: uv run python/lis_bruteforce.py <N>")
        sys.exit(1)

    n = int(sys.argv[1])
    file_path = f"data/sequence_{n}.json"

    try:
        sequence = load_sequence_from_json(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        print("Run 'uv run python/generator.py' to generate the data.")
        sys.exit(1)

    result = lis_bruteforce(sequence)

    print(f"LIS length = {len(result)}")
    print(f"LIS = {result}")


if __name__ == "__main__":
    main()
