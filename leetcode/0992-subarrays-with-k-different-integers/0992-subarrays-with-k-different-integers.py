class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ln,lf = 0,0
        ans = 0
        hmap = defaultdict(int)
        for r in range(len(nums)):
            hmap[nums[r]]+=1
            while len(hmap)>k:
                hmap[nums[ln]]-=1
                if hmap[nums[ln]]==0:
                    del hmap[nums[ln]]
                ln+=1
                lf = ln
            while ln<len(nums) and hmap[nums[ln]]>1:
                hmap[nums[ln]]-=1
                ln+=1
            if len(hmap)==k:
                ans+=ln-lf+1
        return ans