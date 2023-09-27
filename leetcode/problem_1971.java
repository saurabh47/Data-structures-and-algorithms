// # Problem 1971: Find if Path Exists in Graph (Easy): https://leetcode.com/problems/find-if-path-exists-in-graph/description/

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if(source == destination)
            return true;
        HashMap<Integer, ArrayList<Integer>> paths = new HashMap<>(); 
        for(int node=0; node < edges.length; node++){
            int src = edges[node][0];
            int dst = edges[node][1];
            if(paths.containsKey(src)){
                final ArrayList<Integer> array = paths.get(src);
                if(!array.contains(dst)){
                    paths.computeIfAbsent(src, k -> new ArrayList<>()).add(dst);
                }
            }else{
                final ArrayList<Integer> array = new ArrayList<>();
                array.add(dst);
                paths.put(src, array);
            }

            if(paths.containsKey(dst)){
                final ArrayList<Integer> array2 = paths.get(dst);
                if(!array2.contains(src)){
                    paths.computeIfAbsent(dst, k -> new ArrayList<>()).add(src);
                }
            }else{
                final ArrayList<Integer> array = new ArrayList<>();
                array.add(src);
                paths.put(dst, array);
            }
        }
         System.out.println(paths);
        //  Traverse
        boolean result = Solution.traverse(paths, source, destination, new ArrayList<Integer>());
        return result;
    }

    public static boolean traverse(HashMap<Integer, ArrayList<Integer>> paths, int source, int destination, ArrayList<Integer> visited){
        if(paths.containsKey(source)){   
            final ArrayList<Integer> connections = paths.get(source);
            if(connections.contains(destination)){
                return true;
            }
            for(int i = 0; i < connections.size(); i++){
                int toVisit = connections.get(i);
                if(!visited.contains(toVisit)){
                    visited.add(toVisit);
                    boolean found = Solution.traverse(paths, toVisit, destination, visited);
                    if(found){
                        return found;
                    }
                }
            }
            return false;
        }else{
            return false;
        }
    }
}
