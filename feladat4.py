#4. feladat: gráfos
#https://cses.fi/problemset/task/1674
#4. feladat: gráfos

import sys

def get_subordinates(n, bosses):
    subordinates = [list() for i in range(n+1)]

    for i in range(2, n+1):
        subordinates[bosses[i-2]].append(i)

    result = (n+1)*[0]

    def enum_graph(employee_index):
        count = 0
        for i in subordinates[employee_index]:
            count += 1+enum_graph(i)
        result[employee_index] = count
        return count

    enum_graph(1)

    return [result[i] for i in range(len(result)) if i != 0]


input_data = sys.stdin.read().splitlines()
n = int(input_data[0])
boss_nodes = list(map(int, input_data[1].split()))
output = get_subordinates(n, boss_nodes)
print(output)
