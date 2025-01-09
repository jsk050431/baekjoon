n,l,d = map(int, input().split())
time = 0
listen = False

lt = l
dt = d
interval = 5
nextmusic = False
while True:

    if n != 0 and lt == 0 and interval != 0: # 한 곡 완곡시 중간무음 5초 카운트
        listen = True
        interval -= 1
        nextmusic = True

    elif nextmusic and interval == 0: # 5초 이후 다음곡 시작
        interval = 5
        lt = l
        n -= 1
        listen = False
        nextmusic == False

    if n == 1 and lt == 0: # 전곡 완곡시
        print(time+dt)
        break



    if dt == 0 and listen: # 전화벨 울리고 들었을때
        print(time)
        break

    elif dt == 0 and not(listen): # 전화벨 울렸지만 못들었을 때
        dt = d

    time += 1 # 총시간 증가

    if lt != 0: # 한 곡 재생시간 감소
        lt -= 1
    if dt != 0: # 전화벨 대기시간 감소
        dt -= 1
    # print('남은곡{} 남은시간{} 전화남은시간{} 총시간{} 인터벌{}'.format(n,lt,dt,time,interval))