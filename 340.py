arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort()
if arr1[0] == arr2[0] and arr1[1] == arr2[1] and arr1[2] == arr2[2]:
	print('Boxes are equal')
elif arr1[2] >= arr2[2] and arr1[1] >= arr2[1] and arr1[0] >= arr2[0]:
	print('The first box is larger than the second one')
elif arr1[2] <= arr2[2] and arr1[1] <= arr2[1] and arr1[0] <= arr2[0]:
	print('The first box is smaller than the second one')
else:
	print('Boxes are incomparable')
