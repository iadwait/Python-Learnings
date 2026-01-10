import json

data = {
    "name": "Adwait Barkale",
    "age": 20,
    "skills": ["iOS", "react-native", "python"]
}

# Write to json file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# read from json file
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print(f"Loaded Content: {loaded_data}")
print(f"Name = {loaded_data["name"]}")