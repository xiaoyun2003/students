import os.path
#利用反序列化模块
import pickle
def menuBase():
    print('########     1.插入学生记录      ########')
    print('########     2.删除学生记录      ########')
    print('########     3.修改学生记录      ########')
    print('########     0.返回上层菜单      ########')

def menuScore():
    print('########     1.计算学生总分      ########')
    print('########     2.根据总分排名      ########')
    print('########     0.返回上层菜单      ########')

def menuCount():
    print('########     1.求课程最高分      ########')
    print('########     2.求课程最低分      ########')
    print('########     3.求课程平均分      ########')
    print('########     0.返回上层菜单      ########')

def menu():
    print('########     1.显示基本信息     ########')
    print('########     2.基本信息管理     ########')
    print('########     3.学生成绩管理     ########')
    print('########     4.考试成绩统计     ########')
    print('########     5.根据条件查询     ########')
    print('########     0.退出             ########')
def menuSearch():
    print('########     1.按学号查询     ########')
    print('########     2.按姓名查询     ########')
    print('########     3.按性别查询     ########')
    print('########     4.按语文查询     ########')
    print('########     5.按数学查询     ########')
    print('########     6.按外语查询     ########')
    print('########     7.按总分查询     ########')
    print('########     8.按排名查询     ########')
    print('########     0.返回上层菜     ########')


def searchManage(stu):
    while True:
        print("请输入您的选择（0-8）:")
        t=["学号","姓名","性别","语文","数学","外语","总分","总分排名"]
        choice=int(input())
        if 1<=choice and choice<=8:
            z=input("请输入"+t[choice-1]+"多个用逗号分割,支持范围56-68:")
            res=[]
            find=[]
            searchStu(stu,choice,z,find)
            if len(find)==0:
                print("未找到记录")
                continue
            for x in find:
                res.append(stu[x])
            printStu(res)
        if choice==0:
            break

class Student(object):
    def __init__(self,num='',name='',gender='',score=[0,0,0],total=0,rank=0):
       self.num=num
       self.name=name
       self.gender=gender
       self.score=score
       self.total=total
       self.rank=rank
    def get(self,s):
       #这里可以简写
       p=""
       if s==1:p=self.num
       if s==2:p=self.name
       if s==3:p=self.gender
       if s==4:p=self.score[0]
       if s==5:p=self.score[1]
       if s==6:p=self.score[2]
       if s==7:p=self.total
       if s==8:p=self.rank
       return p
    def set(self,s,data):
       if s==1:self.num=data
       if s==2:self.name=data
       if s==3:self.gender=data
       if s==4:self.score[0]=int(data)
       if s==5:self.score[1]=int(data)
       if s==6:self.score[2]=int(data)
       if s==7:self.total=int(data)
       if s==8:self.rank=int(data)
        
def readFile(stu):
    file="students.txt"
    if os.path.isfile(file):
        f = open(file,'r')
        tab="\t"
        fl=f.readlines()
        if len(fl)==0:
            os.remove(file)
        for x in fl:
            s=x.split(tab)
            cjlist=[0,0,0]
            cjlist[0]=int(s[3])
            cjlist[1]=int(s[4])
            cjlist[2]=int(s[5])
            oneStu=Student(s[0],s[1],s[2],cjlist,int(s[6]),int(s[7]))
            stu.append(oneStu)
        f.close()
        return len(stu)
    else:
        print("学生成绩信息文件不存在！！！")
        return 0
    
def createFile(stu):
    file="students.txt"
    f = open(file,'w')  
    if os.path.isfile(file)==False:
        print("文件打开错误！")
        exit()
    print("*****下面将进入初始化过程，创建学生信息文件并请录入数据*****")
    while True:
        n=readStu(stu)
        if n==0:
            break
    #写入数据
    tab="\t"
    rr=""
    for x in stu:
        rr=x.num+tab+x.name+tab+x.gender+tab+str(x.score[0])+tab+str(x.score[1])+tab+str(x.score[2])+tab+str(x.total)+tab+str(x.rank)+"\n"+rr
    rr=rr.strip("\n")
    f.write(rr)
    f.close()
    return n


#这个可以存入student.py
def readStu(stu,n=100):
    oneStu = Student()
    print("请输入一个学生信息(学号为0时结束输入):")
    xh=input("学号: ")
    if checkStu(stu,xh,1)==False:
        print("学号已存在或输入错误")
        return 1
    if xh=="0":
        return 0
    xm=input("姓名: ")
    xb=input("性别: ")
    print("请输入该学生的三门课程成绩,以空格分割:")
    cj=input("")
    temp=cj.split(" ")
    if len(temp)!=3:
        print("成绩输入错误")
        return 1
    cjlist=[]
    for x in temp:
        if x.isdigit()==False:
            print("成绩输入错误")
            return 1
        cjlist.append(int(x))
    oneStu=Student(xh,xm,xb,cjlist)
    stu.append(oneStu)
    return len(stu)

def baseManage(stu):
    choice=0
    t=0
    find=[]
    oneStu=Student()
    while True:
        print("请输入您的选择（0-3）:")
        choice=int(input())
        if choice==1:
            readStu(stu)
        elif choice==2:
            print("请输入需要删除的学生学号")
            xh=input()
            deleteStu(stu,xh)
        elif choice ==3:
            print("请输入需要修改的学生学号")
            xh=input()
            res=[]
            searchStu(stu,1,xh,find)
            for x in find:
                res.append(stu[x])
            printStu(res)
            print("请输入需要修改的内容:")
            print("所有内容:0 学号:1 姓名:2 性别:3 语文:4 数学:5 外语:6 总分:7 排名:8")
            c=input()
            amendvStu(stu,stu[find[t]],int(c))
        elif choice==0:
            break
    return len(stu)

def searchStu(stu,s,condition,f):
    find=0
    #这段代码是一段超级低级的
    for x in stu:
        p=x.get(int(s))
        if ("," in condition):
            l=condition.split(",")
            for xx in l:
                if str(p)==xx:f.append(find)
        elif ("-" in condition):
            l=condition.split("-")
            if int(p) in range(int(l[0]),int(l[1])+1):f.append(find)
        else:
            if str(p)==condition:f.append(find)
        find=find+1
    return len(f)

#检查是否为空已经学号是否重复
#type 1学号 2数值 3文本
def checkStu(stu,data,type):
    if type==1:
        if data.isdigit()==False:
            return False
        for x in stu:
            if int(data)==int(x.num):
                return False
    elif type==2:
        if data.isdigit()==False:
            return False
    elif type==3:
        if len(data)==0:
            return False
    return True

#修改学生记录的函数
#吐槽:真难写
#别看这个函数的代码这么复杂这是为了实现一个非常良好的交互过程
def amendvStu(stu,oneStu,s):
    print("请输入需要修改的内容:")
    print("所有内容:0 学号:1 姓名:2 性别:3 语文:4 数学:5 外语:6 总分:7 排名:8")
    t=["学号","姓名","性别","语文","数学","外语","总分","总分排名"]
    c=0
    if s==0:
        for x in t:
            c=c+1
            while True:
                z=input("请输入新的"+x+":")
                if z=="0":
                    print("未修改记录")
                    break
                if c==1:
                    if checkStu(stu,z,1):
                        print("修改成功")
                        oneStu.set(c,z)
                        break
                    else:
                        print("输入错误,输入0结束")
                if c==2 or c==3:
                    if checkStu(stu,z,3):
                        print("修改成功")
                        oneStu.set(c,z)
                        break
                    else:
                        print("输入错误,输入0结束")
                elif 4<=c and c<=8:
                    if checkStu(stu,z,2):
                        print("修改成功")
                        oneStu.set(c,z)
                        break
                    else:
                        print("输入错误,输入0结束")
                else:
                    print("输入错误")
                
    else: 
        while True:
            z=input("请输入新的"+t[s-1]+":")
            if z=="0":
                print("未修改记录")
                break
            if s==1:
                if checkStu(stu,z,1):
                    print("修改成功")
                    oneStu.set(s,z)
                    break
                else:
                    print("输入错误,输入0结束")    
            if s==2 or s==3:
                if checkStu(stu,z,3):
                    print("修改成功")
                    oneStu.set(s,z)
                    break
                else:
                    print("输入错误,输入0结束")
            elif 4<=s and s<=8:
                if checkStu(stu,z,2):
                    print("修改成功")
                    oneStu.set(s,z)
                    break
                else:
                    print("输入错误,输入0结束")
            else:
                print("输入错误")
                
def calcuTotal(stu):
    for x in stu:
        x.total=x.score[0]+x.score[1]+x.score[2] 
    print("总分计算完成")    




def deleteStu(stu,s):
    count=0
    for x in stu:
       if int(x.num)==int(s):
           stu.pop(count)
           print("删除成功")
       count=count+1
    return len(stu)





def calcuRank(stu):
    sortStu(stu,7)
    stu=reverse(stu)
    stu[0].rank=1
    count=1
    
    for x in stu:
        print(x.total)
        if x.total==stu[count-1].total:
            x.rank=stu[count-1].rank
        else:
            count=count+1
            x.rank=count
    print("排名完成")


def reverse(stu):
    n=[0 for i in range(len(stu))]
    for i in range(int(len(stu)/2)):
        n[i]=stu[len(stu)-1-i]
        n[len(stu)-1-i]=stu[i]
    if int(len(stu)/2)!=len(stu)/2:
        n[int(len(stu)/2)]=stu[int(len(stu)/2)]
    return n
def sortStu(stu,id):
   n=len(stu)
   for x in range(n-1):
   #内层循环开始比较
       for y in range(x+1,n):
      #stu[x]在for y 循环中是代表特定的元素，stu [y]代表任意一个stu任意一个元素。
           if stu[x].get(id)>stu[y].get(id):
               #让stu[x]和stu列表中每一个元素比较，找出小的
               stu[x],stu[y]=stu[y],stu[x]


def scoreManage(stu):
    choice=0
    while True:
        print("请输入您的选择（0-2）：")
        choice=int(input())
        if choice==1:
            calcuTotal(stu)
        elif choice==2:
            calcuRank(stu)
        elif choice==0:
            break

def calcuMark(m,stu,n):
    #冒泡排序
    #这里其实不用写这么复杂，为了让代码看起来更低级
    maxlist=[0,0,0]
    minlist=[2000,2000,2000]
    yw=0
    sx=0
    yy=0
    for x in stu:
        #求最高分
        if x.score[0]>=maxlist[0]:
            maxlist[0]=x.score[0]
        if x.score[1]>=maxlist[1]:
            maxlist[1]=x.score[1]
        if x.score[2]>=maxlist[2]:
            maxlist[2]=x.score[2]
        #求最低分
        if x.score[0]<=minlist[0]:
            minlist[0]=x.score[0]
        if x.score[1]<=maxlist[1]:
            minlist[1]=x.score[1]
        if x.score[2]<=minlist[2]:
            minlist[2]=x.score[2]
        
        yw=yw+x.score[0]
        sx=sx+x.score[1]
        yy=yy+x.score[2]
    m[0][0]=maxlist[0]
    m[0][1]=minlist[0]
    m[0][2]=yw/len(stu)
    
    m[1][0]=maxlist[1]
    m[1][1]=minlist[1]
    m[1][2]=sx/len(stu)
    
    m[2][0]=maxlist[2]
    m[2][1]=minlist[2]
    m[2][2]=yy/len(stu)





def countManage(stu,n):
    choice=0
    m=[[0]*3 for i in range(3)]
    calcuMark(m,stu,n)
    while True:
        print("请输入您的选择（0-3）：")
        choice=int(input())
        if choice==1:
            s="语数外最高分"
            printMarkCourse(s,m,0)
        elif choice==2:
            s="语数外最低分"
            printMarkCourse(s,m,1)
        elif choice==3:
            s="语数外平均分"
            printMarkCourse(s,m,2)
        elif choice==0:
            break
def saveFile(stu):
    file="students.txt"
    f = open(file,'w')  
    if os.path.isfile(file)==False:
        print("文件打开错误！")
        exit()
    tab="\t"
    rr=""
    for x in stu:
        rr=x.num+tab+x.name+tab+x.gender+tab+str(x.score[0])+tab+str(x.score[1])+tab+str(x.score[2])+tab+str(x.total)+tab+str(x.rank)+"\n"+rr
    rr=rr.strip("\n")
    f.write(rr)
    print("保存成功")
    return n


def printMarkCourse(s,m,k):
    print(s)
    for i in range(3):
        print(m[i][k])
    print('')







def runMain(stu,choice,n):
    if choice==1: 
        printStu(stu,n)
    elif choice==2:
        menuBase()
        baseManage(stu)
    elif choice==3:
        menuScore()
        scoreManage(stu)
    elif choice==4:
        menuCount()
        countManage(stu,n)
    elif choice==5:
        menuSearch()
        searchManage(stu)


def printStu(stu,n=100):
    #循环输出
    tab="\t"
    stu=sorted(stu, key=lambda s: s.num) 
    print("学号"+tab+"姓名"+tab+"性别"+tab+"语文"+tab+"数学"+tab+"外语"+tab+"总分"+tab+"总分排名")
    for x in stu:
        print(x.num+tab+x.name+tab+x.gender+tab+str(x.score[0])+tab+str(x.score[1])+tab+str(x.score[2])+tab+str(x.total)+tab+str(x.rank))
    print("----------------------当前记录已全部显示完毕-------------------")


if __name__=="__main__":
    print('########     欢迎使用学生成绩系统     ########')
    #这里要求一维list
    stu=[]
    n=readFile(stu)
    if n==0:
        createFile(stu)
    n=len(stu)
    while True:
        menu()
        choice=int(input("请输入您的选择（0-5）"))
        if choice==1 or choice==2 or choice==3 or choice==4 or choice==5:
            runMain(stu,choice,n)
        elif choice==0:
            print("拜拜,么么哒")
            break
        else:
            print("输入错误，请重新输入！")
        if choice==0:
            pass
            #list排序
            sortStu(stu,1)
        #存入文件
    saveFile(stu)
        
            