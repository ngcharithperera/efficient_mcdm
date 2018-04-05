import numpy as np# learn more: https://python.org/pypi/numpy


def generate_all_combinations(n,total):
  if n == 1:
      yield (total,)
  else:
    for i in range(total + 1):
      for j in generate_all_combinations(n - 1,total - i):
        yield (i,) + j
                
                
filtering_combinations = np.asarray(list(generate_all_combinations(3,20)))
print(len(filtering_combinations))
print(filtering_combinations)


from operator import itemgetter

x = [('CP1',3), ('CP2', 8), ('CP3', 5), ('CP4', 2)]
y =sorted(x, key=lambda student: student[1]) 
print(y)
sorted(x, key=itemgetter(0))
print(x)





