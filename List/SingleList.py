class SingleList:
    class Node:
        def __init__(self,item=None, link=None):
            self._item=item
            self._link=link

    def __init__(self):
        self._head=None
        self._size=0
    def appender_first(self, item):
        newest=self.Node(item,self._head)
        self._head=newest
        self._size+=1
    def appender_last(self,item):
        if(self._head is None):
            self.appender_first(item)
        else:
            newest=self.Node(item)
            tail=self._head
            while tail._link is not None:
                tail=tail._link
            tail._link=newest
            self._size+=1
    def delete_first(self):
        if(self._size==0):
            return None
        self._head=self._head._link
        self._size-=1
    def delete_last(self):
        if(self._size==0):
            return None
        newest=self._head
        prev=None
        while(newest._link is not None):
            prev=newest
            newest=newest._link
        if prev is None:
            self._head==None
        else:
            prev._link=None
        self._size-=1
    def printer(self):
        newest=self._head
        for i in range(self._size):
            print(newest._item)
            newest=newest._link
    def searcher(self, target):
        newest=self._head
        for i in range(self._size):
            if(newest._item==target):
                return i
            newest=newest._link 
        return None
s=SingleList()
s.appender_first('orange')
s.appender_first('apple')
s.appender_last('ball')
s.appender_last('ball1')
s.appender_first('banana')
s.printer()
print('---------------------------------------')
s.delete_first()
s.delete_last()
s.printer()
print(s.searcher('ball'))
