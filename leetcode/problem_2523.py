#### Problem 2523. Closest Prime Numbers in Range
#### tags:  math, number theory

# hint:find prime numbers using sieve of eratosthenes
# ref: https://www.youtube.com/watch?v=mv9mycLruJ0

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.get_primes(left, right)
        result = [-1, -1]
        if(len(primes) == 1):
            return result

        minDiff = 100000
        for i in range(len(primes)-1):
            diff = primes[i + 1] - primes[i]
            if(diff < minDiff):
                minDiff = diff
                result = [primes[i], primes[i + 1]]
        return result
    
    def get_primes(self, left, right):
        is_prime = [True if i >= 2 else False for i in range(right + 1)]
        for i in range(2, int(right ** 0.5) + 1):
            if(is_prime[i]):
                for j in range(i*i, right+1, i):
                    is_prime[j] = False
        return [i for i in range(left, len(is_prime)) if is_prime[i] ]
