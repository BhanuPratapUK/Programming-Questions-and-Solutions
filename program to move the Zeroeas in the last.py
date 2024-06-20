
def moveZeroes(nums):#[0,1,0,3,12],[1,0,0,3,12],[1,3,0,0,12]
    anchor = 0#updated by 1, updated by 2
    for explorer in range(len(nums)):#0,1,2,3,4
         if nums[explorer] != 0:
         # nums[0]->0!=0 (False),nums[1]->1!=0(True),nums[2]->0!=0(False),
         # nums[3]->3!=0(True),nums[4]->12!=0(True)
          nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                #nums[0],nums[1]->0,1=1,0
                # nums[1],nums[3]->0,3=3,0
                #nums[2], nums[4]->0,12=12,0
          anchor += 1#1,2
            #End The List will be like this
            # #[0,1,0,3,12]
            # [1,0,0,3,12]
            # [1,3,0,0,12]
            # [1,3,12,0,0]
    print('Here the sorted list after moving Zeroes-->',nums)
nums= [0,1,0,2,3,12]
moveZeroes(nums)