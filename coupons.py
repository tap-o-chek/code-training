def count_ways_to_use_coupon(S, prices_category1, prices_category2):
    count = 0
    pointer1 = 0
    pointer2 = len(prices_category2) - 1

    while pointer1 < len(prices_category1) and pointer2 >= 0:
        total_price = prices_category1[pointer1] + prices_category2[pointer2]
        if total_price == S:
            count += 1
            pointer1 += 1
            pointer2 -= 1
        elif total_price < S:
            pointer1 += 1
        else:
            pointer2 -= 1

    return count

S = int(input())
prices_category1 = list(map(int, input().split()))
prices_category2 = list(map(int, input().split()))

result = count_ways_to_use_coupon(S, prices_category1, prices_category2)
print(result)
