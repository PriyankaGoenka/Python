class sum:
    def ThreeSum(self,num):
        new_list=[]
        i=0
        j=1
        k=2
        for i in range(len(num)-2):
            for j in range(len(num)-1):
                for k in range(len(num)):
                    if num[i]+num[j]+num[k]==0:
                        #tri=(num[i],num[j],num[k])
                        #print(tri)
                        new_list.append([num[i],num[j],num[k]])
        print(new_list)
ob=sum()
num=[-25,-10,-7,-3,2,4,8,10]
num=sorted(num)
ob.ThreeSum(num)
