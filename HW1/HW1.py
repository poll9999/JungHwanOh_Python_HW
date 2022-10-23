katok = []
select=-1


def add_data(friend) :
    a = -1
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = friend

def des(katok):
    for i in range(len(katok)-1) :
        for j in range(i+1, len(katok)):
            x = katok[i].split(',')
            y = katok[j].split(',')
            if int(x[1].replace(')', '')) < int(y[1].replace(')', '')):
                int(x[1].replace(')', ''))
                katok[i], katok[j] = katok[j], katok[i]
    print(katok)

def delete_data(position) :
    if position <0 or position >= len(katok) :
        print("삭제할 데이터가 존재하지 않습니다.")
        return

    klen = len(katok)
    katok[position] = None

    for i in range(position + 1, klen) :
        katok[i-1] = katok[i]

    del(katok[klen-1])

while(select !=3) :

    select = int(input("선택하세요(1: 추가, 2:삭제, 3:종료)--> "))

    if(select == 1) :
        data = input("추가할 데이터--> ")
        add_data(data)
        des(katok)
    elif(select == 2) :
        pos = int(input("삭제할 위치--> "))-1
        delete_data(pos)
        if pos < 0 or pos >= len(katok):
            continue
        print(katok)
    elif select != 3:
        print("1~3 중 하나를 입력하세요.")
        continue