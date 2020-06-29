# This code produces the first found magic square using backtracking with the numbers 
# 1 - 9, if the number 5 is already in the middle at the beginning:

# For an explanation for this approach see:

# https://www.researchgate.net/publication/
# 317019849_A_not_unlikely_interpretation_of_Goethe%27s_Hexeneinmaleins_
# -Eine_nicht_unwahrscheinliche_Interpretation_des_Goethe%27schen_Hexeneinmaleins 

# magic_square = [[0, 0, 0],
#                 [0, 5, 0],
#                 [0, 0, 0]]

nums = [0] * 8

def check_sum(i1, i2, i3):
    nums5 = nums[:]
    nums5.insert(4, 5)
    if (nums5[i1] != 0 and nums5[i2] != 0 and nums5[i3] != 0 and
      ((nums5[i1] + nums5[i2] + nums5[i3]) != 15)):
        return False
    else:
        return True

def check_all_sums():
    if (check_sum(0, 1, 2) and check_sum(3, 4, 5) and check_sum(6, 7, 8) and
        check_sum(0, 3, 6) and check_sum(1, 4, 7) and check_sum(2, 5, 8) and
        check_sum(0, 4, 8) and check_sum(2, 4, 6)):
        return True
    else:
        return False

def back_and_next_option(num):
    if num == 4:
        num += 2
    else:
        num += 1
    return num

def fill(i, num, nums):
    print(num)
    nums[i] = num
    print(nums)
    if nums[5] + nums[6] + nums[7] == 15:
        return nums    
    if len(nums[0:i+1]) != len(set(nums[0:i+1])) or not check_all_sums():
        if num < 9:
            num = back_and_next_option(num)
        else:
            while nums[i] == 9:
                nums[i] = 0
                i -= 1
            num = nums[i]
            num = back_and_next_option(num)
        fill(i, num, nums)
        return nums
    else:
        i += 1
        num = 1
        fill(i, num, nums)
        return nums

fill(0, 1, nums)
nums.insert(4, 5)
magic_square = [nums[:3], nums[3:6], nums[6:]]
print(magic_square)
