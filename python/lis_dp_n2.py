import sys
from typing import Optional

from utils import load_sequence_from_json


def lis_dp(sequence: list[int]) -> list[int]:
    """
    O(n^2) DP algorithm that returns one Longest Increasing Subsequence.
    Time: O(n^2), Space: O(n)
    """
    n: int = len(sequence)
    if n == 0:
        return []

    # dp[i] = length of LIS ending at i
    dp: list[int] = [1] * n
    prev: list[Optional[int]] = [None] * n

    for i in range(n):
        for j in range(i):
            if sequence[j] < sequence[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # find index of maximum dp
    max_len: int = max(dp)
    max_idx: int = dp.index(max_len)

    # reconstruct LIS
    lis: list[int] = []
    idx: Optional[int] = max_idx
    while idx is not None:
        lis.append(sequence[idx])
        idx = prev[idx]
    lis.reverse()
    return lis


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

    result = lis_dp(sequence)

    print(f"LIS length = {len(result)}")
    # print(f"LIS = {result}")


if __name__ == "__main__":
    main()
