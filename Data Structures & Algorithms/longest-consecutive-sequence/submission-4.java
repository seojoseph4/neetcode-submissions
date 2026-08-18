class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> x = new HashSet<>();
        if (nums.length == 0) {
            return 0;
        }
        for(int i = 0; i < nums.length; i++) {
            x.add(nums[i]);
        }
        int maxCounter = 1;
        for(int y : nums) {
            if(!x.contains(y-1)) {
                int counter = 1;
                while (x.contains(y + 1)) {
                    y++;
                    counter++;
                }
                if(counter > maxCounter) {
                    maxCounter = counter;
                }
            }
        }

        return maxCounter;
    }
}
