
# coding: utf-8

# In[ ]:


import sys
import numpy as np

def loot(capacity, weights, values):
    #print(values)
    val_per_weight=np.random.randint(1, 100, len(values))
    for n in range(len(values)):
        val_per_weight[n]=values[n]/weights[n]
    sort_val_per_weight=np.sort(val_per_weight)
    a=np.random.randint(1, 100, len(values))
    sort_val_per_weight=sort_val_per_weight[::-1]
    sort_weights=np.random.randint(1, 100, len(values))
    sort_values=np.random.randint(1, 100, len(values))
    for i in range(len(values)):
        for j in range(len(values)):
            if sort_val_per_weight[i]==val_per_weight[j]:
                a[i]=j
    #print(sort_val_per_weight)
    for p in range(len(weights)):
        sort_values[p]=values[a[p]]
    #print(sort_values)
    for k in range(len(weights)):
        sort_weights[k]=weights[a[k]]
    #print(sort_weights)
    load=0
    
    for l in range(len(sort_weights)):
        if load<capacity:
            load=load+sort_weights[l]
            last_weight=l
            #print(load)
    flag=0
    if load>capacity: 
        flag=1
        last_weight_proportion=(capacity-(load-sort_weights[last_weight]))/sort_weights[last_weight]
        load=capacity
        #print(last_weight_proportion)
    #print(flag)
    final_value=0
    
    for m in range(last_weight):
            final_value=final_value+sort_values[m]
    if flag==1:
        final_value=final_value+last_weight_proportion*sort_values[last_weight]
    else:
        final_value=final_value+sort_values[last_weight]
    #print(final_value)                                       
    return final_value
                                                        
                                                        
                                           
    
if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = loot(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    


# In[ ]:



    

