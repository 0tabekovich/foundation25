class time:
    s=0
    m=0
    sec=0
    def __init__(self,s,m,sec):
        time.s=s
        time.m=m
        time.sec=sec
    def show_time(self):
        print("{0:02d}:{1:02d}:{2:02d}".format(time.s,time.m,time.sec))
class min(time):
    def __init__(self):
        if time.m+5>=60:
           time.s+=1
           time.m=60-time.m
        else :
            time.m=time.m+5
class sec(time):
    def __init__(self):
        if time.sec+5>=60:
            time.m+=1
            time.sec=60-time.sec
        else:
            time.sec+=5

