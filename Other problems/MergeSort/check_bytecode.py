import merge_sort_leftright as ms_slice
import merge_sort_temp as ms_temp
import merge_sort_islice as ms_islice
import dis
import sys

# fptr = open('out_test11.txt', 'w')
# fptr.write('dis merge_sort_leftright: \n')
# fptr.write(dis.dis(str(ms_slice.countInversions)))
# fptr.write(dis.dis(str(ms_slice.merge_sort)))
# fptr.write(dis.dis(str(ms_slice.merge)))

# fptr.write('\ndis merge_sort_temp: \n')
# fptr.write(dis.dis(str(ms_temp.countInversions)))
# fptr.write(dis.dis(str(ms_temp.merge_sort)))
# fptr.write(dis.dis(str(ms_temp.merge)))

# fptr.write('\ndis merge_sort_islice: \n')
# fptr.write(dis.dis(str(ms_islice.countInversions)))
# fptr.write(dis.dis(str(ms_islice.merge_sort)))
# fptr.write(dis.dis(str(ms_islice.merge)))

# fptr.close()

print('dis merge_sort_leftright: \n')
print(dis.dis((ms_slice.countInversions)))
print(dis.dis((ms_slice.merge_sort)))
print(dis.dis((ms_slice.merge)))

print('\ndis merge_sort_temp: \n')
print(dis.dis((ms_temp.countInversions)))
print(dis.dis((ms_temp.merge_sort)))
print(dis.dis((ms_temp.merge)))

print('\ndis merge_sort_islice: \n')
print(dis.dis((ms_islice.countInversions)))
print(dis.dis((ms_islice.merge_sort)))
print(dis.dis((ms_islice.merge)))