import sys

from utils import load_sequence_from_json


def lis_recursive(
    sequence: list[int],
    previous: float = float("-inf"),
    index: int = 0,
) -> list[int]:
    """
    Compute the Longest Increasing Subsequence (LIS)
    using a naive recursive approach (O(2^n)).

    Args:
        sequence: Input sequence of integers.
        previous: Last element considered in the subsequence.
        index: Current position in the sequence.

    Returns:
        Length of the LIS.
    """
    # Base case: end of sequence
    if index == len(sequence):
        return []

    # Option 1: skip current element
    subseq_excluding = lis_recursive(sequence, previous, index + 1)

    # Option 2: include current element if it's greater than the previous one
    subseq_including = []
    if sequence[index] > previous:
        subseq_including = [sequence[index]] + lis_recursive(
            sequence,
            sequence[index],
            index + 1,
        )

    # Return the longer subsequence
    return (
        subseq_including
        if len(subseq_including) > len(subseq_excluding)
        else subseq_excluding
    )


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: uv run python/lis_recursive.py <N>")
        sys.exit(1)

    n = int(sys.argv[1])
    file_path = f"data/sequence_{n}.json"

    try:
        sequence = load_sequence_from_json(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        print("Run 'uv run python/generator.py' to generate the data.")
        sys.exit(1)

    result = lis_recursive(sequence)

    print(f"LIS length = {len(result)}")
    print(f"LIS = {result}")


if __name__ == "__main__":
    main()
