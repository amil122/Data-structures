
# *********************************************************************************TREE***********************************************************************************************
class BTS:
    def __init__(self,key) :
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insertion(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data :
            return
        if data < self.key :
            if self.lchild:
                self.lchild.insertion(data)
            else :
                self.lchild = BTS(data)
        else :
            if self.rchild:
                self.rchild.insertion(data)
            else :
                self.rchild = BTS(data)
    
    def search(self, data):
        if self.key is None:
            print('the tree is empty')
            return None
        if self.key == data:
            print('the given element is there in the tree')
            return self.key
        if data <= self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('the given node is not present in the BTS')
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('the given node is not present in the BTS')
        return self.key
                
    
    def inorder(self):
        result = []
        if self.key is None:
            print('the tree is empty')
            return result  # Return an empty list if the tree is empty
        if self.lchild:
            result.extend(self.lchild.inorder())  # Extend the result list with the inorder traversal of the left subtree
        print(self.key, end=' ')
        result.append(self.key)  # Append the current node's key to the result list
        if self.rchild:
            result.extend(self.rchild.inorder())  # Extend the result list with the inorder traversal of the right subtree
        return result

    def is_bst(self):
        inorder_result = self.inorder()
        print(inorder_result)
        for i in range(len(inorder_result)-1):
            if inorder_result[i] <= inorder_result[i + 1]:
                return True
            return False
        
    def pre_order(self):
        if self.key == None:
            print('there is no element in the tree')
            return
        print(self.key, end = ' ')
        if self.lchild :
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()
            
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end = ' ')
    
    def delete(self,data):
        if self.key is None:
            print('the tree is empty')
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print('the given node is not in there')
        elif data > self.key :
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else :
                print('the given node is not present in the tree')
        else :
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.lchild
            while node.rchild :
                node = node.rchild
            self.key = node.key
            self.rchild = self.rchild.delete(data)
        return self
    
    def ancestor(self,data):
        if self.key is None:
            print('it is not possible')
        list1=[]
        current = self
        while current is not None:
            list1.append(current.key)
            if data < current.key :
                current = current.lchild
            elif data > current.key:
                current = current.rchild
            else:
                break
        if current is None:
            print('it is not there in the tree')
        return list1
    
    def min_node(self):
        if self.key is None:
            print('the tree is empty')
            return
        current = self
        while current.lchild:
            current = current.lchild
        return current.key
    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild  
        return current.key

    def closest(self, val):
        clo = float('inf')
        current = self
        while current:
            print("Current node key:", current.key)
            if abs(current.key - val) < abs(clo - val):
                clo = current.key
            if current.key > val:
                print("Moving left")
                current = current.lchild
            elif current.key < val:
                print("Moving right")
                current = current.rchild
            else:
                print("Target value found")
                break
        print("The closest value is:", clo)
        
    def sum_of_left_leaves(node, is_left=False):
        if node is None:
            return 0
        if node.lchild is None and node.rchild is None and is_left:
            return node.key
        return (sum_of_left_leaves(node.lchild, True) + sum_of_left_leaves(node.rchild, False))

            
def count(node):
    if node is None:
        return 0
    return 1 +  count(node.lchild) + count(node.rchild)

root = BTS(None)
# Create a binary search tree
list1= [45,12]
for i in list1:
    root.insertion(i)
print(count(root))
root.delete(45)
root.inorder()
