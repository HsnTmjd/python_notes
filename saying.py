def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}. ")

def goodbye(name):
    print(f"Goodbye, {name}. ")

if __name__ == "__main__": # There is 2 underscores. We may find it hard to see in vs code
    main()

# As it turns out this '__name__' variable is a special symbol in python.
# It makes python to go to the target that we want it to go.
"""
When you run a Python script directly (e.g., by typing python script.py in the command line), the __name__ variable is set to "__main__".

When a Python script is imported as a module into another script, the __name__ variable is set to the name of the script (without the ".py" extension).

So, you can use if __name__ == "__main__": in your script to specify what code should run only when the script is the main program, and not when it's imported as a module.
 This helps keep your code organized and separate the parts meant for execution and parts meant for reuse in other scripts.
"""