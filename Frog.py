import pygame

import Vars


class FrogC:
    def __init__(self, screen):
        self.screen = screen
        # X
        self.frog_pos = [Vars.screen_width // 2, Vars.screen_height - Vars.frog_size * 4]

    def frog_movement(self, key_char):
        left_key, right_key = 97, 100

        if key_char == left_key:
            self.frog_pos[0] -= Vars.frog_size
        elif key_char == right_key:
            self.frog_pos[0] += Vars.frog_size

    def draw_frog(self):
        pygame.draw.rect(self.screen, [150, 150, 150], [self.frog_pos[0], self.frog_pos[1], Vars.frog_size,
                                                        Vars.frog_size])


# The list goes on forever of all the ways I could be better in my mind
