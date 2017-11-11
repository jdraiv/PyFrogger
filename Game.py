
import sys, pygame

# Classes
import Frog
import Terrain
import Vars


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode([Vars.screen_width, Vars.screen_height])
        self.frog_class = Frog.FrogC(self.screen)
        self.terrain_class = Terrain.TerrainC(self.screen)

    def game_loop(self):
        play = True

        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exit")
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.frog_class.frog_movement(event.key)

            self.screen.fill([0, 0, 0])
            self.terrain_class.set_terrain()
            self.frog_class.draw_frog()

            pygame.display.update()


game = Game()
game.game_loop()