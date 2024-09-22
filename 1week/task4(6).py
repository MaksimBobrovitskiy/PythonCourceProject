s = "ABCED"
numRows = 4
c = numRows+numRows-2
print(c)
ans=''
if len(s)<=numRows or (c == 0):
    print(s)
else:
    for k in range (numRows):
        print (k)
        for i in range(k,len(s),c):
            print (s[i])
            ans+=s[i]
            
            if k>0 and k!=(numRows-1):
                if (numRows-k-1)==1:
                    if (i+2)<len(s):
                        ans+=s[i+2]
                
                else:
                    if (i+(numRows-k)*2-1)<=len(s):
                        ans+=s[i+(numRows-k-1)*2]
                        print(s[i+(numRows-k-1)*2])


print(ans)