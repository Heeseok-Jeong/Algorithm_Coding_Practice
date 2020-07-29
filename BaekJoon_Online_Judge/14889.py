import sys
from itertools import combinations

def read_sys():
    return sys.stdin.readline()

def get_combi_list(combi_list):
    n_list = [i for i in range(1, n+1)]
    combi = list(combinations(n_list, n//2))
    len_combi = len(combi)
    for i in range(len_combi//2):
        temp = []
        temp.append(list(combi[i]))
        temp.append(list(combi[len_combi-1-i]))
        combi_list.append(temp)

def compute_team_stat(team):
    value = 0
    for i in team:
        for j in team:
            value += info_list[i-1][j-1]
    return value

def get_min_stat_dif():
    combi_list = []
    diff_list = []
    get_combi_list(combi_list)
    for team_a, team_b in combi_list:
        v_team_a = compute_team_stat(team_a)
        v_team_b = compute_team_stat(team_b)
        diff_list.append(abs(v_team_a - v_team_b))
    return diff_list

n = int(read_sys())
info_list = [list(map(int, read_sys().split())) for _ in range(n)]
diff_list = get_min_stat_dif()
print(min(diff_list))
