'''https://leetcode.com/problems/multiply-strings?envType=problem-list-v2&envId=string'''
s1 ='123'
s2 ='456'
ans = 0
podans = 0
for i in range(len(s1)):
    for j in range(len(s2)):
        #print(s2[j])
        podans+=int(s1[i])*10**(len(s1)-i-1)*int(s2[j])*10**(len(s2)-j-1)
    print(podans)
    ans+=podans
    podans = 0                

print(str(ans))
