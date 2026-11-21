import os


name = os.getenv("WHO_TO_GREET", "World")
print(f"Hello, {name}")