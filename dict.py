deta = {
    "name": "Fahad",
    "caste": "Bhatti",
    "age": 18,
    "Gender" :"male",
    "Subject": "python"
}
print(deta)
print(deta["name"])
print(deta.get("city"))
print(deta.keys())
print(deta.values())


# using loop print data keys
for key in deta.keys():
    print(key) 

# using loop print data values
for value in deta.values():
    print(value) 

# using loop print data keys and values
for key in deta.keys():
    print(key,":",deta[key])