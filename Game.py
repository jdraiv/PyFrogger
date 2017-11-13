
import sys, pygame

# Classes
import Frog
import Terrain
import Vars


# Hold on for a minute, cause I believe that we can fix this overtime.

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode([Vars.screen_width, Vars.screen_height])
        self.frog_class = Frog.FrogC(self.screen)
        self.terrain_class = Terrain.TerrainC(self.screen, self.frog_class.frog_pos)

    def game_loop(self):
        play = True

        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exit")
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.frog_class.frog_movement(event.key)
                    self.terrain_class.camera_movement(event.key)

            self.screen.fill([0, 0, 0])
            self.terrain_class.draw_terrain()
            self.frog_class.draw_frog()

            pygame.display.update()


game = Game()
game.game_loop()