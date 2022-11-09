Nomor1.py

# Implementasi ADT LinkedList
class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def addFirst(self, data):
        newNode = _Node(data)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    # Method addLast(data) menambahkan data ke akhir linked list.
    # Method ini tidak mengembalikan nilai.
    def addLast(self, data):
        # Tuliskan implementasi method addLast(data) Anda di bawah.
        newNode = _Node(data)
        if(self._head == None):
            self._head = newNode
        else:
            smt = self._head
            while(smt.next != None):
                smt = smt.next
            smt.next = newNode
        self._size +=1
        
    def __contains__(self, data):
        curNode = self._head
        found = False
        while curNode is not None and curNode.data != data:
            curNode = curNode.next
        if curNode is not None:
            found = True
        else:
            found = False
        return found

    def remove(self, data):
        curNode = self._head
        prevNode = None
        while curNode is not None and curNode.data != data:
            prevNode = curNode
            curNode = curNode.next
        if curNode is None:
            raise ValueError('Data tidak ditemukan.')
        else:
            self._size -= 1
            if curNode is self._head:
                self._head = curNode.next
            else:
                prevNode.next = curNode.next
        
        return curNode.data

    def __iter__(self):
        return _LinkedListIterator(self._head)

class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class _LinkedListIterator:
    def __init__(self, listHead):
        self._curNode = listHead
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self._curNode is None:
            raise StopIteration
        else:
            data = self._curNode.data
            self._curNode = self._curNode.next
            return data
          
 ================

Nomor2.py


# Implementasi ADT SortedLinkedList
class SortedLinkedList:
    # Constructor SortedLinkedList (dimulai dengan linked list kosong)
    def __init__(self):
        self._head = None
        self._size = 0

    # Method length() mengembalikan banyaknya elemen dalam sorted linked list.
    # Method ini diakses menggunakan fungsi len().
    def __len__(self):
        # Implementasikan method __len__ di bawah.
        return self._size

    # Method add(data) menambahkan data baru ke sorted linked list.
    def add(self, data):
        # Implementasikan method add(data) di bawah.
       gcpn = self._head
       if gcpn is None:
           x = _Node(data)
           x.data = data
           self._head = x
           self._size += 1
           return
       if gcpn.data > data:
           x = _Node(data)
           x.data = data
           x.next = gcpn
           self._head = x
           self._size += 1
           return
       while gcpn.next is not None:
           if gcpn.next.data > data:
               break
           gcpn = gcpn.next
       x = _Node(data)
       x.data = data
       x.next = gcpn.next
       gcpn.next = x
       self._size += 1
       return

    # Method contains(data) digunakan untuk mencari data dalam sorted linked list.
    # Method ini diakses menggunakan operator in dan 
    # mengembalikan nilai Boolean: True jika data ditemukan dan False jika
    # data tidak ditemukan. 
    def __contains__(self, data):
        # Implementasikan method __contains__ di bawah.
        curNode = self._head
        found = False
        while curNode is not None and curNode.data != data:
            curNode = curNode.next
        if curNode is not None:
            found = True
        else:
            found = False
        return found
        
    # Method remove() menghapus data dari sorted linked list.
    # Method ini mengembalikan data yang dihapus.
    def remove(self, data):
        # Implementasikan method remove di bawah.
        curNode = self._head
        prevNode = None
        while curNode is not None and curNode.data != data:
            prevNode = curNode
            curNode = curNode.next
        if curNode is None:
            raise ValueError('Data tidak ditemukan.')
        else:
            self._size -= 1
            if curNode is self._head:
                self._head = curNode.next
            else:
                prevNode.next = curNode.next
        
        return curNode.data
        
    # Method iterator untuk men-traverse sorted linked list
    # Method ini mengembalikan object dari class `_LinkedListIterator` 
    # dengan argumen referensi head.
    def __iter__(self):
        # Implementasikan method __iter__ di bawah
        return _LinkedListIterator(self._head)


# Definisikan class _Node sebagai penyimpanan data dan referensi 
# ke node selanjutnya.
class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class iterator untuk ADT Sorted Linked List
class _LinkedListIterator:
    # Implementasikan class _LinkedListIterator di bawah.
    def __init__(self, listHead):
        self._curNode = listHead
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self._curNode is None:
            raise StopIteration
        else:
            data = self._curNode.data
            self._curNode = self._curNode.next
            return data
