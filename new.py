'''maps = [['$','*','*','*','*','*'],
        ['#','*','*','*','*','#'],
        ['*','*','#','#','*','#'],
        ['#','*','*','*','*','#'],
        ['*','*','*','#','#','#'],
        ['#','#','*','*','*','@']]
'''
rows = eval(input("请输入行数："))
columns =eval(input("请输入列数："))


#创建迷宫
maps=[]
print('请输入数据：')
for row in range(rows):
    map=input().split()
    maps.append(map)
for row in range(rows):
    print(maps[row])



#读取起点和终点坐标
for row in range(rows):
    for column in range(columns):
        if (maps[row][column]=='@'):
            qx=row
            qy=column
        if (maps[row][column]=='$'):
            zx=row
            zy=column


#正向标记列表
f=[]
for row in range(rows):
        f.append([])
        for column in range(columns):
            f[row].append(eval('-1'))  #全部初始化为-1
#print(f)


#逆向标记列表
b=[]
for row in range(rows):
        b.append([])
        for column in range(columns):
            b[row].append(eval('-1'))  #全部初始化为-2
#print(b)

dx=[1,0,-1,0]#四个方向移动向量  
dy=[0,1,0,-1]#四个方向移动向量
sx=5
sy=5
ey=0
ex=0

def walk(maze,sx,sy,ex,ey):
    #防止开始就在终点
    if(sx==ex and sy==ey):
        return 0
    #正向列表
    Q_f=[[sx,sy]]
    #print(Q_f)
    f[sx][sy]=0
    #print(f)
    #逆向列表
    Q_b=[[ex,ey]]
    b[ex][ey]=0
    #print(b)

    while (len(Q_f)!=0 and len(Q_b)!=0):
        
        if(len(Q_f)!=0):
            temp_1=Q_f.pop(0)
            #print(temp_1[0],temp_1[1])
        #四个方向移动（右，上，左，下）
        for i in range(4):
            nx = temp_1[0] + dx[i]
            ny = temp_1[1] + dy[i]
            #print(nx,ny)
            #判断在迷宫范围内没有走过并且可以走
            if (nx>=0 and nx<rows and ny>=0 and ny<columns and (maps[nx][ny]=='*' or maps[nx][ny]=='$') and f[nx][ny]==-1):
                #print(nx,ny)
                #将坐标加入队列末尾
                Q_f.append([nx,ny])
                #在标记列表内距离加一
                f[nx][ny]=f[temp_1[0]][temp_1[1]] + 1
            #print(b)
            #print(f)
            #如果逆向已经搜到这点
                if (b[nx][ny]!=-1):
                    #print(f)
                    #print("\n")
                    #print(b)
                    return f[nx][ny] + b[nx][ny]


        if(len(Q_b)!=0):
            temp_2=Q_b.pop(0)

        #四个方向移动（右，上，左，下）
        for i in range(4):
            nx = temp_2[0] + dx[i]
            ny = temp_2[1] + dy[i]
            #print(temp_2[0],temp_2[1])
            #判断在迷宫范围内没有走过并且可以走
            if (nx>=0 and nx<rows and ny>=0 and ny<columns and (maps[nx][ny]=='*' or maps[nx][ny]=='$') and b[nx][ny]==-1):
                #将坐标加入队列末尾
                Q_b.append([nx,ny])
                #在标记列表内距离加一
                b[nx][ny]=b[temp_2[0]][temp_2[1]] + 1

            #如果正向已经搜到这点
                if (f[nx][ny]!=-1):
                    #print(f)
                    #print("\n")
                    #print(b)
                    return f[nx][ny] + b[nx][ny]
            

s=walk(maps,sx,sy,ex,ey)
print('最少次数为%d'%s)