todolist = []
truelist = []

while True:    
    yarukoto = input('やること')
    if yarukoto == "z" and "ｚ":
        break
    elif len(yarukoto)==0:
        print("未入力")
    else:
        todolist.append(yarukoto)
        truelist.append('未達成')
        print('追加しました')
        
print(todolist)

listnum = len(todolist)

print('-----------登録済みのタスク----------')

for num in range(listnum):
    if listnum == 0:
        print("データがありません")
    else:
        print(f"やること {num + 1} : {todolist[num]} ステータス : {truelist[num]})")

while True:
    test = int(input('入力'))
    test_num = test-1
    do = True

    if (test > listnum):
        print('エラー : リスト数字外')  
    else:
        if truelist[test_num] == '達成':
            print('既にタスクを終えています')
            
        elif truelist[test_num] == '未達成':
            truelist[test_num] = '達成'
            if (test == 0):
                print('管理を中断します')
                break
            else:
                print('------------残りのタスク-----------')
                for num in range(listnum):
                    print(f"やること {num + 1} : {todolist[num]} ステータス : {truelist[num]})")
