import event

weapon = 0
battle = 0
Random = 0
mhp = 100
mmhp = 100
ehp = 0
answer = ""
keys = 2


rooms = {'room01':[1,0,0,0,0],
         'room02':[1,1,0,0,0],
         'room03':[0,1,1,0,1],
         'room04':[1,0,0,1,2],
         'room05':[1,1,0,0,0],
         'room06':[1,1,1,1,6],
         'room07':[0,0,0,1,7],
         'room08':[0,0,1,1,0],
         'room09':[0,0,1,1,0],
         'room10':[0,1,1,0,4],
         'room11':[1,1,0,0,0],
         'room12':[0,1,0,0,8],
         'room13':[1,1,0,0,0],
         'room14':[0,1,0,1,3],
         'room15':[1,0,1,0,4],
         'room16':[1,1,0,1,0],
         'room17':[0,0,1,0,9],
         'room18':[0,0,0,0,5]}
running = True
room_name = 'room01'
dir = 0

def enter(room_name):
    print(rooms[room_name])
    if len(rooms[room_name]) == 5:
        if rooms[room_name][4] == 1:
            event.gf(weapon)
            rooms[room_name][4] = 0
        elif rooms[room_name][4] == 2:
            event.tutorial(mhp)
            rooms[room_name][4] = 0
        elif rooms[room_name][4] == 3:
            event.battle1(mhp)
            rooms[room_name][4] = 0
        elif rooms[room_name][4] == 4:
            event.battle2(mhp)
            rooms[room_name][4] = 0
        elif rooms[room_name][4] == 5:
            event.boss(mhp)
            rooms[room_name][4] = 0
        elif rooms[room_name][4] == 6:
            event.shop(weapon,mmhp,answer)
            rooms[room_name][4] = 0
        elif rooms[room_name][4] == 7:
            event.key_room(keys,answer)
            rooms[room_name][4] = 0
        elif rooms[room_name][4] == 8:
            event.treasure1(weapon,answer)
            rooms[room_name][4] = 0
        elif rooms[room_name][4] == 9:
            event.treasure2(mmhp,answer)
            rooms[room_name][4] = 0
    print("어디로 가시겠습니까?")
    print("1.오른쪽\n2.왼쪽\n3.뒤\n4.앞\n")
    direction = int(input())

    return direction

def move(room_name, walls, direction):
    nextRoom = room_name
    if room_name == 'room01':
        if walls[direction-1] == 1:
            nextRoom = 'room02'
            print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")

    if room_name == 'room02':
        if walls[direction-1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room03'
                print(f"{nextRoom} 방")

            elif direction-1 == 1:
                nextRoom = 'room01'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")

    if room_name == 'room03':
        if walls[direction-1] == 1:
            if direction - 1 == 1:
                nextRoom = 'room02'
                print(f"{nextRoom} 방")

            elif direction-1 == 2:
                nextRoom = 'room04'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")
    
    if room_name == 'room04':
        if walls[direction-1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room05'
                print(f"{nextRoom} 방")

            elif direction-1 == 3:
                nextRoom = 'room03'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")

    if room_name == 'room05':
        if walls[direction-1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room06'
                print(f"{nextRoom} 방")

            elif direction-1 == 1:
                nextRoom = 'room04'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")  
    
    if room_name == 'room06':
        event.shop(weapon,mhp,answer)
        if walls[direction-1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room13'
                print(f"{nextRoom} 방")

            elif direction-1 == 1:
                nextRoom = 'room05'
                print(f"{nextRoom} 방")
            
            elif direction-1 == 2:
                nextRoom = 'room07'
                print(f"{nextRoom} 방")

            elif direction-1 == 3:
                nextRoom = 'room08'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")

    if room_name == 'room07':
        event.key_room(keys,answer)
        if walls[direction-1] == 1:
            if direction - 1 == 3:
                nextRoom = 'room06'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")      
    
    if room_name == 'room08':
        if walls[direction-1] == 1:
            if direction - 1 == 2:
                nextRoom = 'room06'
                print(f"{nextRoom} 방")

            elif direction-1 == 3:
                nextRoom = 'room09'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")  
    
    if room_name == 'room09':
        if walls[direction-1] == 1:
            if direction - 1 == 2:
                nextRoom = 'room08'
                print(f"{nextRoom} 방")

            elif direction-1 == 3:
                nextRoom = 'room010'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")  
    
    if room_name == 'room10':
        event.battle2(mhp)
        if walls[direction-1] == 1:
            if direction - 1 == 1:
                nextRoom = 'room11'
                print(f"{nextRoom} 방")

            elif direction-1 == 2:
                nextRoom = 'room09'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")
    
    if room_name == 'room11':
        if walls[direction-1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room10'
                print(f"{nextRoom} 방")

            elif direction-1 == 1:
                nextRoom = 'room12'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")
    
    if room_name == 'room12':
        event.treasure1(weapon,answer)
        if walls[direction-1] == 1:
            nextRoom = 'room11'
            print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")

    if room_name == 'room13':
        if walls[direction-1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room14'
                print(f"{nextRoom} 방")

            elif direction-1 == 1:
                nextRoom = 'room06'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")
    
    if room_name == 'room14':
        event.battle1(mhp)
        if walls[direction-1] == 1:
            if direction - 1 == 1:
                nextRoom = 'room13'
                print(f"{nextRoom} 방")

            elif direction-1 == 3:
                nextRoom = 'room15'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")
    
    if room_name == 'room15':
        event.battle2(mhp)
        if walls[direction-1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room16'
                print(f"{nextRoom} 방")

            elif direction-1 == 2:
                nextRoom = 'room14'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")
    
    if room_name == 'room16':
        if walls[direction-1] == 1:
            if direction - 1 == 3:
                nextRoom = 'room17'
                print(f"{nextRoom} 방")

            elif direction-1 == 1:
                nextRoom = 'room15'
                print(f"{nextRoom} 방")
            
            elif direction-1 == 3:
                nextRoom = 'room17'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")
    
    if room_name == 'room17':
        event.treasure2(mhp,answer)
        if walls[direction-1] == 1:
            if direction - 1 == 2:
                nextRoom = 'room16'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")

    if room_name == 'room18':
        event.boss(mhp)
        if walls[direction-1] == 1:
            if direction - 1 == 1:
                nextRoom = 'room16'
                print(f"{nextRoom} 방")

        else:
            print("이쪽은 막혀있다.")
    return nextRoom

while running:
    dir = enter(room_name)
    room_name = move(room_name, rooms[room_name], dir)