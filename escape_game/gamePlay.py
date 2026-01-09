import room
import event

running = True
room_name = 'room01'
dir = 0


while running:
    dir = room.enter("room_name")
    room_name = room.move(room_name, room.rooms[room_name], dir)
