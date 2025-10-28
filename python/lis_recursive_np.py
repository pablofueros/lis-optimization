# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "numpy",
# ]
# ///
import sys

import numpy as np  # type: ignore
from utils import load_sequence_from_json


def lis_recursive_np(
    sequence: np.ndarray,
    previous: float = float("-inf"),
    index: int = 0,
) -> np.ndarray:
    """
    Compute the Longest Increasing Subsequence (LIS)
    using a naive recursive approach (O(2^n)) with NumPy.

    Args:
        sequence: Input sequence as NumPy array.
        previous: Last element considered in the subsequence.
        index: Current position in the sequence.

    Returns:
        NumPy array containing the LIS.
    """
    # Base case: end of sequence
    if index == len(sequence):
        return np.array([], dtype=sequence.dtype)

    # Option 1: skip current element
    subseq_excluding = lis_recursive_np(sequence, previous, index + 1)

    # Compute the current element once
    current = sequence[index]

    # Option 2: include current element if it's greater than the previous one
    if current > previous:
        subseq_including = np.concatenate(
            (
                [current],
                lis_recursive_np(
                    sequence,
                    current,
                    index + 1,
                ),
            )
        )
        if len(subseq_including) > len(subseq_excluding):
            return subseq_including

    return subseq_excluding


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: uv run python/lis_recursive.py <N>")
        sys.exit(1)

    n = int(sys.argv[1])
    file_path = f"data/sequence_{n}.json"

    try:
        sequence = np.array(load_sequence_from_json(file_path))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        print("Run 'uv run python/generator.py' to generate the data.")
        sys.exit(1)

    result = lis_recursive_np(sequence)

    print(f"LIS length = {len(result)}")
    print(f"LIS = {result}")


if __name__ == "__main__":
    main()
