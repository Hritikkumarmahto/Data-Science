import random
import time
import numpy as np
from collections import Counter
from scipy import stats   # for mode


# Generate 100000 values from 1-1000

data=[random.randint(1,1000) for _ in range(1000000)]
np_data=np.array(data)


# implement from scratch

def mean_from_Scratch(arr):
  return sum(arr)/len(arr)



def median_from_scratch(arr):
  sorted_arr=sorted(arr)
  n=len(sorted_arr)
  mid=n//2

  if n%2==0:
    return (sorted_arr[mid-1]+sorted_arr[mid])/2
  else:
    return sorted_arr[mid]

def mode_from_scratch(arr):
  freq=Counter(arr)
  max_freq=max(freq.values())
  modes=[k for k, v in freq.items() if v==max_freq]

  return modes[0] if len(modes)==1 else modes # return first max

# time from scratch 

start=time.time()
mean_s=mean_from_Scratch(data)
median_s=median_from_scratch(data)
mode_s=median_from_scratch(data)
end=time.time()

scratch_time=end-start

# _________________________________________________________________________________
#        
#                         USING NUMPY BUILD IN FUNTION
# _________________________________________________________________________________

start_np=time.time()
mean_np=np.mean(np_data)
median_np=np.median(np_data)
mode_np=stats.mode(np_data,keepdims=True).mode[0]     # numpy doesnt have build in function for mode so used scipy
end_np=time.time()
scratch_time_np=end_np-start_np



print("  From Scratch  ")
print("1. Mean - ",mean_s)
print("2. Median - ",median_s)
print("3. Mode - ", mode_s)
print("----Time-----",scratch_time)



print(" Using build in Numpy ")
print("1. Mean - ",mean_np)
print("2. Median - ",median_np)
print("3. Mode - ", mode_np)
print("-------Time-----",scratch_time_np)


print("speed_up_time",scratch_time/scratch_time_np)