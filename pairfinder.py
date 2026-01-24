class pairfinder:
    def find(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

nums= (10, 10, 20, 30, 40, 50, 60, 70, 80, 90)
target= int(input("Enter your sum here: "))

result= pairfinder().find(nums, target)

if result:
    print("Number1= ", result[0], "Number 2=", result[1])
else:
    print("No match found")