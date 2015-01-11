# from codesprint
# Enter your code here. Read input from STDIN. Print output to STDOUT

from sys import stdin, stdout

def print_tree(N, w, h):
    """Print ascii tree recursively -- in this case, upside-down..."""

    if N == 0:
        stdout.write("_" * w)
        return

    # straight part of Y
    for i in range(h):
        stdout.write("_" *(w/2) + "1" + "_"*(w/2) + "\n")

    # branched part of Y
    for i in range(1, h, 2):
        stdout.write("_" * (w/2 - i) + "1" + "_"*i + "1" + "_" * (w/2 - i) + "\n")

    print_tree(N-1, w/2, h/2), print_tree(N-1, w/2, h/2)

num_iter = stdin.readline()
print_tree(int(num_iter), 100, 16)
