# find the left most point and let it be the first element
# then sort the points based on their slope to the left-most point
def sort_points(lst):
    sort_lst = []
    x_min = [99999, 99999]  # random super large number
    for i in lst:   # find out the left most point
        if i[0] < x_min[0]:
            x_min = i
    
    lst.remove(x_min)
    sort_lst.append(x_min)  # add left most to the list

    slope_list = []
    for i in lst:   # calculate the slope from every point to x_min
        slope = (i[1]-x_min[1])/(i[0]-x_min[0]) # delta y / delta x
        slope_list.append([i, slope])   # use list to store the information [point, slope]

    slope_list = sorted(slope_list, key=lambda x: x[1]) # sorted the points with slope
    for i in slope_list:    # add the tuples to the list we want to return
        sort_lst.append(i[0])
    
    # sort_lst starts from left most point and then go counter-clockwise
    return sort_lst


# find the points that make convex hull
def Graham_Scan_core(lst):
    stack = []
    for i in range(3):  # push first three points into stack
        stack.append(lst[i])
    
    for i in range(3, len(lst)):
        while stack != []:
            a, b = stack[-2], stack[-1] # the 2nd latest and latest points
            dot_product = (b[0]-a[0])*(b[0]-lst[i][0])+(b[1]-a[1])*(b[1]-lst[i][1]) # check the angle from a -> b -> i
            if dot_product > 0: # if this angle is acute
                stack.pop() # delete the latest point
            else:
                break
        stack.append(lst[i]) # push the new point on the stack
    
    return stack


def envelope_num(lst):
    x_max = [-99999, -99999]    # right most
    for i in lst:   # find the right most point
        if i[0] > x_max[0]:
            x_max = i
    
    upper, lower = 2, len(lst)

    i = 1
    while lst[i] != x_max:  # from left-most to right-most
        upper += 1  # number of points from left-most and right-most
        lower -= 1  # the number of points above are those not in the lower envelope
        i += 1
        
    print(upper, lower)

    return 


def main():
    num_of_lines = int(input())
    points = []
    for i in range(num_of_lines):
        nums = input().split()
        nums = [float(j) for j in nums]
        points.append(nums)

    sort_arr = sort_points(points)
    ch_arr = Graham_Scan_core(sort_arr)
    envelope_num(ch_arr)

    return 


main()