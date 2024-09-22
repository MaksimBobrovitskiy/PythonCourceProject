''' https://leetcode.com/problems/longest-substring-without-repeating-characters?envType=problem-list-v2&envId=string'''

# моё для проверок
s="dvdf"
ans=s[0]
maxi=0
for i in range(0,len(s)):
    
    if not(s[i] in ans):
        print("v", ans)
        ans=ans+s[i]
        print("z", ans)
    else:
        maxi=max(len(ans),maxi)
        ans = ans[ans.find(s[i])+1:]+s[i]
    print(s[i], " ", ans)
print(ans)
print(max(maxi,len(ans)))

# что вставлено туда
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         if len(s)!=0:
#             ans=s[0]
#             maxi=0
#             for i in range(0,len(s)):
#                 print(s[i])
#                 if not(s[i] in ans):
#                     ans=ans+s[i]
                    
#                 else:
#                     maxi=max(len(ans),maxi)
#                     ans = ans[ans.find(s[i])+1:]+s[i]
          
#             return(max(maxi,(len(ans))))
            
#         else:
#             return 0



        

