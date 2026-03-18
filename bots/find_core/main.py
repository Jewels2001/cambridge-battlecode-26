"""
Each unit gets its own Player instance; the engine calls run() once per round.
Use Controller.get_entity_type() to branch on what kind of unit you are.
"""

import random, sys

from cambc import * # Controller, Direction, EntityType, Environment, Position

# non-centre directions
DIRECTIONS = [d for d in Direction if d != Direction.CENTRE]

class Player:
    def __init__(self):
        self.num_spawned = 0 # number of builder bots spawned so far (core)

    def run(self, ct: Controller) -> None:
        scale_percent = ct.get_scale_percent()
        etype = ct.get_entity_type()
        my_id = ct.get_id()
        if etype == EntityType.CORE:
            if scale_percent <= 200:
            #if self.num_spawned < 3:
                # if we haven't spawned builder bots yet, try to spawn one on a random tile
                spawn_pos = ct.get_position().add(random.choice(DIRECTIONS))
                if ct.can_spawn(spawn_pos):
                    ct.spawn_builder(spawn_pos)
                    self.num_spawned += 1
        elif etype == EntityType.BUILDER_BOT:
            print(f"Builder bot {my_id} here! :)", file=sys.stderr)
            # if we are adjacent to an ore tile, build a harvester on it
            for d in Direction:
                check_pos = ct.get_position().add(d)
                if ct.can_build_harvester(check_pos):
                    ct.build_harvester(check_pos)
                    break
            # get current tile ID
            cur_tile_id = ct.get_tile_building_id(ct.get_position().add(Direction.CENTRE))
            #if cur_tile_id and ct.get_team(cur_tile_id) == Team.B and ct.get_entity_type(cur_tile_id) == EntityType.CORE:
            #    ct.self_destruct()
                #self.num_spawned -= 1

            #self.random_move(ct, my_id)
            self.move_explore(ct, my_id)
            # # move in a random direction
            # move_dir = random.choice(DIRECTIONS)
            # move_pos = ct.get_position().add(move_dir)
            # # we need to place a conveyor or road to stand on, before we can move onto a tile
            # if ct.can_build_conveyor(move_pos):
            #     ct.build_conveyor(move_pos)
            # #if ct.can_build_road(move_pos):
            # #    ct.build_road(move_pos)
            # if ct.can_move(move_dir):
            #     ct.move(move_dir)
            
            # let's see if we can destroy the core
            #building_pos = ct.get_position().add(Direction.CENTRE)
            #if ct.can_destroy(building_pos):
            #    ct.destroy(building_pos)
            #    ct.self_destruct()

        #scale_percent = ct.get_scale_percent()
        print(f"Cost scaling: {scale_percent} :)") #, file=sys.stderr
        print(f"Num spawned: {self.num_spawned}", file=sys.stderr)


            ## place a marker on an adjacent tile with the current round number
            #marker_pos = ct.get_position().add(random.choice(DIRECTIONS))
            #if ct.can_place_marker(marker_pos):
            #    ct.place_marker(marker_pos, ct.get_current_round())
    
    """
    Move in a random direction

    """
    def random_move(self, ct: Controller, my_id: int) -> None:
        print(f"Builder bot {my_id} trying to move in a random direction! :)", file=sys.stderr)
        move_dir = random.choice(DIRECTIONS)
        move_pos = ct.get_position(my_id).add(move_dir)
        # we need to place a conveyor or road to stand on, before we can move onto a tile
        #if ct.can_build_conveyor(move_pos):
        #    ct.build_conveyor(move_pos)
        if ct.can_build_road(move_pos):
            ct.build_road(move_pos)
        if ct.can_move(move_dir):
            ct.move(move_dir)

    def move_explore(self, ct: Controller, my_id: int) -> None:
        # try to move in a new direction
        move_dir = None # random.choice(DIRECTIONS)
        move_pos = None
        for move_dir in Direction:
            move_pos = ct.get_position().add(move_dir)
            # we need to place a conveyor or road to stand on, before we can move onto a tile
            if ct.can_build_road(move_pos):
                ct.build_road(move_pos)
                if ct.can_move(move_dir):
                    ct.move(move_dir)
            else:
                continue
        if (not move_dir) or (not move_pos):
            print("Couldn't find a direction to move in :( - will self destruct", file=sys.stderr)
            print("Couldn't find a direction to move in :( - will self destruct")
            ct.self_destruct()

        #if ct.can_build_conveyor(move_pos):
        #    ct.build_conveyor(move_pos)

    