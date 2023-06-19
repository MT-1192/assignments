# a = dict([("name","sravya"),("no.",15)])
# print(a)

# a = dict([["name","sravya"],["no.",15]])
# print(a)

# a = dict([{"name","sravya"},{"no.",15},{"name","teju"}])
# print(a) #in sets keys and values order is also changing.

# a = dict((("name","sravya"),("no.",15),("name","teju"),("name","car")))
# print(a) # the last key value pair is taking as output.

a = dict[(("name","sravya"),("no.",15),("name","teju"),("name","car"))]
print(a)


