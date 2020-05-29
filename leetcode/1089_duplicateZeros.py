class Solution:
    def duplicateZeros(self, arr) -> None:
        res = []
        for x in arr:
            res.append(x)
            if x == 0:
                res.append(x)
        for i in range(len(arr)):
            arr[i] = res[i]
    
    #copied
    def duplicateZeros_1(self, arr) -> None:
        n = len(arr)
        zeros = 0
        i = 0
        while i + zeros < n:
            zeros += arr[i] == 0
            i += 1
		# i + zeros is at most n + 1
        i -= 1
        while zeros > 0:
            if i + zeros < n:
                arr[i+zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                arr[i+zeros] = arr[i]
            i -= 1