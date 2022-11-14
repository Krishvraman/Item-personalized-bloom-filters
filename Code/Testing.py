# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 17:59:17 2022


"""

import IP_Bloom_Filter
import SBF_K_hashes


words = [str(i) for i in range(10000)]
    

start = 1
end = 1001
members = words[start:end]
print('Number of items to be inserted m =' , end-start)


# Making number of Hash functions and size of the bloom filter to be the same
bf_size = 5000
num_hash =bf_size
print('Size of the bloom filter n =' , bf_size)
print('Total Number of hash functions = Size of bloom filter   ' , num_hash)

# Choice of hashes
K_path_size=10
print('Number of hash functions choosen ' , K_path_size)

# Create Bloom Filter, and insert the set of words
bf=IP_Bloom_Filter.IPBloomFilter(size=bf_size, num_hash=num_hash, seeds=range(num_hash), K=K_path_size)

#Inserting m elements 
IP_Bloom_Filter.bf_insertion(bf, members)


#Querying elements
start1=1
end1=101
start2=end+1
end2=start2+500
query_members=words[start1:end1]+words[start2:end2]
Total_items_alreadry_present=end1-start1


#Querying for IBP
print('\nItem personalised bloom filter ')
Number_of_items_queriedpresent=IP_Bloom_Filter.bf_querying(bf, query_members)
# False Positives calculation
Items_wrongly_told_present=Number_of_items_queriedpresent-Total_items_alreadry_present
FPR=Items_wrongly_told_present/len(query_members)
print("Total Number of False Positives is ",Items_wrongly_told_present)
print('FPR=',FPR)

# Inserting for SBF
num_hash=K_path_size
bf2 = SBF_K_hashes.BloomFilter(size=bf_size, num_hash=num_hash, seeds=range(num_hash))
SBF_K_hashes.bf_insertion(bf2, members)

#Querying
print('\nSBF - with k hash functions ')
Number_of_items_queriedpresent=SBF_K_hashes.bf_querying(bf2, query_members)
# False Positives calculation
Items_wrongly_told_present=Number_of_items_queriedpresent-Total_items_alreadry_present
FPR=Items_wrongly_told_present/len(query_members)
print("Total Number of False Positives is ",Items_wrongly_told_present)
print('FPR=',FPR)