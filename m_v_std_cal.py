import numpy as np

def calculate(list):
    if len(list) !=  9:
        raise ValueError("List must contain nine numbers.")

# Convert  the list into a 3x3 numpy array
    part3 = []
    smaller_ls_size = 3
    for ele in range(0, len(list), smaller_ls_size):
        part3.append(list[ele:ele+smaller_ls_size])
    # list comprehension version
    #part3 = [list[ele:ele+chunk_size] for ele in range(0, len(list), smaller_ls_size)]
    
    # list_range = np.arange(len(list))
    # list3 = np.hsplit(list_range, 3)

    # print(part3)     #!!!testing!!!
    arr = np.asarray(part3)     # Convert the input to an array.
    # print(arr)        #!!!testing!!!

# Create lists containing different value aspects

    mean = []
    var = []
    std = []
    min = []
    max = []
    sum = []

# value of the dictionary - vertical matrix
    for i in range(3):
        mean1 = np.mean(arr[:, i])
        mean.append(mean1)

        var1 = np.var(arr[:, i])
        var.append(var1)

        std1 = np.std(arr[:, i])
        std.append(std1)

        min1 = np.min(arr[:, i])
        min.append(min1)

        max1 = np.max(arr[:, i])
        max.append(max1)

        sum1 = np.sum(arr[:, i])
        sum.append(sum1)

# value of the dictionary - horizontal matrix

    for horizon in arr:
        mean0 = np.mean(horizon)
        mean.append(mean0)

        var0 = np.var(horizon)
        var.append(var0)

        std0 = np.std(horizon)
        std.append(std0)

        max0 = np.max(horizon)
        max.append(max0)

        min0 = np.min(horizon)
        min.append(min0)

        sum0 = np.sum(horizon)
        sum.append(sum0)

# append the axis = 0 and axix = 1 values to the dictionary 
    meann = []
    varr = []
    stdd = []
    minn = []
    maxx = []
    summ = []
    for ele in range(0, 6, 3):
        meann.append(mean[ele:ele+smaller_ls_size])
        varr.append(var[ele:ele+smaller_ls_size])
        stdd.append(std[ele:ele+smaller_ls_size])
        minn.append(min[ele:ele+smaller_ls_size])
        maxx.append(max[ele:ele+smaller_ls_size])
        summ.append(sum[ele:ele+smaller_ls_size])

# value of the dictionary - flattened list

    means = np.mean(list)
    meann.append(means)

    vars = np.var(list)
    varr.append(vars)

    stds = np.std(list)
    stdd.append(stds)

    maxs = np.max(list)
    maxx.append(maxs)

    mins = np.min(list)
    minn.append(mins)

    sums = np.sum(list)
    summ.append(sums)

    left_curly_bracket = "{"
    right_curly_bracket = "}"
    diction_form = f"{left_curly_bracket}\n  'mean': {meann},\n  'variance': {varr},\n  'standard deviation': {stdd},\n  'max': {maxx},\n  'min': {minn},\n  'sum': {summ}\n{right_curly_bracket}"
    
    print(diction_form)

    
    # mean = [[np.mean(arr, axis = 0)], [np.mean(arr, axis = 1)], np.mean(list, dtype=np.float32)]
    # diction_form["mean"] = mean

    # variance = [[np.var(arr, axis = 0)], [np.var(arr, axis = 1)], np.var(list, dtype=np.float32)]
    # diction_form["variance"] = variance

    # std = [[np.std(arr, axis = 0)], [np.std(arr, axis = 1)], np.std(list, dtype=np.float32)]
    # diction_form["standard deviation"] = std

    # min = [[np.min(arr, axis = 0)], [np.min(arr, axis = 1)], np.min(list)]
    # diction_form["min"] = min

    # max = [[np.max(arr, axis = 0)], [np.max(arr, axis = 1)], np.max(list)]
    # diction_form["max"] = max

    # sum = [[np.sum(arr, axis = 0)], [np.sum(arr, axis = 1)], np.sum(list)]
    # diction_form["sum"] = sum

    # for value in diction_form.values():
    #     for sub_value in value[0:2]:
    #         str(sub_value).lstrip("array")
    #     print(value)
    
    # result = ""
    # for stat , val in diction_form.items():
    #     result += f"{stat}: {val}\n"

    # print(result)
    # return calculations

# TESTING 
print(calculate([10, 11, 12, 13, 14, 15, 16, 17, 18]))