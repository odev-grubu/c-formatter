# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 23:14:54 2020

@author: Aslih
"""

class ArrayQueue:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 20          # moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).
    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      return False
    answer = self._data[self._front]
    self._data[self._front] = None         # help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self._data))     # double the array size
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1

    
def tab_(filename): 
       
    S = ArrayQueue() 
    kaynak = open(filename) 
    bosluk = '  '
    bosluk_sayisi = 0
      
    for satir in kaynak: 
        
       if '{' in satir:
         satir = bosluk*bosluk_sayisi+satir
         bosluk_sayisi += 1
         S.enqueue(satir.rstrip("\n"))

       elif '}' in satir:
         bosluk_sayisi -= 1
         satir = bosluk*bosluk_sayisi+satir
         S.enqueue(satir.rstrip("\n")) 

       else:
         satir = bosluk*bosluk_sayisi+satir
         S.enqueue(satir.rstrip("\n"))
        
    kaynak.close() 
            
    hedef = open(filename, 'w')   
    while not S.is_empty(): 
        hedef.write(S.dequeue()+"\n") 
      
    hedef.close() 
  
filename = "source.c"
tab_(filename)  #call
   
with open(filename) as file: 
        for f  in file.readlines() : 
            print(f,end ="") 
