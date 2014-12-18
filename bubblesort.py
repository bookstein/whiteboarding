# with bubble sort, switch two pairs at a time

lst = [2,3,1,4,0, -1]

def bubbleSort(lst):
    done = False
    while not done:
        done = True
        for i in range(len(lst) - 1):
            if lst[i+1] < lst[i]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                print "switching", i, " with ", i+1
                done = False

    print "bubble:", lst

bubbleSort(lst)


def selectionSort(lst):
    for fillslot in range(len(lst) - 1, 0, -1):

        positionOfMax = 0

        # find biggest number in entire list, from 1 to fillslot (+1 to include fillslot)
        for i in range(1, fillslot + 1):
            if lst[i] > lst[positionOfMax]:
                positionOfMax = i

        # switch fillslot with biggest list number
        lst[fillslot], lst[positionOfMax] = lst[positionOfMax], lst[fillslot]

    print "selection:", lst

selectionSort(lst)
