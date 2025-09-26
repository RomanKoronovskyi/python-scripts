"""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of followed by lines of commands
where each command will be of the  types listed above. Iterate through each command
in order and perform the corresponding operation on your list.
The first line contains an integer, denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

!!!Don't convert list to string for output!!!!
l = [1, 2, 3]
print(l) # correct
print(str(l) # wrong
"""

def main():
    """Perform list commands."""
    l = []
    n = int(input())

    for _ in range(n):
        command_line = input().split()
        command = command_line[0]

        if command == "insert":
            index = int(command_line[1])
            value = int(command_line[2])
            l.insert(index, value)
        elif command == "print":
            print(l)
        elif command == "remove":
            value = int(command_line[1])
            l.remove(value)
        elif command == "append":
            value = int(command_line[1])
            l.append(value)
        elif command == "sort":
            l.sort()
        elif command == "pop":
            l.pop()
        elif command == "reverse":
            l.reverse()

if __name__ == "__main__":
    main()
