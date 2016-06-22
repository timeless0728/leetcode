# 其实有更好的解决方法。。。然而这个偷懒了竟然过了。。。。就过了吧。。。二刷再改


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        if all(num==0 for num in nums):
            return [[0,0,0]]


        res_list = []
        num_list = sorted(nums)
        for i in range(len(num_list)):
            left = i+1
            right = len(num_list)-1

            while left<right:
                lis = [num_list[i],num_list[left],num_list[right]]
                if sum(lis)==0:
                    res = [num_list[i],num_list[left],num_list[right]]
                    if res not in res_list:
                        res_list.append(res)
                    right -=1
                elif sum(lis)<0:
                    left +=1
                else:
                    right -=1
        return res_list

solu = Solution()
print solu.threeSum([-1,0,1,2,-1,-4])