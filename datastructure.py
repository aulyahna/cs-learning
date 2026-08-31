from collections import deque

stack = []  # prinsip LIFO (Last In, First Out), "Tumpukan Piring"

stack.append("A")   # berada di paling bawah
stack.append("B")
stack.append("C")   # 1. Push (Menambah data)

stack.pop()  # 2. Pop (Mengambil yang berada di paling atas, C)

stack = ["Book", "Laptop", "Phone"]
print(stack[-1])  # 3. Peek (Melihat data paling atas tanpa menghapusnya), Python tidak punya peek()

if len(stack) == 0:        # 4. isEmpty (Mengecek apakah stack kosong)
    print("Stack kosong")

if not stack:              # lebih "Pythonic"
    print("Stack kosong")


queue = []  # prinsip FIFO (First In, First Out), "Antrean Kasir"

queue.append("A")
queue.append("B")
queue.append("C")

print(queue.pop(0))  # karena elemen paling depan berada di indeks ke-0
print(queue)


from collections import deque
from operator import index

dq = deque()  # Deque (Double Ended Queue), gabungan dari Stack dan Queue (bisa diambil dari dua sisi, depan dan belakang)

dq.append("A")
dq.append("B")
dq.appendleft("C")
print(dq)
print(dq.pop())
print(dq.popleft())


class Node:  # Linked List ≠ List. List = cepat untuk akses dengan indeks (numbers[500])
    def __init__(self, data):    # Linked List = cepat untuk menyisipkan atau menghapus node di tengah, tetapi lebih lambat untuk mencari data.
        self.data  = data        # Linked List tidak menyimpan data berdampingan. Bentuknya seperti gerbong kereta, setiap gerbong berisi "Node".
        self.next = None         # Setiap Node berisi dua hal: data dan next (alamat Node berikutnya). Jadi Node tidak perlu berdampingan di memori.
                  # None = Belum ada Node berikutnya.
node1 = Node(10)
print(node1.data)  # Node = 1 kotak

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

print(node1.data)
print(node1.next.data)
print(node1.next.next.data)


class LinkedList:  # LinkedList = "Bagaimana komputer berjalan dari satu node ke node berikutnya"
    def __init__(self):  # LinkedList = Hanya menyimpan alamat node pertama
        self.head = None  # head = Node pertama pada Linked List. Kalau Linked List kosong, head = None

    def append(self, data):  # append() = "Cari node terakhir, lalu sambungkan node baru."
        new_node = Node(data)  # 1. Buat node baru
      # new_node = referensi/alamat menuju object Node
        if self.head is None:     # 2. Kalau head masih None
            self.head = new_node        # jadikan head = node baru
            return                      # selesai
    
        current = self.head    # 3. Mulai dari head

        while current.next is not None:  # 4. Jalan sampai node terakhir
            current = current.next

        current.next = new_node      # 5. Sambungkan node terakhir ke node baru
              # next (pointer/reference) = penghubung antar node
    def display(self):   # display() = "Mulai dari head, kunjungi setiap node satu per satu sampai habis."
        current = self.head  # Traversal = "Mengunjungi satu per satu semua node" (proses berjalan)

        while current is not None:
            print(current.data, end=" -> ")      # cetak   # end mengganti karakter akhir yang biasanya berupa \n (pindah baris).
            current = current.next               # lanjut jalan
        print("None")

    def search(self, target):
        current = self.head

        while current:
            if current.data == target:
                return True
            
            current = current.next

        return False
    
    def insert_after(self, target, data):
        current = self.head

        while current:
            if current.data == target:
                new_node = Node(data)

                new_node.next = current.next
                current.next = new_node
                return
            
            current = current.next

        print("Target tidak ditemukan.")

    def delete(self, target):
        current = self.head  # current = node yang sedang diperiksa (dipakai untuk mencari node yang ingin diproses)
        previous = None      # previous = digunakan untuk mengingat node tepat sebelum current (dipakai ketika kita perlu mengubah hubungan)
                                       # (next) dari node sebelumnya, misalnya saat menghapus node.
        while current:
            if current.data == target:

                if previous is None:
                    self.head = current.next

                else:
                    previous.next = current.next

                return
            
            previous = current
            current = current.next

        print("Data tidak ditemukan.")

    def length(self):   # length() digunakan untuk menghitung berapa banyak node yang ada di Linked List.
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next

        return count
    
    def reverse(self):  # reverse() = Digunakan untuk membalik urutan node di Linked List.
        previous = None
        current = self.head

        while current:
            next_node = current.next  # Simpan alamat node berikutnya    (SAVE)
            current.next = previous   # Balik arah panah                 (REVERSE)
            previous = current        # Geser previous ke node saat ini  (MOVE previous)
            current = next_node       # Geser current ke node berikutnya (MOVE current)

        self.head = previous          # Head sekarang menunjuk ke node terakhir yang telah dibalik
    
ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print(ll.search(30))
print(ll.search(50))

ll.insert_after(20,25)

ll.delete(30)

ll.display()

print(ll.length())

ll.reverse()
ll.display()


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack kosong.")
            return
        data = self.top.data
        self.top = self.top.next
        return data
    
    def peek(self):
        if self.top is None:
            print("Stack kosong.")
            return
        return self.top.data
    
    def isEmpty(self):
        return self.top is None
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.isEmpty())

    
class Queue:
    def __init__(self):
        self.front = None  # ada Front dan Rear karena kita memasukkan data dari belakang, tapi mengeluarkannya dari depan.
        self.rear = None

    def enqueue(self, data):  # enqueue() = menambah orang ke belakang antrean
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):   # dequeue() = melayani orang paling depan (mirip pop dalam Stack())
        if self.front is None:
            print("Queue kosong.")
            return
        
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None

        return data
    
    def peek(self):
        if self.front is None:
            print("Queue kosong.")
            return
        return self.front.data
    
    def isEmpty(self):
        return self.front is None
    

class TreeNode:  # TreeNode = "Node pada pohon biner" (Binary Tree). "Pohon biner" (Binary Tree) = "Node yang memiliki maksimal 2 anak (cabang = Tree)."
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
                          # Traversal = cara mengunjungi semua node di Tree. Ada 3 cara Traversal:
    def preorder(self,node):   # 1. Preorder Traversal = Root -> Left -> Right (Kunjungi node saat ini, lalu anak kiri, lalu anak kanan)
        if node is None:
            return
        
        print(node.data)

        self.preorder(node.left)

        self.preorder(node.right)

    def inorder(self,node):    # 2. Inorder Traversal = Left -> Root -> Right (Kunjungi anak kiri, lalu node saat ini, lalu anak kanan)
        if node is None:
            return
        
        self.inorder(node.left)

        print(node.data)

        self.inorder(node.right)

    def postorder(self,node):  # 3. Postorder Traversal = Left -> Right -> Root (Kunjungi anak kiri, lalu anak kanan, lalu node saat ini)
        if node is None:
            return
        
        self.postorder(node.left)

        self.postorder(node.right)

        print(node.data)

    def search(self, node, target):  # Binary Search Tree (BST) = "Pohon biner yang memiliki aturan tertentu: anak kiri < parent < anak kanan"
        if node is None:
            return False
        
        if target == node.data:
            return True
        
        elif target < node.data:
            return self.search(node.left, target)
        
        else:
            return self.search(node.right, target)
        
    def insert(self, node, data):  # Insert = "Menambahkan node baru ke pohon biner"
        if node is None:
            return TreeNode(data)  # "Kalau sudah menemukan tempat kosong, buat node baru." (Base Case dari recursion)
        
        if data < node.data:
            node.left = self.insert(node.left, data)

        else:
            node.right = self.insert(node.right, data)
        return node
    
    def find_min(self, node):    
                while node.left: 
                    node = node.left
                return node
    
    def delete(self, node, data):  # Delete = "Menghapus node dari pohon biner"
        if node is None:
            return None
        
        if data < node.data:               
            node.left = self.delete(node.left, data)

        elif data > node.data:
            node.right = self.delete(node.right, data)

        else:
            # Kasus 1 = tidak memiliki anak kiri
            if node.left is None:
                return node.right
            
            # Kasus 2 = tidak memiliki anak kanan
            elif node.right is None:
                return node.left

            # Kasus 3 = memiliki dua anak
            temp = self.find_min(node.right)   # find_min() = "Mencari node dengan nilai terkecil di pohon biner" (Node paling kiri)
            node.data = temp.data              # Inorder Successor = "Node dengan nilai terkecil di subtree kanan" (Node paling kiri di subtree kanan) / Node yang akan dikunjungi setelah node saat ini pada Inorder Traversal.
            node.right = self.delete(node.right, temp.data)  # temp = nama variabel semnetara untuk menyimpan node yang akan dihapus (temporary variable)

        return node

root = TreeNode("A")        # Root = Node paling atas pada pohon biner. Root tidak memiliki parent (induk) dan merupakan titik awal seluruh Tree.
                            # Parent = Node induk (Node yang memeiliki anak/cabang)
root.left = TreeNode("B")   # Child = Node anak (Node yang berada di bawah parent)
root.right = TreeNode("C")  # Sibling = Node saudara (Node yang memiliki parent sama)
                            # Leaf = Node daun (Node yang tidak memiliki anak/cabang)
root = TreeNode(50)
root = root.insert(root, 25)

class MaxHeap:  # Max Heap = "Heap yang memiliki aturan tertentu: setiap parent >= anak-anaknya" (Parent lebih besar dari anak-anaknya)
    def __init__(self):
        self.heap = []

    def display(self):  # display() = "Menampilkan semua elemen di heap"
        print(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):  # peek() = "Melihat nilai maksimum (root) tanpa menghapusnya"
        if len(self.heap) == 0:
            return None
        
        return self.heap[0]  # root = elemen pertama di heap (indeks ke-0)
    
    def size(self): # size() = "Menghitung jumlah elemen di heap"
        return len(self.heap)

    def get_parent(self, index):  # get_parent() = "Mendapatkan indeks parent dari node saat ini"
        return (index - 1) // 2
    
    def get_left(self, index):  # get_left() = "Mendapatkan indeks anak kiri dari node saat ini"
        return 2 * index + 1    # rumus anak kiri = 2*i + 1 

    def get_right(self, index):  # get_right() = "Mendapatkan indeks anak kanan dari node saat ini"
        return 2 * index + 2     # rumus anak kanan = 2*i + 2

    def insert(self, data):  # Insert = "Menambahkan elemen baru ke heap"
        self.heap.append(data)  # Tambahkan elemen baru di akhir heap
        
        self._heapify_up(len(self.heap) - 1)  # Memperbaiki heap dari bawah ke atas (Heapify Up) untuk memastikan aturan Max Heap tetap terjaga.

    def _heapify_up(self, index):
        # Memperbaiki Heap dari bawah ke atas

        parent_index = (index - 1) // 2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            # Tukar node dengan parent
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[index]
            )

            # Lanjutkan pengecekan ke atas
            self._heapify_up(parent_index)

    def remove(self): 
        return self.extract_max()  # wrapper method = "method yang membungkus method lain" (method ini hanya memanggil method lain, tapi tidak menambahkan fungsionalitas baru)

    def extract_max(self):

        # Heap kosong
        if len(self.heap) == 0:
            return None

        # Jika hanya ada satu elemen
        if len(self.heap) == 1:
            return self.heap.pop()

        # Simpan nilai maksimum (root)
        max_value = self.heap[0]

        # Pindahkan elemen terakhir ke root
        self.heap[0] = self.heap.pop()

        # Perbaiki Heap
        self._heapify_down(0)

        # Kembalikan nilai maksimum
        return max_value

    def _heapify_down(self, index):
        # Memperbaiki Heap dari atas ke bawah

        largest = index

        left_child_index = self.get_left(index)
        right_child_index = self.get_right(index)

        # Cek anak kiri
        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index] > self.heap[largest]
        ):
            largest = left_child_index

        # Cek anak kanan
        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index] > self.heap[largest]
        ):
            largest = right_child_index

        # Jika parent bukan yang terbesar
        if largest != index:

            # Tukar
            self.heap[index], self.heap[largest] = (
                self.heap[largest],
                self.heap[index]
            )

            # Lanjutkan perbaikan ke bawah
            self._heapify_down(largest)


    def _heapify_up(self, index):
        # Memperbaiki Heap dari bawah ke atas

        parent_index = self.get_parent(index)

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            # Tukar node dengan parent
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[index]
            )

            # Lanjutkan pengecekan ke atas
            self._heapify_up(parent_index)

    def remove(self): 
        return self.extract_max()  # wrapper method = "method yang membungkus method lain" (method ini hanya memanggil method lain, tapi tidak menambahkan fungsionalitas baru)

    def extract_max(self):

        # Heap kosong
        if len(self.heap) == 0:
            return None

        # Jika hanya ada satu elemen
        if len(self.heap) == 1:
            return self.heap.pop()

        # Simpan nilai maksimum (root)
        max_value = self.heap[0]

        # Pindahkan elemen terakhir ke root
        self.heap[0] = self.heap.pop()

        # Perbaiki Heap
        self._heapify_down(0)

        # Kembalikan nilai maksimum
        return max_value
    
heap = MaxHeap()

if heap.is_empty():
        print("Heap Kosong")
    

heap = MaxHeap()
heap.heap = [100, 70, 80, 20, 30, 50, 60]

heap.display()

print(heap.get_parent(5))
print(heap.heap[heap.get_parent(5)])  # nilai parent dari node dengan indeks 5

parent = heap.get_parent(5)
print(heap.heap[parent])

print(heap.get_left(1))  
print(heap.heap[heap.get_left(1)])  # nilai anak kiri dari node dengan indeks 1

heap.insert(90)
heap.insert(110)
print(heap.peek())

print(heap.size())




class HashTable:  # Memakai List karena sebenarnya Hash Table menyimpan data di Array/List. Hash Table hanya menentukan disimpan di indeks berapa
    def __init__(self):
        self.size = 10  # memiliki 10 slot (dari index 0) untuk menyimpan data. Ukuran ini bisa diubah sesuai kebutuhan.
        self.table = [[] for _ in range(self.size)]  # "Buat list sepanjang 10, diisi dengan list kosong" (setiap slot berisi list untuk menampung pasangan key-value)

    def hash_function(self, key):
        return hash(key) % self.size  # hash() = "Fungsi hash bawaan Python" (mengubah key menjadi angka unik). % = modulus (sisa bagi). 

    def insert(self, key, value):
        index = self.hash_function(key)

        self.table[index].append((key, value))  # Simpan tuple (key, value) di indeks yang ditentukan oleh fungsi hash

    def get(self, key):
        index = self.hash_function(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        return None  # Jika key tidak ditemukan

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket): # enumerate() = "Mendapatkan indeks dan nilai dari list" (misal: [(0, (key1, value1)), (1, (key2, value2))])
            if k == key:
                del bucket[i]  # Hapus pasangan key-value dari bucket
                return True

        return False  # Jika key tidak ditemukan

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")
            else:
                print(f"Index {i}: []")
         

ht = HashTable()
ht.insert("name", "Anna")  # Menyimpan data dengan key "Anna"
ht.insert("age", 17)
ht.insert("class", 12)

ht.get("name")  # Mengambil data berdasarkan key "name" (mengembalikan value "Anna")

print(ht.get("name"))  # Mengambil data berdasarkan key "name" (mengembalikan value "Anna")

ht.display()  # Menampilkan seluruh isi Hash Table

ht.delete("class") # Menghapus data berdasarkan key "class"

ht.display()  # Menampilkan seluruh isi Hash Table setelah penghapusan



class Graph:  # Graph = "Kumpulan node (vertex) yang saling terhubung (edge)" (Node = Vertex, Edge = Sisi)

    def __init__(self):  # graph = "Dictionary yang menyimpan node dan tetangganya" (key = node, value = list tetangga)
        self.graph = {}  # self.graph = "siapkan sebuah dictionary kosong untuk menyimpan Graph"

    def add_vertex(self, vertex):  # add_vertex() = "Menambahkan node ke Graph"
        if vertex not in self.graph:
            self.graph[vertex] = []  # "Buat list kosong untuk menyimpan tetangga node ini"

    def add_edge(self, vertex1, vertex2):  # add_edge() = "Membuat hubungan (edge) antara dua node"
        if vertex1 in self.graph and vertex2 in self.graph:

            self.graph[vertex1].append(vertex2)  # Menambahkan vertex2 ke list tetangga vertex1
            self.graph[vertex2].append(vertex1)  # Karena ini Graph tidak berarah (undirected), tambahkan juga hubungan dari vertex2 ke vertex1

    def display(self): 
            for vertex in self.graph:
                print(vertex, "->", self.graph[vertex])  # Menampilkan node dan tetangganya

    def dfs(self, vertex, visited=None):  # Depth-First Search (DFS) = "Algoritma untuk menjelajahi Graph dengan cara menelusuri sedalam mungkin sebelum mundur" (mengunjungi node tetangga terlebih dahulu sebelum kembali ke node sebelumnya)
        if visited is None:               # Recursion DFS = Menggunakan call stack Python secara otomatis untuk menyimpan node yang sedang dikunjungi. 
            visited = set()  # visited = "Set untuk menyimpan node yang sudah dikunjungi" (agar tidak mengunjungi node yang sama berulang kali)

        visited.add(vertex)  # tandai node ini sudah dikunjungi
        print(vertex)        # cetak node yang sedang dikunjungi

        for neighbor in self.graph[vertex]: # lihat tetangga dari node ini
            if neighbor not in visited:
                self.dfs(neighbor, visited) # masuk lebih dalam ke tetangga yang belum dikunjungi (rekursi)

    def dfs_stack(self, start): # Iterative DFS = Kita membuat Stack sendiri untuk menyimpan node yang akan dikunjungi, bukan mengandalkan call stack Python. (lebih efisien untuk Graph besar)

        visited = set()
        stack = [start]  # stack = "Tumpukan untuk menyimpan node yang akan dikunjungi"

        while stack:

            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)  # tambahkan tetangga ke stack untuk dikunjungi nanti

    def bfs(self, start): # Breadth-First Search (BFS) = "Algoritma untuk menjelajahi Graph dengan cara mengunjungi semua tetangga sebelum masuk lebih dalam" 

        visited = set()
        queue = deque([start])  # queue = "Antrean untuk menyimpan node yang akan dikunjungi"

        while queue:
            vertex = queue.popleft()  # ambil node dari depan antrean

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)  # tambahkan tetangga ke antrean untuk dikunjungi nanti

    def remove_edge(self, vertex1, vertex2): # remove_edge() = "Menghapus hubungan (edge) antara dua node"

        if vertex1 in self.graph and vertex2 in self.graph:

            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)

            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def remove_vertex(self, vertex): # remove_vertex() = "Menghapus node dan semua hubungannya (edge) dari Graph"

        if vertex not in self.graph:
            return

        for neighbor in self.graph[vertex]:
            self.graph[neighbor].remove(vertex)

        del self.graph[vertex]  # Hapus node dari Graph


g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.bfs("A")  # Menelusuri Graph mulai dari node "A"

g.display()  # Menampilkan seluruh isi Graph

