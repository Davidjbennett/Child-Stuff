post = {"user_ID":209, "message":"Hello there", "language":"English", "datetime":"20201001T124231Z", "location":(44.890533, -104.715556)}
#key:value We have 5 in the above dictionary

post2 = {"message":"SS Cotopaxi", "language":"English"}

#! we are creating a new key here with the value
post2["user_ID"] = 209
post2["datetime"] = "20201001T124231Z"

print(post["message"])

#! gives us keyError. the key must be in the dictionary
# print(post2["location"])

#check for a key like this
if "location" in post2:
    print(post2["location"])
else:
    print("The location is not contained in post2")

#or
try:
    print(post2["location"])
except KeyError:
    print("The location is not contained in post2")

loc = post2.get("location", "There is no location")
print(loc)

# for key in post.keys():
#     value = post[key]
#     print(key, "=", value)

for key, value in post.items():
    print(key, "=", value)