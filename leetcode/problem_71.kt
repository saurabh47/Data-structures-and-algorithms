// Problem 71. Simplify Path
// tags: stack
// company: Meta

class Solution {
    fun simplifyPath(path: String): String {
      var parts = path.split('/').filter { it != "." && it.isNotEmpty() }
      var stack = mutableListOf<String>()
      for (part in parts) {
        if (part == "..") {
          if (stack.size > 0) {
            stack.removeLast()
          }
        } else {
          stack.add(part)
        }
      }
      return "/" + stack.joinToString("/")
    }
  }