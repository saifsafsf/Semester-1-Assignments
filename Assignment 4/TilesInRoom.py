def tiles_in_room(size_tile, wid_room, len_room):
    '''tiles_in_room(Size of tile, Room width, Room length)
        Returns number of tiles required for the specified room.'''     # Documentation
    
    area_room = len_room * wid_room     # Using formula
    tiles_room = area_room / size_tile     # To find how many tiles for that area
    return tiles_room
