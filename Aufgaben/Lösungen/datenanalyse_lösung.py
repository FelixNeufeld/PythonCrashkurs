import numpy as np

array = np.random.randint(0, 101, size=(1, 10))

mean_numpy = np.mean(array)
min_numpy = np.min(array)
max_numpy = np.max(array)

print(array)
print("Durchschnitt: " + str(mean_numpy))
print("Minimum" + str(min_numpy))
print("Maximum" + str(max_numpy))

# Beim Vergleich solltest du merken, dass Bibliotheken nützlich sind, da sie einen 
# arbeit abnehmen und den Fokus somit auf das lösen des Problems setzen kann.