class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] ans =new int[k];
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int x : nums) {
            if(map.containsKey(x)) {
                int current = map.get(x) + 1;
                map.put(x,current);
            }
            else {
                map.put(x,1);
            }
        }

        PriorityQueue<Map.Entry<Integer, Integer>> heap = new PriorityQueue<>(
            (a,b) -> b.getValue() - a.getValue()
        );
        for(Map.Entry<Integer, Integer> entry: map.entrySet()){
            heap.add(entry);
        }

        for(int i=0; i<k; i++) {
            ans[i] = (int) heap.poll().getKey();
        }

        return ans;
    }
}
