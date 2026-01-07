/** Problem 278. First Bad Version (Easy) tags: Binary Search */

/* The isBadVersion API is defined in the parent class VersionControl.
fun isBadVersion(version: Int) : Boolean {} */

class Solution : VersionControl() {
    override fun firstBadVersion(n: Int): Int {
        /*
         * input: int n the latest version
         * output: int b: first bad version [1, n]
         *
         * exmple: 1 ,2, 3, 4 ,5, 6, 7, 8, 9, 10
         *         g, g, g, g, g, b, b, b, b, b
         */
        var start = 1
        var end = n
        while (start < end) {
            var mid = start + (end - start) / 2
            if (mid > 0 && !isBadVersion(mid - 1) && isBadVersion(mid)) {
                return mid
            }
            if (mid < n && !isBadVersion(mid) && isBadVersion(mid + 1)) {
                return mid + 1
            }

            if (!isBadVersion(start) && !isBadVersion(mid)) {
                start = mid
            } else {
                end = mid - 1
            }
        }
        return start
    }
}

class SolutionOptimized : VersionControl() {
    override fun firstBadVersion(n: Int): Int {
        /*
         * input: int n the latest version
         * output: int b: first bad version [1, n]
         *
         * exmple: 1 ,2, 3, 4 ,5, 6, 7, 8, 9, 10
         *         g, g, g, g, g, b, b, b, b, b
         */
        var start = 1
        var end = n
        while (start < end) {
            var mid = start + (end - start) / 2
            if (isBadVersion(mid)) {
                end = mid
            } else {
                start = mid + 1
            }
        }
        return start
    }
}

class VersionControl {
    fun isBadVersion(version: Int): Boolean {
        // This is a stub. The actual implementation will be provided by the system.
        return false
    }
}
