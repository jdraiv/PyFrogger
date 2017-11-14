
import pygame
import random
import Vars


class TerrainC:
    def __init__(self, screen, frog_pos):
        self.screen = screen
        self.terrain_types = self.initial_terrain()
        self.terrain_colors = [['grass', [92, 249, 87]], ['road', [42, 45, 61]], ['water', [50, 107, 209]]]
        self.frog_pos = frog_pos
        self.last_terrain_index = 0
        self.terrain_c = 0

    def random_terrain(self):
        t_type = random.randint(0, 2)

        for _ in range(4):
            self.terrain_types.append(t_type)
            
    def initial_terrain(self):
        # Start with two four of grass(type 0)
        result = [0, 0, 0, 0]
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
                result.append(terrain_t)

        return result

    def camera_movement(self, key_char):
        if key_char == 119:
            self.last_terrain_index += 1
            self.terrain_c += 1
            # Insert a new terrain into the terrain list
            if self.terrain_c == 5:
                self.random_terrain()
                self.terrain_c = 0
        elif key_char == 115:
            if self.last_terrain_index > 0:
                self.last_terrain_index -= 1

    def remove_terrain(self):
        if self.last_terrain_index > 5:
            self.terrain_types = self.terrain_types[self.last_terrain_index:]
            self.last_terrain_index = 0

    def draw_terrain(self):
        # Remove old terrain
        self.remove_terrain()

        screen_place = Vars.screen_height - Vars.terrain_height * 4
        for terrain in range(self.last_terrain_index, len(self.terrain_types)):
            color = self.terrain_colors[self.terrain_types[terrain]][1]
            # Draw terrain
            pygame.draw.rect(self.screen, color,
                             [0, screen_place, Vars.screen_width, Vars.frog_size * 4])
            screen_place -= Vars.terrain_height
