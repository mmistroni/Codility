# https://www.codewars.com/kata/6a37e118ef0c62f1772b6c6d

ORIENTATIONS = [
    (1, (0, 1), 'CW'),  # DownClockwise
    (2, (0, 1), 'CCW'), # DownCounter-Clockwise
    (3, (0, -1), 'CW'), # UpClockwise
    (4, (0, -1), 'CCW'), # UpCounter-Clockwise
    (5, (1, 0), 'CW'),  # RightClockwise
    (6, (1, 0), 'CCW'), # RightCounter-Clockwise
    (7, (-1, 0), 'CW'), # LeftClockwise
    (8, (-1, 0), 'CCW') # LeftCounter-Clockwise
]


def parse_key(key: int) -> tuple[bool, int, int]:
    """
    Parses key into:
      - is_center_out: True if positive, False if negative
      - orientation: Integer from 1 to 8
      - gap: Integer from 0 to 9
    """
    is_center_out = key > 0
    orientation = abs(key) % 10
    gap = abs(key) // 10 % 10
    return is_center_out, orientation, gap


def get_orientation_rules(orientation: int) -> tuple[tuple[int, int], str]:
    """
    Translates orientation digit (1-8) into:
      - initial_direction: (dr, dc)
      - turn_direction: 'CW' (clockwise) or 'CCW' (counter-clockwise)
    """
    for orient, direction, turn in ORIENTATIONS:
        if orient == orientation:
            return direction, turn
    raise ValueError("Invalid orientation")


def generate_spiral_path(length: int, orientation: int, gap: int) -> list[tuple[int, int]]:
    """
    Traces the spiral path from center (0, 0) outward for `length` steps,
    accounting for gap width and orientation turning rules.
    Returns ordered list of (row, col) coordinates.
    """
    pass


def get_reading_order_permutation(path: list[tuple[int, int]], is_center_out: bool) -> list[int]:
    """
    Maps text character positions along the spiral to reading-order 
    grid positions (top-to-bottom, left-to-right).
    """
    pass


def encode(plaintext: str, key: int) -> str:
    """
    Encodes plaintext using the Spaced Snail Cipher key.
    """
    pass


def decode(cipher: str, key: int) -> str:
    """
    Decodes cipher text back to plaintext using the Spaced Snail Cipher key.
    """
    pass