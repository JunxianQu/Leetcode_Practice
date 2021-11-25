strs = ["AA,A,10,12:01:00","AA,B,-15,12:05:00","RE,AA,EX1","RE,EX1,AA","EX1,B,-15,12:05:00","EX1,B,-20,12:07:00","RE,AA,EX1","RE,EX1,AA","RE,EX2,AA"];
records = {}
ans = []
for s in strs:
    cur_str = s.split(",")
    if len( cur_str ) == 4:
        if cur_str[0] not in records:
            records[ cur_str[0] ] =  [cur_str[1] + cur_str[2]]
        else:
            records[ cur_str[0] ].append( cur_str[1] + cur_str[2] )
        ans.append( int(cur_str[2]) )
    else:
        if cur_str[1] not in records:
            ans.append( 0 )
        else:
            tmp = 0
            source1 = records[ cur_str[1] ]
            if cur_str[2] not in records:
                ans.append( len( source1 ) )
            else:
                source2 = records[ cur_str[2] ]
                for s1 in source1:
                    if s1 not in source2:
                        tmp += 1
                ans.append( tmp )
return ans

def build( strs ):
    new_strs = []
    for s in strs:
        tmp = s.split(",")
        new_strs.append( tmp )
    new_strs = sorted( new_strs, key = lambda x: x[-1] )
    while new_strs:
        cur_str = new_strs[0]
        length = len( new_strs )
        for i in range( 1, length ):
            tmp_str = new_strs[i]
            if tmp_str[0] == cur_str[0] or tmp_str[1] != cur_str[1] or tmp_str[2] != cur_str[2]:
                continue
            time1 = cur_str[3].split(':')
            time2 = tmp_str[3].split(':')
            if abs( int(time1[0])*3600 + int(time1[1])*60 + int(time1[2]) - int(time2[0])*3600 - int(time2[1])*60 - int(time2[2]) ) <= 300:
                new_strs.pop(i)
                new_strs.pop(0)
                break
        if length == len( new_strs ):
            return False
    return True

strs = ["AA,A,10,12:01:00","AA,B,-15,12:05:00","EX1,B,-15,12:05:00","EX1,A,10,12:06:00"]
print( build( strs ) )
strs = ["AA,A,10,12:01:00","AA,A,10,12:02:00","AA,A,10,12:03:00","EX,A,10,12:05:00","EX,A,10,12:03:00","EX,A,10,12:02:00"]
print( build( strs ) )
strs = ["EX,A,10,11:59:00","AA,A,10,11:59:00","EX,A,10,12:00:00","EX,B,12,15:01:03","EX,H,-50,16:14:02","AA,A,10,11:53:00","AA,A,10,12:00:00","EX,A,10,12:01:00","AA,B,12,15:01:02","AA,H,-50,16:19:02",]
print( build( strs ) )



def build( strs ):
    strs = sorted(strs)
    ans = []
    tmp = strs[0].split(':')
    start_time = int(tmp[0])*3600 + int(tmp[1]) * 60 + float(tmp[2])//1
    count = 0
    for i in range( len( strs ) ):
        s = strs[i]
        tmp = s.split(":")
        cur_time =  int(tmp[0])*3600 + int(tmp[1]) * 60 + float(tmp[2])//1 - start_time
        if cur_time == count:
            count += 1
        elif cur_time > count:
            count = cur_time+1
            ans.append( strs[i-1] + "-" + strs[i] )
    return ans

strs = ["12:01:04.04","12:01:05.01","12:01:05.21","12:01:14.39","12:01:15.13","12:01:16.98","12:01:18.01"]
print( build( strs ) )
            
