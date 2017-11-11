
import pygame
import random
import Vars


class TerrainC:
    def __init__(self, screen):
        self.screen = screen
        self.terrain_types = self.initial_terrain()
        self.terrain_colors = [['grass', [92, 249, 87]], ['road', [42, 45, 61]], ['water', [50, 107, 209]]]

    def initial_terrain(self):
        result = [0, 0]
        """
        Terrain height: Frog width * 4

        Terrain types
            0: Grass
            1: Road
            2: Water
        """
        for c in range(10):
            result.append(random.randint(0, 2))

        return result

    def set_terrain(self):
        screen_place = Vars.screen_height
        for terrain in self.terrain_types:
            color = self.terrain_colors[terrain][1]
            pygame.draw.rect(self.screen, color,
                             [0, screen_place, Vars.screen_width, 80])
            screen_place -= 80
