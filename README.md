# Standardizing Nature-inspired Algorithms: a unified framework UNIOA for seven swarm-based algorithms
- [ Main Work ](#ov)
- [ Experiments ](#ep)
  - [ Group 1 ](#ep1)
  - [ Group 2 ](#ep2)
  - [ Group 3 ](#ep3)
- [ Benchmark Environment ](#env)
- [ Pseudo-code of algorithms in UNIOA ](#exm)
- [ Notes ](#cod)

<a name="ov"></a>
## Main work
For solving the problem that most of the modern swarm-based optimization algorithms are frequently repeating similar core ideas, we proposed a unified framework UNIOA in which seven different swarm-based optimization algorithms can be represented in same terminologies with same tuples. Meanwhile, the positions of these tuples are also same when building up these seven algorithms.
```math
UNIOA = (f, Init_x, Opt_x, C, T, S, Init_delta, Opt_delta)
```
![UNIOA_pseudocode](UNIOA_pseudocode.png)

<a name="ep"></a>
## Experiments 
We did three groups of experiments.
<a name="ep1"></a>
### Group 1 
The Group 1 is for avoiding side effects. In our many experiments, we found the way of evaluating the fitness and the way of calculating the global best individual might impact the performance of algorithms. The experimental results show that the way of evaluating the fitness will not impact the performance of algorithm, but the way of calculating the global best individual will.

Therefore, when we reproduced the original implementation, we kept the way of evaluating fitness as its original way, but modified the way of calculating the global best individual as the way in our unified framework.
| item | meaning |
| ----- | ------- |
| synchronous E | the way of evaluating is synchronous=evaluate the whole population together (at the same time) |
| asynchronous E | the way of evaluating is asynchronous=evaluate the whole individuals one by one |
| synchronous G | the way of calculating the global best individual (G) is synchronous=directly get the (G) in the updated whole population= the G is same to the whole individuals in the next round|
| asynchronous G | the way of calculating the global best individual (G) is asynchronous=get the (G) by iteratively comparing the updated individuals one by one=the G might be different to the whole individuals in the next round |

<a name="ep2"></a>
### Group 2 
The Group 2 is for verifying our unified framework can work correctly as their original framework.

| file name | usage | status | output name |
| --------- | ----- | ------ | ------------|
| orig_MBO.py  | reproduce original implementation|synchronous E + synchronous G | orig_MBO_syncE_syncG, orig_MBO |
| orig_MBO_asyncE_syncG.py  | modify original implementation|asynchronous E + synchronous G | orig_MBO_asyncE_syncG |
| orig_MBO_asyncE_asyncG.py  | modify original implementation|asynchronous E + asynchronous G | orig_MBO_asyncE_asyncG |


<a name="ep3"></a>
### Group3 









Click [here](https://surfdrive.surf.nl/files/index.php/s/sffBTtaFT5Yynrx) to access all data and referenced papers used in this thesis project.





<a name="cod"></a>
## Notes
1. avoid side effects of ``=``, must use ``copy.copy()`` somewhere. For example, when you need to create a new variable that is equal to the old variable, but not throw away the old one. Specifically, if you will use the right-variable in the following steps, please use ```copy.copy(single_number)/[list/array].copy()```. Moreover, ``def`` cannot avoid this kind of errors, and must use copy
2. mithril.liacs.nl
3. octiron.liacs.nl
4. duranium.liacs.nl