
import pygame
import random
import Vars


class TerrainC:
    def __init__(self, screen, frog_pos):
        self.screen = screen
        self.terrains = self.initial_terrain()
        self.terrain_colors = [['grass', [92, 249, 87]], ['road', [42, 45, 61]], ['water', [50, 107, 209]]]
        self.frog_pos = frog_pos
        self.last_terrain_index = 0
        self.terrain_c = 0
        self.obj_frontier = Vars.screen_height - Vars.frog_size * 2

    def random_terrain(self):
        t_type = random.randint(0, 2)

        for _ in range(4):
            self.terrains.append([t_type, []])

    def initial_terrain(self):
        # Start with four terrains of grass(type 0)
        result = [[0, []], [0, []], [0, []], [0, []], [1, [0]], [1, []]]
        """
        Terrain height: Frog width * 4

        Terrain types
            0: Grass
            1: Road
            2: Water
        """
        for c in range(10):
            terrain_t = random.randint(0, 2)
            # Append the initial terrain values
            for _ in range(4):
                result.append([terrain_t, []])

        return result

    def remove_terrain(self):
        if self.last_terrain_index > 4:
            self.terrains = self.terrains[self.last_terrain_index:]
            self.last_terrain_index = 0

    def camera_movement(self, key_char):
        if key_char == 119:
            self.last_terrain_index += 1
            self.terrain_c += 1

            # Update obj frontier
            self.obj_frontier += 20

            # Insert a new terrain into the terrain list
            if self.terrain_c == 4:
                self.random_terrain()
                self.terrain_c = 0
        elif key_char == 115:
            if self.last_terrain_index > 0:
                self.last_terrain_index -= 1

                self.obj_frontier -= 20

    def draw_terrain(self):
        # Remove old terrain
        self.remove_terrain()

        screen_place = Vars.screen_height - Vars.terrain_height * 4

        for c, terrain in enumerate(self.terrains[self.last_terrain_index:]):
            # Get color
            color = self.terrain_colors[terrain[0]][1]

            pygame.draw.rect(self.screen, color,
                             [0, screen_place, Vars.screen_width, Vars.frog_size * 4])

            screen_place -= Vars.terrain_height

    def draw_objects(self):
        y_pos = self.obj_frontier
        for c, l in enumerate(self.terrains):
            if len(l[1]) > 0:
                for c_two, obj in enumerate(l[1]):
                    # Update object X position
                    self.terrains[c][1][c_two] += 1

                    # Draw object
                    pygame.draw.rect(self.screen,  [50, 50, 50],
                                     [obj, y_pos, Vars.frog_size * 4, Vars.frog_size * 2])

            y_pos -= Vars.frog_size


