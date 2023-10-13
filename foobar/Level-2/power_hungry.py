def solution(xs):
    negatives = []
    # if odd number of negatives remove negative(max)
    for number in xs:
        if(number<0):
            negatives.append(number)
    if(len(negatives) %2 != 0 and len(xs) > 1):
        to_remove = max(negatives)
        xs.remove(to_remove)

    max_prod = xs[0]
    min_prod = xs[0]

    result = max_prod
    for i in range(1, len(xs)):
        if xs[i] == 0:
            if result < 0:
                result = 0
            pass
        else:
            max_result = max_prod * xs[i]
            min_result = min_prod * xs[i]
            max_prod = max(min_result, max(max_result, xs[i]))
            min_prod = min(max_result, min(min_result, xs[i]))
            result = max(result, max(max_prod, min_prod))
    return str(result)