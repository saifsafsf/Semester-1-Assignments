import math
import TilesInRoom      # Importing modules

num_rooms = int(input('Number of rooms: '))     # Taking number of rooms
size_tile = float(input('Size of a tile in sq. ft.: '))     # Area of a tile

list_rooms = list()
total_tiles = 0

for counter in range(1, num_rooms+1):

    list_room = list()      # The list for each room

    room_name = input(f'\nRoom {counter} Name: ')
    list_room.append(room_name)

    wid_room = float(input(f'{room_name}\'s Width in ft.: '))
    list_room.append(wid_room)      # width of room

    len_room = float(input(f'{room_name}\'s Length in ft.: '))
    list_room.append(len_room)      # length of room

    tiles_room = TilesInRoom.tiles_in_room(size_tile, wid_room, len_room)

    total_tiles += tiles_room

    tiles_room = math.ceil(tiles_room)      # Tiles per room
    total_tiles = math.ceil(total_tiles)    # Total tiles of all the rooms

    list_room.append(tiles_room)
    print(f'\nTiles required for {room_name}: {tiles_room}')
    list_rooms.append(list_room)    # The list for all the rooms

print(f'\nTotal number of tiles for all rooms: {total_tiles}\n')
num_boxes = total_tiles / 25    # Number of boxes of tiles

if total_tiles % 25 == 0:
    print(f'Required number of boxes of tiles (If 1 box = 25 tiles): {num_boxes}')

else:
    num_boxes2 = math.ceil(num_boxes)
    left_tiles = (num_boxes2 * 25) - total_tiles    # Tiles in total boxes - tiles we need

    print(f'Required number of boxes of tiles (If 1 box = 25 tiles): {num_boxes2}')
    print(f'From the last box, {left_tiles} tiles will be left unused.')
