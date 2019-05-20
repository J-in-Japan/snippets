# Calculate the number of steps required to convert word a into word b

word_a = 'printer'
word_b = 'scanner'

# my initial brute force solution
# doesn't tak
def steps_to_convert(a: str, b: str) -> int:
    longest = max(len(a), len(b))
    steps = 0
    for i in range(longest):
        print(f'index: {i}')
        if i < len(a) and i < len(b):
            if b[i] != a[i]:
                print(f'  replace {a[i]} with {b[i]}')
                steps += 1
        else:
            if len(a) > len(b):
                print(f'  delete extra char {a[i]}')
            if len(b) > len(a):
                print(f'  add missing char {b[i]}')
            steps += 1
    return steps

#total_steps = steps_to_convert(word_a, word_b)
#print(f'total steps: {total_steps}')


# dynamic programming mehtod
# maintain a table of calculated sub-results

def editDistDP(str1, str2): 
    m = len(str1)
    n = len(str2)
    
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m+1): 
        for j in range(n+1): 
  
            # If first string is empty, only option is to 
            # insert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])      # Replace 
  
    return dp[m][n] 
  
# Driver program 
str1 = "sunday"
str2 = "saturday"

answer = editDistDP(str1, str2)

print(answer)