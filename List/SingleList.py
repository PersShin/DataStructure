class SingleList:
    class Node:
        def __init__(self,item=None, link=None):
            self._item=item
            self._link=link
    def __init__(self):
        self._head=None
        self._size=0
    def isNone(self):
        if(self._head is None):
            return True
        return False
    def appender_first(self,item):
        newest=self.Node(item, self._head)
        self._head=newest
        self._size+=1
    def appender_last(self, item):
        if(self.isNone()):
            self.appender_first(self,item)
        else:
            newest=self.Node(item)
            tail=self._head
            while(tail._link is not None):
                tail=tail._link
            tail._link=newest
            self._size+=1
    def printer(self):
        newest=self._head
        while(newest._link is not None):
            print(newest._item, end=' ')
            newest=newest._link
        print(newest._item)
    def delete_first(self):
        if(self.isNone()):
            return None
        else:
            self._head=self._head._link
            self._size-=1
    def delete_last(self):
        if(self.isNone()):
            return None
        else:
            tail=self._head
            prev=0
            while(tail._link is not None):
                prev=tail
                tail=tail._link
            prev._link=None
            self._size-=1
    def delete_item(self,item):
        if(self.isNone()):
            return None
        else:
            finder=self._head
            prev=None
            while(finder._item is not item):
                prev=finder
                finder=finder._link
                if(finder._link==None):
                    return None
            prev._link=finder._link
            self._size-=1
    def searcher(self, item):
        if(self.isNone()):
            return None
        else:
            finder=self._head
            for i in range(self._size):
                if(finder._item==item):
                    return i
                finder=finder._link
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
s.delete_item('orang')
s.printer()
print(s.searcher('ball'))
