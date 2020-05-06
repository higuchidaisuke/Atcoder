import heapq as hp
N, M = [int(item) for item in input().split()]
price_list = sorted([-1 * int(item) for item in input().split()])

total_m = 0

def discount(price_list, ticket_num):
    total_ticket =0
    hp.heapify(price_list)

    while total_ticket < ticket_num:
        temp = hp.heappop(price_list)
        hp.heappush(price_list, -1* (-1*temp//2))
        total_ticket += 1

    return price_list

res = discount(price_list, M)
print(res)
print(-1 * sum(res))


N,M=map(int,input().split())
price_list=sorted([int(item) for item in input().split()])
total_m=0
def discount(price_list,tickets_num):
    total_ticket =0
    price_list.sort(reverse=True)

    while total_ticket < tickets_num:
        temp = price_list.pop(0)
        temp_new=temp//2
        price_list.append(temp_new)
        price_list.sort(reverse=True)
        total_ticket+=1
    return price_list

res = discount(price_list,M)
print(sum(res))
