import json
from pathlib import Path


def save_sequence_to_json(
    sequence: list[int],
    path: str | Path,
) -> None:
    """
    Save a integer sequence to a JSON file.

    Args:
        sequence: A integer list.
        path: Path where the JSON file will be saved.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(sequence, f, indent=2)


def load_sequence_from_json(
    path: str | Path,
) -> list[int]:
    """
    Load a sequence from a JSON file.

    Args:
        path: Path to the JSON file.

    Returns:
        A integer list.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
