import sys

a= sys.stdin.readline()[:-1]

dic = {}
dic['A'] = 3
dic['B'] = 3
dic['C'] = 3
dic['D'] = 4
dic['E'] = 4
dic['F'] = 4
dic['G'] = 5
dic['H'] = 5
dic['I'] = 5
dic['J'] = 6
dic['K'] = 6
dic['L'] = 6
dic['M'] = 7
dic['N'] = 7
dic['O'] = 7
dic['P'] = 8
dic['Q'] = 8
dic['R'] = 8
dic['S'] = 9
dic['T'] = 9
dic['U'] = 9
dic['V'] = 9
dic['W'] = 10
dic['X'] = 10
dic['Y'] = 10
dic['Z'] = 10

time = 0

for i in a:
    time += dic[i]
print(time)
