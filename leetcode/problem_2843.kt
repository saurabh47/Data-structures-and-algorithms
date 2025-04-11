// Problem 2843. Count Symmetric Integers
// tags: [math, simulation]

class Solution {
    fun countSymmetricIntegers(low: Int, high: Int): Int {
        var count = 0
        for(i in low..high){
            // two digit number
            if(i < 100 && i % 11 == 0){
                count += 1
            }
            // four digit
            if(i > 1000 && i<10000){
                // print("four digit= $i")
                // 8688 =>     8     +   688/100 = 6 => 14 
                var left = (i / 1000) + ((i % 1000) / 100) 
                // 8688 =>     8     +   88 / 10 = 8
                var right = (i % 10) + (i % 100) / 10
                // println("left = $left right=$right")
                if(left == right){
                    count += 1
                }
            }

        }
        return count
    }
}