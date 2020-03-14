'''
k个'<'，n-k-1个'>'，1到n的排列
i表示当前有几个数，j表示在当前i个数构成的全排列中，有j个'<'
dp[i][j]表示当前i个数中有j个‘<’的全排列有多少种
'''
n, k = [int(each) for each in input().split()]
dp = [1, 0]
for i in range(2, n+1):
  new_dp = [1] + [0] * i
  for j in range(1, i):
    new_dp[j] = dp[j] + dp[j-1] + dp[j] * j + dp[j-1] * (i-j-1)
  dp = new_dp
print(dp[k] % 2017)
