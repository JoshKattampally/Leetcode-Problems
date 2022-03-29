class Solution {
    public int findDuplicate(int[] nums) {
        Set<Integer> visited = new HashSet<Integer>();
        for (int num : nums) {
            if (visited.contains(num))
                return num;
            visited.add(num);
        }
        return -1;
    }
}