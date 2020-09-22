class tree_node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class link_binary_search_tree:
    def __init__(self):
        self.root=None
    def search_tree_add_data(self,data):
        temp=self.root
        if not temp:
            self.root=tree_node(data)
            return
        q=[temp]
        new=tree_node(data)
        while len(q):
            temp=q.pop(0)
            if temp.left:
                q.append(temp.left)
            else:
                if data<temp.data:
                    temp.left=new
                    break
            if temp.right:
                q.append(temp.right)
            else:
                if data>=temp.data:
                    temp.right=new
                    break
    def serch_inorder_tree(self,root):
        if root:
            self.serch_inorder_tree(root.left)
            print(root.data)
            self.serch_inorder_tree(root.right)
    def serch_postrder_tree(self,root):
        if root:
            self.serch_postrder_tree(root.left)
            self.serch_postrder_tree(root.right)
            print(root.data)
    def serch_preorder_tree(self,root):
        if root:
            print(root.data)
            self.serch_preorder_tree(root.left)
            self.serch_preorder_tree(root.right)
    def search_delete_data(self,data):
        temp=self.root
        if not temp:
            return
        q=[temp]
        while len(q):
            temp=q.pop(0)
            pass
    def print_search_tree(self):
        temp=self.root
        if not temp:
            return
        q=[temp]
        while len(q):
            temp=q.pop(0)
            print(temp.data)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
binary_serch_tree=link_binary_search_tree()
binary_serch_tree.search_tree_add_data(50)
binary_serch_tree.search_tree_add_data(30)
binary_serch_tree.search_tree_add_data(20)
binary_serch_tree.search_tree_add_data(40)
binary_serch_tree.search_tree_add_data(70)
binary_serch_tree.search_tree_add_data(60)
binary_serch_tree.search_tree_add_data(80)
#binary_serch_tree.print_search_tree()
binary_serch_tree.serch_inorder_tree(binary_serch_tree.root)
