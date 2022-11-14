========= Prelab 5 =============

---- No.1 ----

[1,6,5,9]


---- No.2 ----

[] 

Error

---- No.3 ---

Pada Operasi dari en1ueue dan dequeue dibutuhkan reservasi ruang memori yang lebih besar dibandingkan kebutuhan

---- No.4 ----

def._init_(self):
  self._head = None
  self._tail = None
  self._count  0
 

---- No.5 ----

def.enqueue(self, data):
  self._qList.append(data)

  
---- No.6 ----

Enqueue


---- No.7 ----

[5,6]
[6]


---- No.8 ----

def isEmpty(self):
  return self._head is None


---- No.9 -----

[6,5,9]



----- No.10 ----

queues = deque([1,2,3,4,5,6,7,8])



======================= ACT 5 ==================


------ No.1 -------

from linkedliststack import Stack

# Fungsi reverse_queue() membalik urutan elemen-elemen dalam
# queue yang diberikan sebagai argument.
def reverseQueue(q):
    # [1] Buat sebuah stack sementara untuk menyimpan elemen-elemen queue yang ditukar 
    stack = []


    # [2] Keluarkan semua elemen dari queue dan masukkan ke dalam stack.
    while len(q) > 0:
        stack.append(q.dequeue())



    # [3] Keluarkan semua elemen dari stack dan kembalikan ke dalam queue
    while len(stack) > 0:
        q.enqueue(stack.pop())
        
        
        
        
 -------.---- No.2 ----------


# Implementasi ADT Deque menggunakan list.
class Deque:
    # Constructor unutk membuat deque baru.
    # Field 1: list yang digunakan untuk menyimpan elemen-elemen deque.
    def __init__(self):
        # Tuliskan implementasi constructor di bawah.
        self.deqList = list()


    # Method isEmpty() mengembalikan True jika deque kosong dan
    # mengembalikan False jika deque tidak kosong.
    def isEmpty(self):
        # Tuliskan implementasi method isEmpty di bawah.
        return len(self) == 0
        
        
        
    # Method length() mengembalikan banyaknya elemen dalam deque.
    # Method ini diakses menggunakan fungsi len().
    def __len__(self):
        # Tuliskan implementasi method __len__ di bawah.
        return len(self.deqList)



    # Method addFront(data) menambahkan data ke bagian depan dari deque.
    # Method ini tidak mengembalikan nilai.
    def addFront(self, data):
        # Tuliskan implementasi method addFront di bawah.
        self.deqList.insert(0, data)
            
        
        
        
    # Method addRear(data) menambahkan data ke bagian belakang dari deque.
    # Method ini tidak mengembalikan nilai.
    def addRear(self, data):
        # Tuliskan implementasi method addRear di bawah.
        self.deqList.append(data)



    # Method removeFront() menghapus elemen bagian depan dari deque.
    # Method ini mengembalikan nilai data yang dihapus.
    # Jika method ini dipanggil pada deque kosong, maka method ini meng-raise
    # sebuah eksepsi.
    def removeFront(self):
        # Tuliskan implementasi method removeFront di bawah.
        if self.isEmpty():
            raise Exception("Deque kosong. Tidak dapat meremove front.")
        else:
            return self.deqList.pop(0)
        
        
        
    # Method removeRear() menghapus elemen bagian belakang dari deque.
    # Method ini mengembalikan nilai data yang dihapus.
    # Jika method ini dipanggil pada deque kosong, maka method ini meng-raise
    # sebuah eksepsi.
    def removeRear(self):
        # Tuliskan implementasi method removeRear di bawah.
        if self.isEmpty():
            raise Exception("Deque kosong. Tidak dapat meremove rear.")
        else:
            return self.deqList.pop(len(self.deqList) - 1)
