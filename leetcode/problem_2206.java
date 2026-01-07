// Problem 2206. Divide Array Into Equal Pairs (Easy)
//  tags: hashmap, array
class Solution {
    public boolean divideArray(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num:nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        boolean result = true;
        for(Integer key: map.keySet()){
            if(map.get(key) % 2 != 0){
                result = false;
                break;
            }   
        }
        return result;
    }
}

// Memory optimized solution

class Solution2 {
    public boolean divideArray(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for(int num:nums){
            if(set.contains(num)){
                set.remove(num);
            }else{
                set.add(num);
            }
        }
        return set.size() == 0;
    }
}