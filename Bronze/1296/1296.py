name = input()
teamname = []
for i in range(int(input())):
    teamname.append([input(), 0])


for j in teamname:
    L = name.count('L') + j[0].count('L')
    O = name.count('O') + j[0].count('O')
    V = name.count('V') + j[0].count('V')
    E = name.count('E') + j[0].count('E')
    j[1] = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100

teamname.sort(key=lambda x:(-x[1], x[0]))
print(teamname[0][0])