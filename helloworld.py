# David Rasmussen
# CS71 6/25/2024
import sys

if len(sys.argv) < 2:
    print("Usage: python helloworld.py <name>")
    exit(1)
name = sys.argv[1]
print(f"Hello {name}!")
