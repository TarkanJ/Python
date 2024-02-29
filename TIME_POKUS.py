class MyTime:
    def __init__(self,time=[0,0]):
        self.time = time
    
    def get_mins(self):
        return(self.time[0]*60+self.time[1])
    
    def mins_to_time(mins):
        return([mins//60,mins%60])

""" VSTUP - Jak to ma fungovat!!!
t1 = MyTime([1,20])
mins = t1.get_mins()
mins_to_time(mins)
"""