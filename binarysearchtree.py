import math

"""
for my tree_node, I have the following attribute;
    cargo: the value of the node
    left : the left sub_tree
    right : the right sub_tree
    repeat_times : return the number of the same values stored in the tree.
                   for the coursework allow duplicates.
    height : return the height of the node in a tree
    parent: pointing to its parent.

"""



class TreeNode:
    def __init__(self, cargo, left, right):
        self.__cargo = cargo
        self.__left = left
        self.__right = right
        self.__repeat_times = 1
        self.__parent = None
        self.__height = 1

    def set_left(self, new_left):
        self.__left = new_left

    @property
    def left(self):
        return self.__left

    def set_right(self, new_right):
        self.__right = new_right

    @property
    def right(self):
        return self.__right

    def set_cargo(self, new_cargo):
        self.__cargo = new_cargo

    @property
    def cargo(self):
        return self.__cargo

    @property
    def repeat_times(self):
        return self.__repeat_times

    def set_repeat_times(self, new_times):
        self.__repeat_times = new_times

    @property
    def parent(self):
        return self.__parent

    def set_parent(self,new_parent):
        self.__parent = new_parent

    @property
    def height(self):
        return self.__height;

    def set_height(self,new_height):
        self.__height = new_height

"""
    for the design of binary search tree class, I referred to myself and Brian Faure's code, 
    and I also made a lot of changes to it.
    <author>
        Brian Faure,
        YU GAN 
    </author>
    <url>
        https://github.com/bfaure/Python3_Data_Structures/blob/master/AVL_Tree/main.py
        https://github.com/YGVICTOR/CS61B_YG/blob/master/lab9/lab9/BSTMap.java
    </url>
    """


class BinarySearchTree:
    def __init__(self, root=None, size_limit="infinite"):
        self.__root = root
        self.__capacity = size_limit
        if self.__root is None:
            self.__current_qty = 0
        else:
            self.__current_qty = 1

    def is_empty(self):
        return self.__root is None

    def is_full(self):
        if self.__capacity == "infinite":
            return False
        else:
            return self.__current_qty >= self.__capacity

    def set_root(self, new_root):
        self.__root = new_root

    @property
    def root(self):
        return self.__root

    def set_capacity(self, new_capacity):
        self.__capacity = new_capacity

    @property
    def capacity(self):
        return self.__capacity

    def set_current_qty(self, new_current_qty):
        self.__current_qty = new_current_qty

    @property
    def current_qty(self):
        return self.__current_qty

    """
    for __repr__(self) function, I referred to Brian Faure's code, and I also made some changes to it .
    <author>
        Brian Faure 
    </author>
    <url>
        https://github.com/bfaure/Python3_Data_Structures/blob/master/AVL_Tree/main.py
    </url>
    """

    # __repr__() return a string representation of tree.
    def __repr__(self):
        if self.__root == None: return ''
        content = '\n'  # to hold final string
        cur_nodes = [self.__root]  # all nodes at current level
        cur_height = self.__root.height  # height of nodes at current level
        sep = ' ' * math.ceil((1.5 ** (cur_height - 1)))  # variable sized separator between elements
        while True:
            cur_height += -1  # decrement current height
            if len(cur_nodes) == 0: break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:
                if n == None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.cargo != None:
                    buf = ' ' * int((5 - len(str(n.cargo))) / 2)
                    cur_row += '%s%s%s' % (buf,"("+str(n.cargo)+","+str(n.repeat_times)+")", buf) + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left != None:
                    next_nodes.append(n.left)
                    next_row += '   /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right != None:
                    next_nodes.append(n.right)
                    next_row += '    \ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)  # cut separator size in half
        return content

    # get the height of a tree(sub_tree)
    def height(self):
        if self.__root is not None:
            return self._height(self.__root, 0)
        else:
            return 0

    # helper function to assist height() above
    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left,cur_height+1)
        right_height = self._height(cur_node.right,cur_height+1)
        return max(left_height,right_height)

    def __search_helper(self, target, root):
        if (root == None):
            return False
        if target > root.cargo:
            return self.__search_helper(target, root.right)
        elif target < root.cargo:
            return self.__search_helper(target, root.left)
        elif target == root.cargo:
            return True

    def search(self, target):
        return self.__search_helper(target, self.root)

    # search() returns true when find the target; find() returns that node itself when find
    # the target
    def find(self,value):
        if self.__root is not None:
            return self._find(value,self.__root)
        else:
            return None

    def __insert_helper(self, target, root):
        if self.capacity == "infinite" or self.capacity > self.current_qty:
            if self.search(target):
                ptr = root
                while ptr.cargo != target:
                    if ptr.cargo > target:
                        ptr = ptr.left
                    else:
                        ptr = ptr.right
                ptr.set_repeat_times(ptr.repeat_times + 1)
                self.set_current_qty(self.current_qty + 1)
            else:
                ptr = root
                ptr_child = root
                while ptr_child is not None:
                    ptr = ptr_child
                    if ptr_child.cargo > target:
                        ptr_child = ptr_child.left
                    else:
                        ptr_child = ptr_child.right
                new_node = TreeNode(target, None, None)
                if ptr.cargo > target:
                    ptr.set_left(new_node)
                    ptr.left.set_parent(ptr)
                    self._inspect_insertion(ptr.left)
                else:
                    ptr.set_right(new_node)
                    ptr.right.set_parent(ptr)
                    self._inspect_insertion(ptr.right)
                self.set_current_qty(self.current_qty + 1)
        else:
            raise Exception("don't have enough space for insertion")

    def insert(self, target):
        if self.__root is None:
            new_node = TreeNode(target, None, None)
            self.__root = new_node
            self.__current_qty += 1
        else:
            self.__insert_helper(target, self.__root)

    def _find(self,value,cur_node):
        if value == cur_node.cargo:
            return cur_node
        elif value < cur_node.cargo and cur_node.left is not None:
            return self._find(value,cur_node.left)
        elif value > cur_node.cargo and cur_node.right is not None:
            return self._find(value,cur_node.right)

    """
        for delete(self,value) function, I referred to Brian Faure's code, and I also made some changes to it .
        <author>
            Brian Faure 
        </author>
        <url>
            https://github.com/bfaure/Python3_Data_Structures/blob/master/AVL_Tree/main.py
        </url>
        """
    def delete(self, value):
        node = self.find(value)
        if node is None:
            raise Exception("the data: {} you want to delete is not inserted".format(value))
        return self._delete_helper(node)

    def _delete_helper(self, node):
        # to delete a node with 2 children, sometimes we need to find
        # the min of the right sub tree.
        def min_value_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        # to delete a node with 2 children, sometimes we need to find
        # the maximum of the left sub tree.
        def max_value_node(n):
            current = n
            while current.right is not None:
                current = current.right
            return current

        # calculate the number of children node n has
        def num_children(n):
            num_children = 0
            if n.left is not None:
                num_children += 1
            if n.right is not None:
                num_children += 1
            return num_children

        node_parent = node.parent
        node_children = num_children(node)

        # CASE 1 Node has no children
        if node_children == 0:
            # delete the root with no child
            if node_parent is None:
                self.__root = None
                return
            else:
                if node_parent.left == node:
                    if node_parent.left.repeat_times >1:
                        node_parent.left.set_repeat_times(node_parent.left.repeat_times -1)
                        self.set_current_qty(self.current_qty-1)
                    else:
                        node_parent.set_left(None)
                        self.set_current_qty(self.current_qty - 1)
                else:
                    if node_parent.right.repeat_times >1:
                        node_parent.right.set_repeat_times(node_parent.right.repeat_times-1)
                        self.set_current_qty(self.current_qty-1)
                    else:
                        node_parent.set_right(None)
                        self.set_current_qty(self.current_qty - 1)

        # CASE 2 (Node has a single child)
        if node_children == 1:
            if node.left is not None:
                child = node.left
            else:
                child = node.right
            if node.repeat_times > 1:
                node.set_repeat_times(node.repeat_times - 1)
                self.set_current_qty(self.current_qty - 1)
                return
            if node.parent is None:
                if node.right is not None:
                    successor = min_value_node(node.right)
                    node.set_cargo(successor.cargo)
                    self._delete_helper(successor)
                else:
                    predecessor = max_value_node(node.left)
                    node.set_cargo(predecessor.cargo)
                    self._delete_helper(predecessor)
            else:
                if node.parent.left == node:
                    node_parent.set_left(child)
                else:
                    node_parent.set_right(child)
                child.set_parent(node_parent)

        # Case 3 (Node has two children)
        if node_children == 2:
            if node.repeat_times > 1:
                node.set_repeat_times(node.repeat_times - 1)
                self.set_current_qty(self.current_qty - 1)
                return
            successor = min_value_node(node.right)
            node.set_cargo(successor.cargo)
            self._delete_helper(successor)
            return

        if node_parent is not None:
            node_parent.set_height(1 + max(self.get_height(node_parent.left),
                                          self.get_height(node_parent.right)))
            self._inspect_deletion(node_parent)

    def _inspect_insertion(self,cur_node,path=[]):
        # reach the root, end the recursion.
        if cur_node.parent is None:
            return
        # add the node locating from the insertion point all the way to root
        path = [cur_node] + path
        # get the height of subtree of the current node
        left_height = self.get_height(cur_node.parent.left)
        right_height = self.get_height(cur_node.parent.right)

        # check if the left and right sub tree are balanced
        if abs(left_height - right_height) > 1:
            # add the parent of the current node into the path
            # the parent of the current node is the first node to be unbalanced.
            path =[cur_node.parent] + path
            self._rebalance(path[0],path[1],path[2])
            return
        # after the rebalance, recalculate the height of the parent
        new_height = 1 + cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.set_height(new_height)


        # when the parnet_node is balanced, we have to check the
        # parent of the parent, all the way to the root.
        self._inspect_insertion(cur_node.parent,path)

    def _inspect_deletion(self,cur_node):
        # similarly, deletion should also traverse the node from
        # the deletion point to the root to balance all unbalanced point
        if cur_node is None:
            return
        left_height = self.get_height(cur_node.left)
        right_height = self.get_height(cur_node.right)
        if abs(left_height - right_height)>1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self._rebalance(cur_node,y,x)
        self._inspect_deletion(cur_node.parent)

    def _rebalance(self,z,y,x):
        # LL Case
        if y==z.left and x == y.left:
            self._right_rotate(z)

        # LR Case
        elif y == z.left and x == y.right:
            self._left_rotate(y)
            self._right_rotate(z)

        #RR Case
        elif y==z.right and x == y.right:
            self._left_rotate(z)

        # RL Case
        elif y==z.right and x == y.left:
            self._right_rotate(y)
            self._left_rotate(z)

        else:
            # This situation will never happen
            raise Exception("Good bye")

    def _right_rotate(self,z):
        sudo_root = z.parent
        y=z.left
        t3 = y.right
        y.set_right(z)
        z.set_parent(y)
        z.set_left(t3)
        if t3 is not None:
            t3.set_parent(z)
        y.set_parent(sudo_root)
        if y.parent is None:
            self.__root = y
        else:
            if y.parent.left == z:
                y.parent.set_left(y)
            else:
                y.parent.set_right(y)
        z.set_height(1 + max(self.get_height(z.left),
                           self.get_height(z.right)))
        y.set_height(1 + max(self.get_height(y.left),
                           self.get_height(y.right)))

    def _left_rotate(self,z):
        sudo_root = z.parent
        y = z.right
        t2 = y.left
        y.set_left(z)
        z.set_parent(y)
        z.set_right(t2)
        if t2 is not None:
            t2.set_parent(z)
        y.set_parent(sudo_root)
        if y.parent is None:
            self.__root = y
        else:
            if y.parent.left == z:
                y.parent.set_left(y)
            else:
                y.parent.set_right(y)
        z.set_height(1+ max(self.get_height(z.left),
                          self.get_height(z.right)))
        y.set_height(1+ max(self.get_height(y.left),
                          self.get_height(y.right)))

    def get_height(self,cur_node):
        if cur_node is None:
            return 0
        return cur_node.height

    # return the taller_sub tree
    def taller_child(self,cur_node):
        left = self.get_height(cur_node.left)
        right = self.get_height(cur_node.right)
        return cur_node.left if left >= right else cur_node.right


    def traverse(self):
        result = []
        self.__traverseHelper(self.__root, result)
        return result

    def __traverseHelper(self, root, result):
        if root is None:
            return result
        self.__traverseHelper(root.left, result)

        if root.repeat_times == 1:
            result.append(root.cargo)
        else:
            for i in range(root.repeat_times):
                result.append(root.cargo)

        self.__traverseHelper(root.right, result)

    """
        for my tree representation, I choose to use (a,b) notation;
        a = the value that stored in the binary search tree;
        b = the times that a was inserted(in order to allow duplicates)
                        (value_father,repeat_times)
                        /                        \ '
        (value_left_child, repeat_times)      (value_right_child, repeat_times) 
    """

    def print_tree(self):
        print(self.__repr__())
        return