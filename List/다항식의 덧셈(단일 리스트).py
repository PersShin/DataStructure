class SingleList:
    class Node:
        def __init__(self,coef=None,exp=None, link=None):
            self._coef=coef
            self._exp=exp
            self._link=link
    def __init__(self):
        self._head=None
        self._size=0
    def isNone(self):
        if(self._head is None):
            return True
        return False
    def appender_first(self,coef,exp):
        newest=self.Node(coef,exp, self._head)
        self._head=newest
        self._size+=1
    def appender_last(self, coef, exp):
        if(self.isNone()):
            self.appender_first(coef,exp)
        else:
            newest=self.Node(coef,exp)
            tail=self._head
            while(tail._link is not None):
                tail=tail._link
            tail._link=newest
            self._size+=1
    def printer(self):
        newest=self._head
        while(newest._link is not None):
            print(newest._coef,newest._exp, end=' ')
            newest=newest._link
        print(newest._coef, newest._exp)
def Sum(list_a,list_b):
    new_a=list_a._head
    new_b=list_b._head
    Summer=SingleList()
    while(new_a or new_b):
        if(new_a is None):
            Summer.appender_last(new_b._coef,new_b._exp)
            return Summer
        elif(new_b is None):
            Summer.appender_last(new_a._coef,new_a._exp)
            return Summer
        elif(new_a._exp>new_b._exp):
            Summer.appender_last(new_a._coef,new_a._exp)
            new_a=new_a._link
        elif(new_a._exp<new_b._exp):
            Summer.appender_last(new_b._coef,new_b._exp)
            new_b=new_b._link
        else:
            Summer.appender_last(new_a._coef+new_b._coef, new_a._exp)
            new_a=new_a._link
            new_b=new_b._link
    return Summer
a,b=SingleList(), SingleList()
a.appender_last(3,14)
a.appender_last(2,8)
a.appender_last(1,0)
b.appender_last(8,14)
b.appender_last(-3,10)
b.appender_last(10,6)
a.printer()
b.printer()
Summer=Sum(a,b)
Summer.printer()