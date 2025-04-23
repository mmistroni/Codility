#https://www.codewars.com/kata/590005bab7c61748c0000039/train/python
import math

def count_nonzero_elements(last_row_elements):
    """
    Calculates the number of non-zero elements in a row where zeros are inserted 
    between every other number.

    Args:
        last_row_elements: The total number of elements in the last row.

    Returns:
        The number of non-zero elements.
    """
    if last_row_elements <= 0:
        return 0

    return (last_row_elements + 1) // 2
    

def pascal_triangle_last_row_elements(last_row_elements):
        """
        Generates Pascal's Triangle based on the number of elements in the last row.

        Args:
            last_row_elements: The number of elements in the last row.

        Returns:
            A list of lists representing Pascal's Triangle, or None if invalid input.
        """

        if last_row_elements <= 0:
            return None

        rows = last_row_elements  # The number of rows is equal to the elements in the last row.

        triangle = []
        for i in range(rows):
            row = [1]
            if i > 0:
                previous_row = triangle[i - 1]
                for j in range(len(previous_row) - 1):
                    row.append(previous_row[j] + previous_row[j + 1])
                row.append(1)
            triangle.append(row)

        return triangle

def pascal_matrix_spaced_conditional(pascal_triangle):
    """
    Creates a Pascal's Matrix with zeros inserted between elements,
    but only for rows with more than one element.

    Args:
        pascal_triangle: A list of lists representing Pascal's Triangle.

    Returns:
        A list of lists representing the spaced Pascal's Matrix.
    """

    if not pascal_triangle:
        return []

    spaced_matrix = []
    for row in pascal_triangle:
        if len(row) > 1:  # Check if the row has more than one element
            spaced_row = []
            for i, num in enumerate(row):
                spaced_row.append(num)
                if i < len(row) - 1:
                    spaced_row.append(0)
            spaced_matrix.append(spaced_row)
        else:
            spaced_matrix.append(row)  # Keep rows with one element as they are

    return spaced_matrix

def pad_with_balanced_zeros(matrix):
  """
  Pads each row in a list of lists (representing a matrix) with zeros
  at the beginning and end so that every row has the same length as the last row.

  Args:
    matrix: A list of lists, where each inner list represents a row.

  Returns:
    A new list of lists where all rows have the same length as the original
    last row, with shorter rows padded with zeros at the beginning and end.
  """
  if not matrix:
    return []

  max_len = len(matrix[-1])  # Length of the last row
  padded_matrix = []

  for row in matrix:
    row_len = len(row)
    if row_len < max_len:
      padding_needed = max_len - row_len
      padding_left = math.floor(padding_needed / 2)
      padding_right = math.ceil(padding_needed / 2)
      padded_row = [0] * padding_left + row + [0] * padding_right
      padded_matrix.append(padded_row)
    else:
      padded_matrix.append(list(row))  # Create a copy

  return padded_matrix



def pascal_matrix(n):
    # Ok step 1 we need to find the numbers
    # No we need to do research.
    non_zero = count_nonzero_elements(n)
    pt = pascal_triangle_last_row_elements(non_zero)
    p_matrix = pascal_matrix_spaced_conditional(pt)
    padded_matrix =  pad_with_balanced_zeros(p_matrix)
    return padded_matrix
        