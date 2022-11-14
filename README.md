# Item-personalized-bloom-filters

- A New concept/BF variant - a prototype to increase the efficiecy of bloom filters in terms of reducing the false positive rate

  by Krishnan Venkataraman and Kavya Vaddadi

Probabilistic data structures are effective in dealing with approximate membership querying, specifically while dealing with extremely large data-sets. Bloom filters are one such popular probabilistic data structures which can determine whether an item is definitely not present or probably present in processing larger data.

The Project :

Introducing a notion of item-personalized insertions in the context of traditional bloom filters which we refer as Item-personalized bloom filters (IBF). 

Initial empirical experimental evaluations show that IBF indeed helps to marginally reduce false positive rate while improvising on the space-efficiency.

The Core Idea:

Let n be the size of the bloom filter. Instead of fixed set of k-hash functions, we are going to initialize n-hash functions equivalent to the size of the filter.

Each slot of the filter holds a hash-function and a bit which is either set or not set (1 or 0). Over the n-hash functions, the input element x chooses k hash functions as its path. 

So, for every distinct element x, we get k number of hash-functions which are sequentially mapped as a path. This allows us to generate C(n, k) unique combinations (distinct paths that can be explored to set). 

For each distinct x, we get one of those combinations as an output path.


![image](https://user-images.githubusercontent.com/117613924/201556007-fb9e3489-3426-4315-9210-ae0f5619c63e.png)

For detailed information please refer Report.pdf


Emperical Plots:

![image](https://user-images.githubusercontent.com/117613924/201556190-790f96e4-fac2-4170-9aaa-daa3b1a3a4a2.png)

![image](https://user-images.githubusercontent.com/117613924/201556227-0be9feb7-7d74-49e8-b31b-354fd5d28ea6.png)


Experiment Details:

We conducted an empirical experiment to study the performance of Item personalised bloom
filter (IBF) in comparison with standard bloom filter (SBF). We took 10 different ratios of m and n beginning from
1 : 1 to 1 : 10 with an increment of 1 at each stage. We generated 10 different sets of random integers and for each set
we produce an insertion set and a query set. The query set was designed in such a way that it consists of 10% of data
from the insertion set and 90% data outside the insertion set. We ran a total of 100 trails wherein each set is inserted
and queried over the 10 different ratios of m and n and then for each trial, we calculated the winner data structure. The
winner was decided by the notion as which bloom filter (IBF or SBF) generated the least false positive rate.

We see that the IBF out-performed SBF by 13.79%. We also observe that there were a lot of
draws between the IBF and SBF. In the overall experiment we see that there was about 41.44% draws observed and also
there were several times the SBF outperformed the IBF. Still, we need rigorous trails with multiple parameter variations
to significantly state that IBF is performing better. We also observe that whenever the IBF is outperforming SBF, the
difference between the min value of IBF is considerable less than the min value of SBF – making it more interesting to
explore further in this direction. Figure 6 and Figure 7 show one of the above discussed sub-experiments showcasing
the performance difference between SBF and IBF with 10 fixed m : n ratios. We could see overall IBF showing lower
FPR in most cases.


