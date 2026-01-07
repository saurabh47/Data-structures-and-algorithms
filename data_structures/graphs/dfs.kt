import java.io.*;
import java.util.*;
import kotlin.collections.hashMapOf
import kotlin.comparisons.maxOf

class Solution{

  fun dfs(edges: Array<IntArray>, source: Int): Unit {

    var visited: HashSet<Int> = HashSet<Int>()
    var adj: HashMap<Int, MutableList<Int>> = HashMap<Int, MutableList<Int>>()
    
    fun dfsHelper(source: Int):Unit{
      if(visited.contains(source)){
        return
      }
      print("$source->")
      visited.add(source)
      var neighbors = adj.getOrDefault(source, mutableListOf<Int>())
      for(neighbor in neighbors){
        dfsHelper(neighbor)
      }
    }

    for(edge in edges){
      var (start, end) = edge;
      if(!adj.containsKey(start)){
        adj.put(start, mutableListOf<Int>())
      }
      if(!adj.containsKey(end)){
        adj.put(end, mutableListOf<Int>())
      }
      adj[start]?.add(end)
      adj[end]?.add(start)
    }

    println("adj list= $adj")
    for(node in adj.keys){
      if(!visited.contains(node)){
        dfsHelper(node);
      }
    }
  }
}


fun main(){
  var solution = Solution()
  var edges = arrayOf<IntArray>(
    intArrayOf(0, 1),
    intArrayOf(2, 3),
    intArrayOf(0, 2),
    intArrayOf(1, 3),
    intArrayOf(1, 4),
    intArrayOf(3, 4),
    intArrayOf(5, 6),
    intArrayOf(6, 7));
  
  /*      0-------1----4        5
   *      |       |   /         |
   *      |       |  /          |
   *      2-------3/            6-------7
  */

  var source = 1
  solution.dfs(edges, source)
}