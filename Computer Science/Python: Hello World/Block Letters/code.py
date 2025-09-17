# ASCII Art for "R" and "M"
R = [
    "RRRRR",
    "R   R",
    "RRRR ",
    "R  R ",
    "R   R"
]

M = [
    "M   M",
    "MM MM",
    "M M M",
    "M   M",
    "M   M"
]

# Function to print the ASCII art
def print_initials():
    # Print "R" first
    for line in R:
        print(line)
    print()  # Space between initials

    # Print "M" second
    for line in M:
        print(line)

# Call the function to print initials
print_initials()
