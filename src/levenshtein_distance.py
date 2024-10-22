# https://gemini.google.com/app/bcafb042f0ba46a5
# solved with LLM assistance

def levenshtein(str1, str2):
  """Calculates the Levenshtein distance between two strings.

  Args:
    str1 (str): The first string.
    str2 (str): The second string.

  Returns:
    int: The Levenshtein distance between the two strings.  

  """

  m = len(str1)
  n = len(str2)

  dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0:
        dp[i][j] = j
      elif j == 0:
        dp[i][j] = i
      elif str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1]
      else:
        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

  return dp[m][n]