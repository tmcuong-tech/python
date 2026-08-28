"""Concatenation is basically just adding strings together."""

message = "Hello," + " World!"
print(message)

message += " (and beyond)"
print(message)

some_iterable = ["I", "can", "be", "put", "together"]
joined = " ".join(some_iterable)
joined2 = ", ".join(some_iterable)
joined3 = "~~~".join(some_iterable)
print(joined)
print(joined2)
print(joined3)
