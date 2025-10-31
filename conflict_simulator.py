import random
import datetime

filename = "conflict_target.txt"

versions = [
    "Updated by main branch",
    "Changed in feature branch",
    "Tweaked line from another dev",
    "Feature: new implementation idea",
    "Main: hotfix applied",
]

new_line = random.choice(versions)
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(filename, "w") as f:
    f.write(f"{new_line} [{timestamp}]\n")

print(f"Simulated update: {new_line}")
