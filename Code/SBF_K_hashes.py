import xxhash
import subprocess
import os
import sys


def get_words(filename):
    return open(filename, "rb").read().decode("utf8", "ignore").strip().split()

class HashXX32(object):
    def __init__(self, seed):
        self.h = xxhash.xxh32(seed=seed)

    def hash(self, o):
        self.h.reset()
        self.h.update(o)
        return self.h.intdigest() % sys.maxsize

class BloomFilter(object):
    def __init__(self, size, num_hash, seeds):
        '''
        Initialize a Bloom filter.

        Inputs:
            - size: number of slots in the Bloom filter (n)
            - num_hash: number of hash functions (k)
            - seeds: seeds to initialize hash functions

        Raises:
            - ValueError if the number of seeds differ with num_hash
        '''
        self._size = size
        self._num_hash = num_hash
        self._hashers = [HashXX32(seed) for seed in seeds]
        #raise NotImplementedError()
        if num_hash != len(self._hashers):
            raise ValueError('Number of hash functions should equal number of seeds.')
        self._bits =  [False] * size

    def insert(self, obj) -> int:
        '''
        Insert an object into the Bloom filter.
        The object will be hashed with `self._num_hash` distinct hash functions.

        Inputs:
            - obj: a bytes-like object.
        
        Returns:
            - num_collision (int): number of collisions during this insertion operation.
        '''
        num_collision = 0
        #raise NotImplementedError()
        for hf in self._hashers:
            Hashvalue_Index=(hf.hash(obj))%(self._size)
            if self._bits[Hashvalue_Index]:
                num_collision+=1
            else:
                 self._bits[Hashvalue_Index]=True
            
        return num_collision
    
    def chec_query(self, obj) -> int:
        '''
        Insert an object into the Bloom filter.
        The object will be hashed with `self._num_hash` distinct hash functions.

        Inputs:
            - obj: a bytes-like object.
        
        Returns:
            - num_collision (int): number of collisions during this insertion operation.
        '''
    
        num_collision = 0
        Full_K_path_Collision=0
        #raise NotImplementedError()
        for hf in self._hashers:
            Hashvalue_Index=(hf.hash(obj))%(self._size)
            if self._bits[Hashvalue_Index]:
                num_collision+=1
           
        
        if num_collision>=self._num_hash:
            Full_K_path_Collision=1
        
        
        return Full_K_path_Collision 

    def __contains__(self, obj) -> bool:
        '''
        Check if an object is in the Bloom filter.

        Inputs:
            - obj: a bytes-like object.
        
        Returns:
            True if `obj` is in the filter; otherwise False.
        '''
        #raise NotImplementedError()
        for hf in self._hashers:
            Hashvalue_Index=(hf.hash(obj))%(self._size)
            if not self._bits[Hashvalue_Index]:
                return False
        return True
                
            

    def get_num_set_buckets(self) -> int:
        '''Return the number of set buckets in the Bloom filter.'''
        return sum(self._bits)

    def get_bit_vector(self):
        return ''.join([str(b*1) for b in self._bits])


def bf_insertion(bf, members):
    num_collision = 0
    for word in members:
        num_collision += bf.insert(word)

def bf_querying(bf, members):
    num_collision = 0
    total_words=0
    for word in members:
        num_collision += bf.chec_query(word)
        total_words+=1
    print("Number of items queried ",total_words)
    print("Number of items present ",num_collision)
    
    return num_collision


if __name__ == '__main__':
    words = [str(i) for i in range(10000)]
    print('SBF - with k hash functions ')
    # Grab the command line arguments
    start = 1
    end = 1001
    num_hash = 100
    bf_size =10000

    # Create Bloom Filter, and insert the set of words
    bf = BloomFilter(size=bf_size, num_hash=num_hash, seeds=range(num_hash))
    members = words[start:end]
    
    bf_insertion(bf, members)
    
    #Querying elements
    start1=1
    end1=101
    start2=end+1
    end2=start2+500
    query_members=words[start1:end1]+words[start2:end2]
    Total_items_alreadry_present=end1-start1
    Number_of_items_queriedpresent=bf_querying(bf, query_members)
    
    # False Positives calculation
    Items_wrongly_told_present=Number_of_items_queriedpresent-Total_items_alreadry_present
    FPR=Items_wrongly_told_present/len(query_members)
    print("Total Number of False Positives is ",Items_wrongly_told_present)
    print('FPR=',FPR)