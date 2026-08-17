"""String is immutable"""

name = "My name is Vikrant"

# Indexing, Slicing, Encoding, Decoding

print(f"Complete String : {name}")
print(f"Complete String : {name[0:]}")
print(f"Initial 7 Characters : {name[0:7]}")
print(f"7 to 10  Characters  : {name[7:10]}")
print(f"7 onwards  : {name[7:]}")
print(f"Reverse  : {name[::-1]}")
print(f"Skip 2 Characters  : {name[::2]}")

address = "Las vegas 😍"

encoded_string = address.encode("utf-8")
print(f"Encoded String : {encoded_string}")
coded_string = encoded_string.decode("utf-8")
print(f"Decoded String : {coded_string}")
