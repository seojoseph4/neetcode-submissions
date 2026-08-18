class Solution {
    public int[] productExceptSelf(int[] nums) {
        int total = nums[0];
        int zero = nums[0];
        int counter =  0;
        for(int i = 1; i<nums.length; i++) {
            if (nums[i] != 0) {
                total *= nums[i];
            } else{
                counter++;
            }
            zero*=nums[i];
        }
        System.out.println(zero);
        System.out.println(total);
        int[] ans = new int[nums.length];
        for(int x = 0; x<nums.length; x++) {
            if (nums[x] != 0){
                ans[x] = zero/nums[x];
            }else{
                if (counter >1){
                    ans[x] = zero;
                } else{
                    ans[x] = total;
                }

            }
        }
        return ans;
    }
}  
