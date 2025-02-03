# This challenge is part of a tutorial track by MyCodeSchool and is accompanied by a video lesson.

# Problem Description:
# Given a pointer to the head of a singly-linked list, print each data value from the reversed list.
# If the given list is empty, do not print anything.

# Example:
# head refers to the linked list with data values: 1 → 2 → 3 → NULL
# Output:
# 3
# 2
# 1

# Function Description:
# Complete the reversePrint function in the editor below.

# reversePrint has the following parameters:
# - SinglyLinkedListNode pointer head: a reference to the head of the list.

# Prints:
# The data values of each node in the reversed list.

# Input Format:
# - The first line of input contains t, the number of test cases.
# - The input of each test case is as follows:
#   * The first line contains an integer n, the number of elements in the list.
#   * Each of the next n lines contains a data element for a list node.

# Constraints:
# 1 <= n <= 1000
# 1 <= list[i] <= 1000, where list[i] is the i-th element in the list.


def reversePrint(llist):
    if llist != None:
        if llist.next != None:
            reversePrint(llist.next)
        print(llist.data)