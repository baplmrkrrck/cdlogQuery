import sys,time,os,json,datetime,operator

#SELECT * FROM cddata WHERE Date > 2019-01-01 and Date < 2019-01-20
dateCount = {}
for root,dirs, files in os.walk('data'):
    #print(root,dirs,files)
    path = root.split(os.sep)
    for fn in files:
        fp = root+os.sep+fn
        print(fp)
        f = open(fp, 'r')
        for line in f:
            data = json.loads(line)
            payload = data['payload']
            payload = json.loads(payload)
#            print(payload['received'])
            k = payload['received'].split('T')[0]
            date = k.split("-")
            if date[0] == '2019' and date[1] == "01" and (date[2] == '01' or date[2] == '02'):
                print (k)
                if k in dateCount.keys():
                    dateCount[k]+=1
                else:
                    dateCount[k] = 1

# 0 == key , 1 == value
sorted_dc = sorted(dateCount.items(),key=operator.itemgetter(1),reverse=True)

print(sorted_dc)

file = 'dateCount.txt'
f = open(file, mode='a')
for row in dateCount:
    f.write(row + "\n")
