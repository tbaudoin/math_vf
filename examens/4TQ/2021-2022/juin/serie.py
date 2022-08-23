from matplotlib.pyplot import vlines


serie = "6;1;5;3;2;1;6;4;1;3;4;5;4;3;5;3;5;1;2;6".split(";")
keys = (1,2,3,4,5,6)
values = (serie.count(str(i)) for i in keys)
data = dict(zip(keys, values))
print(data)
print(sum(data.values()))