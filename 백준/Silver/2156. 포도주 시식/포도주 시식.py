n = int(input())

if n == 1:
    print(int(input()))
else:
    lst = [[int(input())]]
    amount = int(input())
    lst.append((amount, lst[-1][0]+amount))

    for _ in range(0, n-2):
        amount = int(input())
        jump = max(lst[-2])+amount  # 한칸 띄고 마시는 경우
        seq = lst[-1][0]+amount # 연속으로 마시는 경우
        no = max(lst[-1])   # 안마시는 경우
        lst.append((jump, seq, no))  #(한칸 띄고 마심, 이전꺼도 마심, 안마심)

    print(max(max(lst[-1]), max(lst[-2])))


