#Ordered dictionary
# it remembers the insertion order

from collections import OrderedDict, defaultdict

# d = {"name" : "Toshi", "age" : "24", "id" : "123", "address" : "Pune"}
d = dict()
d['age'] = 24
d["name"] = "Toshi"
d["id"] = 123
d["address"] = "Pune"
print(d)

od = OrderedDict()
od['banana'] = 2
od['apple'] = 3
od['pear'] = 1
print(od)


dd = defaultdict(int)
print(dd)       # defaultdict(<class 'int'>, {})
