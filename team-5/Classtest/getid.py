import os
name=[]
rg=range(0,10)

for first in rg:
    if first<7:
        continue
    for second in rg:
        if second >1:
            continue
        for three in rg:
            if second==0 and three == 0:
                continue
            if (second==1 and three>2):
                continue
            for four in rg:
                if four>3:
                    continue
                for five in rg:
                    if four ==0 and five ==0:
                        continue
                    if four==3 and five>1:
                        continue
                    num= "%s%s%s%s%s"%(first,second,three,four,five)
                    name.append('199'+num)


file_object = open('F:/pwd1.txt', 'w')
file_object.writelines(['%s%s' % (x,os.linesep) for x in name])
file_object.close()

