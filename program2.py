def decode_message(s: str, p: str) -> bool:
    s_len = len(s)
    p_len = len(p)
    
    # Create a 2D DP table
    dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
    
    # Base case: empty pattern matches empty string
    dp[0][0] = True
    
    # Handle patterns starting with '*' that match empty strings
    for j in range(1, p_len + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, s_len + 1):
        for j in range(1, p_len + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                # Character matches or '?' matches a single character
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' matches zero or more characters
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
    
    # The result is in the bottom-right corner of the DP table
    return dp[s_len][p_len]
