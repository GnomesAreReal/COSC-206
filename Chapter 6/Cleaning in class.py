def read_inputs(num):
    """
    num is the number of boxes to read

    read the values of each box from the input and return it in a list
    """
    return_value = []
    for _ in range(num):
        box = input().split()
        box.pop(0)
        for i in range(len(box)):
            box[i] = int(box[i])
        return_value.append(box)
    return return_value


def all_boxes_ok(boxes):
    """
    boxes is a list of all boxes

    if all figures in the box are in ascending order, return true, otherwise return true.
    """
    for box in boxes:
        if not box_ok(box):
            return False
        return True


def box_ok(box):
    """

    """
    sorted_box = box.copy()
    sorted_box.sort()

    if box == sorted_box:
        return True
    else:
        return False


def get_endpoints(boxes):
    """
    boxes is the list of boxes

    return a list where each item is the first and last item of each box in a list
    """
    points = []
    for box in boxes:
        points.append([box[0], box[-1]])
    return points


def endpoints_in_order(points):
    for i in range(len(points) - 1):
        if endpoints[i][1] > endpoints[i + 1][0]:
            return False
        return True

# Main program

# Read input
n = int(input("# of boxes "))
boxes = read_inputs(n)

# Check if figures in each box are in ascending order
if not all_boxes_ok(boxes):
    print('NO')
else:

    # Get only the first and last of each box
    endpoints = get_endpoints(boxes)

    # Sort boxes
    endpoints.sort()

    # TODO Check if boxes are in order
    if endpoints_in_order(endpoints):
        print('YES')
    else:
        print('NO')
