import pygame

import Vars


class FrogC:
    def __init__(self, screen):
        self.screen = screen
        # X, Y
        self.frog_pos = [Vars.screen_width // 2, Vars.screen_height - Vars.frog_size]

    def frog_movement(self, key_char):
        # list[0] == X Axis
        # list[1] == Y Axis
        pos_list = [100, 115]
        neg_list = [97, 119]

        # Left and up movement
        if key_char in pos_list:
            self.frog_pos[pos_list.index(key_char)] += Vars.frog_size
        # Right and down movement
        else:
            self.frog_pos[neg_list.index(key_char)] -= Vars.frog_size

    def draw_frog(self):
        pygame.draw.rect(self.screen, [150, 150, 150], [self.frog_pos[0], self.frog_pos[1], Vars.frog_size,
                                                        Vars.frog_size])


# The list goes on forever of all the ways I could be better in my mind
