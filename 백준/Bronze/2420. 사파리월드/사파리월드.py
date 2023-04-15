n, m = map(int, input().split())

sub = n - m
print(sub if sub >= 0 else sub * -1) 
