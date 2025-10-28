import random
import sys
from pathlib import Path

from utils import save_sequence_to_json

# Global seed for reproducibility
SEED = "5061626c6f20617420507974686f6e2042696c62616f203230323521"
random.seed(SEED)


def generate_sequence(
    n: int,
    min_val: int = 0,
    max_val: int = 1_000,
) -> list[int]:
    """
    Generate a reproducible random sequence of integers.

    Args:
        n: Number of elements in the sequence.
        min_val: Minimum integer value.
        max_val: Maximum integer value.

    Returns:
        List of random integers.
    """
    return [random.randint(min_val, max_val) for _ in range(n)]


def generate_and_save_sequence(n: int) -> None:
    """
    Generate a sequence of length n and save it to a JSON file.
    """
    if Path(f"data/sequence_{n}.json").exists():
        print(f"⚠️  Sequence of length {n} already exists. Skipping generation.")
        return
    sequence = generate_sequence(n)
    save_sequence_to_json(sequence, f"data/sequence_{n}.json")
    print(f"✅ Generated sequence of length {n}")


def generate_all_datasets() -> None:
    """
    Generate multiple reproducible datasets of different sizes.
    - small (for slow O(2^n) and O(n²))
    - medium (for O(n²))
    - large (for O(n log n) and benchmarking)
    """
    Path("data").mkdir(exist_ok=True)

    # Define dataset sizes
    sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Generate and save datasets
    for n in sizes:
        generate_and_save_sequence(n)


def generate_results_directory() -> None:
    """
    Create the results directory if it doesn't exist.
    """
    Path("results").mkdir(exist_ok=True)
    print("✅ Results directory created under /results")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            generate_and_save_sequence(n)
        except ValueError:
            print("Error: Please provide a valid integer argument")
    else:
        generate_all_datasets()
        generate_results_directory()
