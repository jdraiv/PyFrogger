
import pygame
import random
import Vars


class TerrainC:
    def __init__(self, screen, frog_pos):
        self.screen = screen
        self.terrain_types = self.initial_terrain()
        self.terrain_colors = [['grass', [92, 249, 87]], ['road', [42, 45, 61]], ['water', [50, 107, 209]]]
        self.frog_pos = frog_pos
        self.c_block_pos = 0
        self.last_terrain_index = 0

    def initial_terrain(self):
        # Start with two blocks of grass(type 0)
        result = [0, 0]
        """
        Terrain height: Frog width * 4

        Terrain types
            0: Grass
            1: Road
            2: Water
        """
        for c in range(5):
            # Append the initial terrain values
            result.append(random.randint(0, 2))

        return result

    def camera_movement(self, key_char):
        # Update c_block_pos on frog movement
        if key_char == 119:
            print("up")
            self.c_block_pos += Vars.frog_size
        elif key_char == 115:
            self.c_block_pos -= Vars.frog_size

        print(self.c_block_pos)

    def update_terrain(self):
        pass

    def draw_terrain(self):
        # Transfer this into a new function
        if self.c_block_pos == 80:
            self.c_block_pos = 0
            self.last_terrain_index += 1
        elif self.c_block_pos == -80:
            self.c_block_pos = 0
            self.last_terrain_index -= 1

        screen_place = Vars.screen_height
        for terrain in range(self.last_terrain_index, len(self.terrain_types)):
            color = self.terrain_colors[self.terrain_types[terrain]][1]
            # Draw terrain
            pygame.draw.rect(self.screen, color,
                             [0, screen_place, Vars.screen_width, Vars.frog_size * 4])
            screen_place -= 80