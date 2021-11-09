class BinaryTree:
    class Node:
        def __init__(self, item=None, link_r=None, link_l=None):
            self._link_l=link_l
            self._item=item
            self._link_r=link_r
    def __init__(self):
        self._head=None
        self._count=0
    def appender(self,item):
        new=self._head
        if(new==None):
            self._head=self.Node(item)
        else:
            self.insert_value(new,item)
        self._count+=1
    def insert_value(self, node, item):
        if(node._item>item):
            if(node._link_l!=None):
                self.insert_value(node._link_l,item)
            else:
                node._link_l=self.Node(item)
        else:
            if(node._link_r!=None):
                self.insert_value(node._link_r,item)
            else:
                node._link_r=self.Node(item)
    def printer_post(self,node=None):
        if(node==None):
            node=self._head
        if(node._link_l):
            self.printer_post(node._link_l)
        print(node._item,end=' ')
        if(node._link_r):
            self.printer_post(node._link_r)

s=BinaryTree()
s.appender(10)
s.appender(1)
s.appender(12)
s.appender(2)
s.printer_post()
#이런식으로 할 경우 BinaryTree가 아닌 그냥 Tree가 되어버리는 문제가 발생한다.