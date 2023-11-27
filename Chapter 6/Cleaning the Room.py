def read_boxes(num):
    """
    Num is the number of boxes to read.

    Read the heights from the input and return it as a multidimensional array.
    """
    return_value = []
    for i in range(num):
        box = input().split()
        box.pop(0)
        for i in range(len(box)):
            box[i] = int(box[i])
        return_value.append(box)

    return return_value


def all_boxes_ascending(boxes):
    """
    Boxes is a list of boxes, each box is a list of integers.

    If the integers of each box are arranged in ascending order, return true, otherwise return false.
    """
    for box in boxes:
        if not is_box_ascending(box):
            return False
        return True


def is_box_ascending(box):
    """
    Box is a single array full of integers.

    Return true if the integers are in ascending order, otherwise return false.
    """
    sorted_box = box.copy()
    sorted_box.sort()

    if box == sorted_box:
        return True
    else:
        return False


def get_endpoints(boxes):
    """
    Boxes is a list of boxes, each box is a list of integers.

    Return a list where each value is a list consisting of only the first and last item in the box
    """
    points = []
    for box in boxes:
        points.append([box[0], box[-1]])
    return points


def endpoints_in_order(endpoints):
    """
    No documentation for you.
    """
    for i in range(len(endpoints) - 1):
        if endpoints[i][1] > endpoints[i+1][0]:
            return False
        return True


# Main program

# read input
n = int(input())
boxes = read_boxes(n)

# check if the figures *in each box* are in ascending order
if not all_boxes_ascending(boxes):
    print('NO')
else:
    # remove all but first and last figure from each box
    endpoints = get_endpoints(boxes)

    # sort boxes
    endpoints.sort()

    # check if figures are in order
    if endpoints_in_order(endpoints):
        print('YES')
    else:
        print('NO')
