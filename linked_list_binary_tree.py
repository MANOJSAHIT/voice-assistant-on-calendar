class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class link_binary_tree:
    def __init__(self):
        self.root=None
    def link_add_data(self,data):
        temp=self.root
        new=node(data)
        if not temp:
            self.root=new
            return
        q=[temp]
        while len(q):
            temp=q[0]
            q.pop(0)
            if temp.left!=None:
                q.append(temp.left)
            else:
                temp.left=new
                break
            if temp.right!=None:
                q.append(temp.right)
            else:
                temp.right=new
                break
    def link_last_node(self,l_node):
        temp=self.root
        q=[temp]
        while len(q):
            temp=q[0]
            q.pop(0)
            if temp ==l_node:
                temp=None
                break
            if temp.left == l_node:
                temp.left=None
                break
            else:
                q.append(temp.left)
            if temp.right == l_node:
                temp.right=None
                break
            else:
                q.append(temp.right)
    def link_delete_data(self,data):
        temp=self.root
        if not temp:
            return
        q=[temp]
        while len(q):
            temp=q[0]
            q.pop(0)
            if temp.data==data:
                req_node=temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if req_node==self.root:
            self.root.data=temp.data
            self.link_last_node(temp)
            return
        req_node.data=temp.data
        self.link_last_node(temp)
    def link_print_tree(self):
        temp=self.root
        q=[temp]
        while len(q):
            temp=q[0]
            q.pop(0)
            if temp.left!=None:
                q.append(temp.left)
            if temp.right!=None:
                q.append(temp.right)
            print(temp.data)
    def link_inorder(self,root):
        if root:
            self.link_inorder(root.left)
            print(root.data)
            self.link_inorder(root.right)
    def link_preorder(self,root):
        if root:
            print(root.data)
            self.link_preorder(root.left)
            self.link_preorder(root.right)
    def link_postorder(self,root):
        if root:
            print('ok'+str(root.data))
            self.link_postorder(root.left)
            self.link_postorder(root.right)
            print(root.data)
link_tree=link_binary_tree()
link_tree.link_add_data(1)
link_tree.link_add_data(2)
link_tree.link_add_data(3)
link_tree.link_add_data(4)
link_tree.link_add_data(5)
#link_tree.link_delete_data(3)
#link_tree.link_inorder(link_tree.root)
#link_tree.link_preorder(link_tree.root)
#link_tree.link_postorder(link_tree.root)
