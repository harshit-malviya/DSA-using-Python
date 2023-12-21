# defining singly LL
class Node :
    def __init__(self , data = None , next = None):
        self.data = data
        self.next = next
class SLL :
    def __init__(self , start = None) :
        self.start = start
    def is_empty (self) :
        if self.start is None :
            print("List is Empty")
            return True
    def insert_at_start(self , data) :
        n = Node(data, self.start)
        self.start = n
    def insert_at_end(self , data) :
        n = Node(data)
        temp = self.start
        if self.start == None :
            self.start = n
        else :
            while temp.next is not None :
                temp = temp.next
            temp.next = n
    def search(self , data):
        temp = self.start
        while temp is not None:
            if temp.data==data:
                print("Location Found For",data)
                return temp
            temp=temp.next
        print("Location Not Found For",data)
        return None
    
    def insert_at_location(self,temp, data) :
        temp = self.search(temp)
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

    def print_list(self) :
        temp = self.start
        while temp is not None :
            print(temp.data ,end=" ")
            temp = temp.next
ml = SLL()
ml.insert_at_start(10)
ml.insert_at_start(1)
ml.insert_at_end(30)
ml.insert_at_end(31)
ml.insert_at_location(1 , 45)
ml.print_list()