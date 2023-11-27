for i in range(1,len(vBars)):
            if vBars[i]=vBars[i-1]+1:
                temp+=1
            else:
                vmax = max(temp, vmax)
                temp=1
        vmax = max(temp, vmax)