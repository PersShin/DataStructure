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
        print(node._item, item)
        if(node._item>item):
            if(node._link_l!=None):
                print(item)
                self.insert_value(node._link_l,item)
            else:
                node._link_l=self.Node(item)
        else:
            if(node._link_r!=None):
                self.insert_value(node._link_r,item)
            else:
                node._link_r=self.Node(item)
    def printer_postfix(self,node=None):
        if(node==None):
            node=self._head
        if(node._link_l):
            self.printer_postfix(node._link_l)
        if(node._link_r):
            self.printer_postfix(node._link_r)
        print(node._item,end=' ')
    def printer_prefix(self, node=None):
        if(node==None):
            node=self._head
        print(node._item,end=' ')
        if(node._link_l):
            self.printer_prefix(node._link_l)
        if(node._link_r):
            self.printer_prefix(node._link_r)
    def printer_inorder(self, node=None):
        if(node==None):
            node=self._head
        if(node._link_l):
            self.printer_inorder(node._link_l)
        print(node._item,end=' ')
        if(node._link_r):
            self.printer_inorder(node._link_r)
    def printer_level(self,node=None):
        if(node==None):
            node=self._head
        queue=[node]
        while queue:
            node=queue.pop(0)
            if node is not None:
                print(node._item, end=' ')
            if(node._link_l):
                queue.append(node._link_l)
            if(node._link_r):
                queue.append(node._link_r)

s=BinaryTree()
s.appender(10)
s.appender(5)
s.appender(12)
s.appender(1)
s.appender(6)
s.printer_postfix()
print(' ')
s.printer_prefix()
print(' ')
s.printer_inorder()
print('')
s.printer_level()