class Time:
    def __init__(self,hrs,mins):
        self.hrs=hrs
        self.mins=mins

    def addTime(t1,t2):
        t3=Time(0,0)
        if t1.mins+t2.mins>60:
            t3.hrs=(t1.mins+t2.mins)/60
        t3.hrs=t3.hrs+t2.hrs+t1.hrs
        t3.mins=(t1.mins+t2.mins)-(((t1.mins+t2.mins)/60)*60)
        return t3

    def displayTime(self):
        print("Time is: ",self.hrs,"hours and",self.mins,"minutes")

    def displayMinute(self):
        print((self.hrs)*60 + self.mins)

A=Time(2,50)
B=Time(1,20)
C=Time.addTime(A,B)
C.displayTime()
C.displayMinute()



