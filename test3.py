import numpy as np

arr=np.array(
    [
        [0,0,0],
        [0,0,0],
        [1,0,1]
    ]
)
# arr_axis0=arr.any(axis=0)  in which column non zero comes return true for that
# arr_axis1=arr.any(axis=1)

# arr_axis0=np.where(arr.any(axis=0))[0][0]   /* get the column indices */


# print(arr_axis0)
# # print(arr_axis1)