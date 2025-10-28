import bisect
import sys
from typing import Optional

from utils import load_sequence_from_json


def lis_nlogn(sequence: list[int]) -> list[int]:
    """
    O(n log n) LIS (patience / tails method) returning one LIS.
    Time: O(n log n), Space: O(n)
    """
    n: int = len(sequence)
    if n == 0:
        return []

    # tails_values[len-1] = smallest tail value for an increasing subsequence of length `len`
    tails_values: list[int] = []
    # tails_idx[len-1] = index in `sequence` of that tail value
    tails_idx: list[int] = []
    # prev[i] = index of predecessor of sequence[i] in the LIS ending at i
    prev: list[Optional[int]] = [None] * n

    for i, val in enumerate(sequence):
        # find insertion point (first >= val) to maintain strictly increasing subsequence
        # for strictly increasing we use bisect_left on val
        pos: int = bisect.bisect_left(tails_values, val)

        if pos == len(tails_values):
            tails_values.append(val)
            tails_idx.append(i)
        else:
            tails_values[pos] = val
            tails_idx[pos] = i

        # set predecessor if pos > 0
        if pos > 0:
            prev[i] = tails_idx[pos - 1]

    # Reconstruct LIS indices: start from last tail index
    lis_indices: list[int] = []
    cur_idx: Optional[int] = tails_idx[-1] if tails_idx else None
    while cur_idx is not None:
        lis_indices.append(cur_idx)
        cur_idx = prev[cur_idx]
    lis_indices.reverse()

    # Map indices to values
    return [sequence[idx] for idx in lis_indices]


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: uv run python/lis_naive.py <N>")
        sys.exit(1)

    n = int(sys.argv[1])
    file_path = f"data/sequence_{n}.json"

    try:
        sequence = load_sequence_from_json(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        print("Run 'uv run python/generator.py' to generate the data.")
        sys.exit(1)

    result = lis_nlogn(sequence)

    print(f"LIS length = {len(result)}")
    # print(f"LIS = {result}")


if __name__ == "__main__":
    main()
