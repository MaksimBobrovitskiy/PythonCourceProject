class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        ans=0
        zn=1
        zn1=0
        zn2=0
        startint=0
        endint=0
        if (s==""): return (ans)
        numers="0123456789"
        for i in range (n):
            if (s[i] in numers):
                startint=i
                break
            else:
                if(not((s[i]==' ') or s[i]=='-' or s[i]=='+')):
                    return ans
                elif (s[i]=='-' and zn2==0): 
                    zn=zn*-1
                    zn1=i
                    zn2=1
                elif (s[i]=='+' and zn2==0): 
                    zn1=i
                    zn2=1
        if(zn2 and zn1+1!=startint):return(ans)                                      
        if (startint==0  and not(s[0] in numers)):return (ans)          
        for i in range (startint,n):
            if(not(s[i]in numers)):
                endint=i
                break    

        if (endint==0): 
            endint=n
        ch=s[startint:endint]
        print(startint,endint)
        print(ch)
        ans=int(ch)*zn
        if(ans<-2**31):ans=-2**31
        if(ans>2**31-1): ans=2**31-1
        return (ans)