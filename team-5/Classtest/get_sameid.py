import os
pds=[]
rg=range(0,10)

for first in rg:
    if first!=7:
        continue
    for second in rg:
        if second!=1:
            continue
        for three in rg:
            if three >2:
                continue
            for four in rg:
                for five in rg:
                    if five!=0:
                        continue
                    for six in rg:
                        if six >3:
                            continue
                        for seven in rg:
                            for eight in rg:
                                num= "%s%s%s%s%s%s%s%s"%(first,second,three,four,five,six,seven,eight)
                                pds.append('201'+num)

file_object = open('F:/456.txt', 'w')
file_object.writelines(['%s%s' % (x, os.linesep) for x in pds])
file_object.close()

