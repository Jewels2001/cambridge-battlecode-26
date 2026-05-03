import random, sys
from cambc import * # Controller, Direction, EntityType, Environment, Position

# non-centre directions
DIRECTIONS = [d for d in Direction if d != Direction.CENTRE]
class Player:

    def __init__(self):
        self.spawned = 0
        self.num = 0

    def run(self, ct: Controller) -> None:
        # win conditions
        # a - blow up core
        # b - deliver axionite (needs refining)
        # c - deliver titanium
        # d - most harvesters alive
        # e - zxionite stored
        # f - titanium stored

        entity = ct.get_entity_type()

        # run core:
        # max 50 units total including core (49 others)
        """
        if under a certain limit of bots, then spawn more
         can now check with c.get_unit_count() - 1 (core counts as 1) and - turrets
        """
        if entity == EntityType.CORE:
            if ct.get_unit_count() - 1 < 25 :
                # spawn builders
                for pos in DIRECTIONS:
                    spawn_pos = ct.get_position().add(pos)
                    if ct.can_spawn(spawn_pos):
                        ct.spawn_builder(spawn_pos)
                        self.spawned += 1
                        break

        # run bots:
        elif entity == EntityType.BUILDER_BOT:
            """
            bots need to:
            - place harvesters
            - place conveyors or bridges or both back
            - place some turrets near harvesters - splitter
            - place turrets near core?
            - destroy enemy squares - new attack (2 ti for 2 damage on tile standing on)
            """
            # 1st step = movement + roads + conveyors?
            # - placing conveyors on way out = already there
            # - placing conveyors on way back means slower getting resources back
            # - need to repair / replace destroyed ones

            # 2nd = deleting enemy harvesters if on tile

            # 3rd = placing harvesters if on tile

            # 4th = placing splitters beside harvester

            # 5th = placing turrets by splitter
            

            

        # run turrets? turrets are units
        elif entity == EntityType.GUNNER or entity == EntityType.SENTINEL or entity == EntityType.BREACH or entity:
            # if enemy in range, shoot
            # 1 - get enemy position
            enemies = ct.get_nearby_entities()
            # 2 check can fire
            for enemy in enemies:
                if ct.can_fire(enemy.get_position()):
                    ct.fire(enemy.get_position())
                    break
            # 3 fire





        