from templates import templates

print("=" * 45)
print("🚀 .gitignore Generator")
print("=" * 45)

print("1. Python")
print("2. Node.js")
print("3. Java")

choice = input("\nChoose project type: ")

mapping = {
    "1": "python",
    "2": "node",
    "3": "java"
}

if choice not in mapping:
    print("❌ Invalid choice")
    exit()

project = mapping[choice]

with open(".gitignore", "w") as file:
    file.write(templates[project])

print("\n✅ .gitignore generated successfully!")
