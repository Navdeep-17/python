numbers = [3, 7, 2, 9, 5]
words = ["apple", "banana", "cherry"]
print("max():", max (numbers))
print("min():", min (numbers))
print("len():", len (words))
print("range():", list(range(1, 6)))
print("any():", any ([0, False, 5]))# any one condetion must be true
print("all():", all ([1, True, "hi"]))# all condetion must be true
print("sum():", sum (numbers))
                                   
print("enumerate():")
for i, w in enumerate (words):
    print(i, w)
                                   
print("eval():", eval ( " 5 + 10 +2" ))
print("list():", list)
print("sorted():", sorted (numbers))
print("reversed():", list(reversed (words)))