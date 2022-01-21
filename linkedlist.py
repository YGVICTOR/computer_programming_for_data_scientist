class ListNoe:
    def __init__(self,cargo,next):
        self.__cargo = cargo
        self.__next = next

    @ property
    def cargo(self):
        return self.__cargo

    def set_cargo(self,new_cargo):
        self.__cargo = new_cargo


    @property
    def next(self):
        return self.__next

    def set_next(self,new_next):
        self.__next = new_next


class LinkedList:
    def __init__(self,head=None,size = "infinite"):
        self.__head = head
        self.__size = size
        self.__current_qty = 0

    @property
    def current_qty(self):
        return self.__current_qty

    def is_empty(self):
        return self.__current_qty == 0

    def is_full(self):
        if self.__size == "infinite":
            return False
        else:
            if self.__current_qty <= self.__size:
                return True
            else:
                return False

    def __str__(self):
        ptr = self.__head
        while ptr is not None:
            if ptr.next is not None:
                print(str(ptr.cargo)+" -> ",end='')
            else:
                print(str(ptr.cargo))
            ptr = ptr.next

    def search(self,target):
        ptr = self.__head
        while ptr is not None:
            if ptr.cargo == target:
                return True
            ptr = ptr.next
        return False

    def insert(self,target):
        if self.is_full():
            raise Exception("do not have enough space to insert {}".format(target))

        if self.is_empty():
            self.__head = ListNoe(target,None)
            self.__current_qty += 1
        else:
            ptr = self.__head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.set_next(ListNoe(target,None))
            self.__current_qty += 1

    def delete(self,target):
        if self.is_empty():
            raise Exception("current list is empty")
        flag = 0
        ptr = self.__head
        if ptr.cargo == target:
            self.__head = ptr.next
            flag = 1
        else:
            while ptr.next is not None:
                if ptr.next.cargo == target:
                    ptr.set_next(ptr.next.next)
                    flag = 1
                    break
                ptr = ptr.next
        if flag == 0:
            raise Exception("{} doesn't in the list".format(str(target)))
        else:
            self.__current_qty -= 1

    def traverse(self):
        result = []
        ptr = self.__head
        while ptr is not None:
            result.append(ptr.cargo)
            ptr = ptr.next
        return result