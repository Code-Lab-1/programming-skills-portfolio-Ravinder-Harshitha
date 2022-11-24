
sample_dict = {
    "name": "Rob",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# keys to be removed
keys = ["salary", "city"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)


