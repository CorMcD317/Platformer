from typing import cast

import pygame

from Player import Player
from Portal import Portal
from Ruby import Ruby
from RubyMaker import RubyMaker
from Tile import Tile
from Zombie import Zombie


class Game:
    """A class to help manage gameplay"""

    # Set display surface (tile size is 32x32 so 1280/32 = 40 tiles wide, 736/32 = 23 tiles high)
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 736
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Zombie Knight")

    # Set FPS and clock
    FPS = 60
    clock = pygame.time.Clock()

    # Set colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (25, 200, 25)

    def __init__(self):
        """Initialize the game"""
        # Set constant variables
        self.running = True
        self.STARTING_ROUND_TIME = 30
        self.STARTING_ZOMBIE_CREATION_TIME = 5
        self.running = True
        self.STARTING_ROUND_TIME = 30
        self.STARTING_ZOMBIE_CREATION_TIME = 5
        # TODO: assign True to self.running
        # TODO: assign 30 to self.STARTING_ROUND_TIME
        # TODO: assign 5 to self.STARTING_ZOMBIE_CREATION_TIME

        # Set game values
        self.score = 0
        self.round_number = 1
        self.frame_count = 0
        self.zombie_creation_time = self.STARTING_ZOMBIE_CREATION_TIME
        self.score = 0
        self.round_number = 1
        self.frame_count = 0
        self.zombie_create_time = self.STARTING_ZOMBIE_CREATION_TIME
        # TODO: assign 0 to self.score
        # TODO: assign 1 to self.round_number
        # TODO: assign 0 to self.frame_count
        # TODO: assign self.STARTING_ZOMBIE_CREATION_TIME to self.zombie_create_time
        self.title_font = pygame.font.Font("./assets/fonts/Poultrygeist.ttf", 48)
        # TODO: assign pygame.font.Font() to self.title_font.  The arguments for Font() are the font file location which is here
        # "./assets/fonts/Poultrygeist.ttf" and the size which is 48
        self.HUD_font = pygame.font.Font("./assets/fonts/Pixel.ttf", 24)
        # TODO: assign pygame.font.Font() to self.HUD_font.  The arguments for Font() are the font file location which is here
        # "./assets/fonts/Pixel.ttf" and the size which is 24
        self.lost_ruby_sound = pygame.mixer.Sound("assets/sounds/lost_ruby.wav")
        # Set Sounds
        # TODO: assign pygame.mixer.Sound() to self.lost_ruby_sound.  The argument for Sound() is the sound file location which is here
        # "assets/sounds/lost_ruby.wav"
        self.ruby_pickup_sound = pygame.mixer.Sound("assets/sounds/ruby_pickup.wav")
        # TODO: assign pygame.mixer.Sound() to self.ruby_pickup_sound.  The argument for Sound() is the sound file location which is here
        # "assets/sounds/ruby_pickup.wav"
        pygame.mixer.music.load("assets/sounds/level_music.wav")
        # TODO: call pygame.mixer.music.load().  The argument for load() is the background music file location which is here
        # "assets/sounds/level_music.wav"

        # Create the tile map
        # 0 -> no tile, 1 -> dirt, 2-5 -> platforms, 6 -> ruby maker, 7-8 -> portals, 9 -> player
        # 23 rows and 40 columns
        self.tile_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 8, 0],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
             4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4,
             4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
             4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 7, 0],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
             2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1]
        ]

        # Create sprite groups
        self.main_tile_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.zombie_group = pygame.sprite.Group()
        self.portal_group = pygame.sprite.Group()
        self.ruby_group = pygame.sprite.Group()

        # TODO: assign pygame.sprite.Group() to the following self variables
        # main_tile_group, platform_group, player_group, bullet_group, zombie_group, portal_group, ruby_group

        # Generate Tile objects from the tile map
        # Loop through the 23 lists (rows) in the tile map (row moves us down the map)
        for row in range(len(self.tile_map)):
            # Loop through the 40 elements in a given list (cols) (col moves us across the map)
            for col in range(len(self.tile_map[row])):
                # Dirt tiles
                if self.tile_map[row][col] == 1:
                    Tile(col * 32, row * 32, 1, self.main_tile_group)
                    # TODO: call the Tile() constructor passing col * 32, row * 32, 1, self.main_tile_group
                # Platform tiles
                elif self.tile_map[row][col] == 2:
                    Tile(col * 32, row * 32, 2, self.main_tile_group, self.platform_group)
                    # TODO: call the Tile() constructor passing col * 32, row * 32, 2, self.main_tile_group, self.platform_group
                elif self.tile_map[row][col] == 3:
                    Tile(col * 32, row * 32, 3, self.main_tile_group, self.platform_group)
                    # TODO: call the Tile() constructor passing col * 32, row * 32, 3, self.main_tile_group, self.platform_group
                elif self.tile_map[row][col] == 4:
                    Tile(col * 32, row * 32, 4, self.main_tile_group, self.platform_group)
                    # TODO: call the Tile() constructor passing col * 32, row * 32, 4, self.main_tile_group, self.platform_group
                elif self.tile_map[row][col] == 5:
                    Tile(col * 32, row * 32, 5, self.main_tile_group, self.platform_group)
                    # TODO: call the Tile() constructor passing col * 32, row * 32, 5, self.main_tile_group, self.platform_group
                # Ruby Maker
                elif self.tile_map[row][col] == 6:
                    RubyMaker(col * 32, row * 32, self.main_tile_group, )
                    # TODO: call the RubyMaker() constructor passing in col * 32, row * 32, self.main_tile_group
                # Portals
                elif self.tile_map[row][col] == 7:
                    Portal(col * 32, row * 32, "green", self.portal_group)
                    # TODO: call the Portal() constructor passing in col * 32, row * 32, "green", and self.portal_group

                elif self.tile_map[row][col] == 8:
                    Portal(col * 32, row * 32, "purple", self.portal_group)
                    # TODO: call the Portal() constructor passing in col * 32, row * 32, "purple", and self.portal_group
                # Player
                elif self.tile_map[row][col] == 9:
                    self.my_player = Player(col * 32 - 32, row * 32 + 32, self.platform_group, self.portal_group,
                                            self.bullet_group, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
                    self.player_group.add(self.my_player)
                    # TODO: assign to self.my_player the Player() constructor passing col * 32 - 32, row * 32 + 32,
                    # self.platform_group, self.portal_group, self.bullet_group,
                    # self.WINDOW_WIDTH, self.WINDOW_HEIGHT
                    # TODO: call self.player_group's add function and pass in self.my_player

        # Load in a background image (we must resize)
        self.background_image = pygame.transform.scale(pygame.image.load("./assets/images/background.png"), (1280, 736))
        self.background_rect = self.background_image.get_rect()
        self.background_rect.topleft = (0, 0)
        # TODO: assign pygame.transform.scale(pygame.image.load("./assets/images/background.png"), (1280, 736))
        # to self.background_image
        # TODO: assign self.background_image.get_rect() to self.background_rect
        # TODO: assign (0, 0) to self.background_rect.topleft
        self.pause_game(("Zombee Knight", "Press 'Enter' to Begin"))
        pygame.mixer.music.play(-1, 0.0)

        self.game_loop()

        # TODO: call self.pause_game() passing in "Zombie Knight", "Press 'Enter' to Begin"
        # TODO: call pygame.mixer.music.play() passing in -1, and 0.0

        # TODO: call self.game_loop()

    def game_loop(self):
        # The main game loop
        running = True
        while running:
            # Check to see if the user wants to quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # Player wants to jump
                    if event.key == pygame.K_SPACE:
                        self.my_player.jump()
                    # Player wants to fire
                    if event.key == pygame.K_UP:
                        self.my_player.fire()

            # Blit the background
            Game.display_surface.blit(self.background_image, self.background_rect)
            # TODO: call Game.display_surface.blit() passing in self.background_image, self.background_rect

            # Draw tiles and update ruby maker
            self.main_tile_group.update()
            self.main_tile_group.draw(Game.display_surface)
            # TODO: call self.main_tile_group.update()
            # TODO: call self.main_tile_group.draw() passing in Game.display_surface

            # Update and draw sprite groups
            self.portal_group.update()
            self.portal_group.draw(Game.display_surface)
            # TODO: call self.portal_group.update()
            # TODO: call self.portal_group.draw() passing in Game.display_surface
            self.player_group.update()
            self.player_group.draw(Game.display_surface)
            # TODO: call self.player_group.update()
            # TODO: call self.player_group.draw() passing in Game.display_surface
            self.bullet_group.update()
            self.bullet_group.draw(Game.display_surface)
            # TODO: call self.bullet_group.update()
            # TODO: call self.bullet_group.draw() passing in Game.display_surface
            self.zombie_group.update()
            self.zombie_group.draw(Game.display_surface)
            # TODO: call self.zombie_group.update()
            # TODO: call self.zombie_group.draw() passing in Game.display_surface
            self.ruby_group.update()
            self.ruby_group.draw(Game.display_surface)
            # TODO: call self.ruby_group.update()
            # TODO: call self.ruby_group.draw() passing in Game.display_surface

            # Update and draw the game
            self.update()
            self.draw()
            # TODO: call self.update()
            # TODO: call self.draw()

            # Update the display and tick the clock
            pygame.display.update()
            Game.clock.tick(Game.FPS)
            # TODO: call pygame.display.update()
            # TODO: call Game.clock.tick() passing in Game.FPS

    def update(self):
        """Update the game"""
        # Update the round time every second
        self.frame_count += 1
        if self.frame_count % Game.FPS == 0:
            self.round_time -= 1
            self.frame_count = 0
        # TODO: add 1 to self.frame_count
        # TODO: if self.frame_count % Game.FPS is 0
        # TODO: (1) subtract 1 from self.round_time
        # TODO: (2) set self.frame_count to 0
        self.check_collisions()
        self.add_zombie()
        self.check_round_completion()
        self.game_over()
        # TODO: call self.check_collisions()
        # TODO: call self.add_zombie()
        # TODO: call self.check_round_completion()
        # TODO: call self.game_over()

    def draw(self):
        """Draw the game HUD"""
        # Set colors

        # Set text
        score_text = self.HUD_font.render("Score: " + str(self.score), True, Game.WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, Game.WINDOW_HEIGHT - 50)

        health_text = self.HUD_font.render("Health: " + str(self.my_player.health), True, Game.WHITE)
        health_rect = health_text.get_rect()
        health_rect.topleft = (10, Game.WINDOW_HEIGHT - 25)

        title_text = self.title_font.render("Zombie Knight", True, Game.GREEN)
        title_rect = title_text.get_rect()
        title_rect.center = (Game.WINDOW_WIDTH // 2, Game.WINDOW_HEIGHT - 25)

        round_text = self.HUD_font.render("Night: " + str(self.round_number), True, Game.WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (Game.WINDOW_WIDTH - 10, Game.WINDOW_HEIGHT - 50)

        time_text = self.HUD_font.render("Sunrise In: " + str(self.round_time), True, Game.WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (Game.WINDOW_WIDTH - 10, Game.WINDOW_HEIGHT - 25)

        # Draw the HUD
        Game.display_surface.blit(score_text, score_rect)
        Game.display_surface.blit(health_text, health_rect)
        Game.display_surface.blit(title_text, title_rect)
        Game.display_surface.blit(round_text, round_rect)
        Game.display_surface.blit(time_text, time_rect)

    def add_zombie(self):
        """Add a zombie to the game"""
        # Check to add a zombie every second
        if self.frame_count % Game.FPS == 0:
            if self.round_time % self.zombie_creation_time == 0:
                zombie = Zombie(
                    self.platform_group, self.portal_group, self.round_number,
                    5 + self.round_number, self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FPS
                )
                self.zombie_group.add(zombie)
        # TODO: if self.frame_count % Game.FPS is 0 then
        # TODO: (1) check if self.round_time % self.zombie_creation_time is 0
        # TODO: (1-1) assign to zombie the Zombie() constructor passing in self.platform_group, self.portal_group, self.round_number
        # 5 + self.round_number, self.WINDOW_WIDTH, self.WINDOW_HEIGHT, and self.FPS
        # TODO: (1-2): call self.zombie_group's add method and pass in zombie

    def check_collisions(self):
        """Check collisions that affect gameplay"""
        # See if any bullet in the bullet group hit a zombie in the zombie group
        collision_dict = pygame.sprite.groupcollide(self.bullet_group, self.zombie_group, True, False)
        if collision_dict:
            for zombies in collision_dict.values():
                for zombie in zombies:
                    zombie.hit_sound.play()
                    zombie.is_dead = True
                    zombie.animate_death = True

        # See if a player stomped a dead zombie to finish it or collided with a live zombie to take damage
        collision_list = pygame.sprite.spritecollide(self.my_player, self.zombie_group, False)
        if collision_list:
            for zombie in collision_list:
                # The zombie is dead; stomp it
                if zombie.is_dead:
                    zombie.kick_sound.play()
                    zombie.kill()
                    self.score += 25

                    ruby = Ruby(self.platform_group, self.portal_group, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
                    self.ruby_group.add(ruby)
                # The zombie isn't dead, so take damage
                else:
                    self.my_player.health -= 20
                    self.my_player.hit_sound.play()
                    # Move the player to not continually take damage
                    self.my_player.position.x -= 256 * zombie.direction
                    self.my_player.rect.bottomleft = self.my_player.position

        # See if a player collided with a ruby
        if pygame.sprite.spritecollide(self.my_player, self.ruby_group, True):
            self.ruby_pickup_sound.play()
            self.score += 100
            self.my_player.health += 10
            if self.my_player.health > self.my_player.STARTING_HEALTH:
                self.my_player.health = self.my_player.STARTING_HEALTH

        # See if a living zombie collided with a ruby
        for zombie in self.zombie_group:
            if not zombie.is_dead:
                if pygame.sprite.spritecollide(zombie, self.ruby_group, True):
                    self.lost_ruby_sound.play()
                    zombie = Zombie(self.platform_group, self.portal_group, self.round_number,
                                    5 + self.round_number, self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FPS)
                    self.zombie_group.add(zombie)

    def check_round_completion(self):
        """Check if the player survived a single night."""
        if self.round_time == 0:
            self.start_new_round()
        # TODO: if self.round_time is 0 then call self.start_new_round()

    def check_game_over(self):
        """Check to see if the player lost the game"""
        if self.my_player.health <= 0:
            pygame.mixer.music.stop()
            self.pause_game("Game Over! Final Score: " + str(self.score), "Press 'Enter' to play again...")
            self.reset_game()
        # TODO: if the self.my_player.health is less than or equal to 0 then do the following
        # (1): call pygame.mixer.music.stop()
        # (2): call self.pause_game() passing in "Game Over! Final Score: " + str(self.score), "Press 'Enter' to play again..."
        # (3): call self.reset_game()

    def start_new_round(self):
        """Start a new night"""
        self.round_number += 1
        # TODO: add 1 to self.round_number

        # Decrease zombie creation time...more zombies
        if self.round_number < self.STARTING_ZOMBIE_CREATION_TIME:
            self.zombie_creation_time -= 1
        # TODO: check if self.round_number is less than self.STARTING_ZOMBIE_CREATION_TIME.  subtract 1 from self.zombie_creation_time

        # Reset round values
        self.round_time = self.STARTING_ROUND_TIME
        # TODO: assign self.STARTING_ROUND_TIME to self.round_time

        # TODO: call empty() on the following self groups
        self.zombie_group.empty()
        self.ruby_group.empty()
        self.bullet_group.empty()
        # zombie_group, ruby_group, bullet_group

        # TODO: call self.my_player.reset()
        self.my_player.reset()

        # TODO: call self.pause_game() passing in "You survived the night!", "Press 'Enter' to continue..."
        self.pause_game("You survived the night!", "Press 'Enter' to continue...")

    def pause_game(self, main_text, sub_text):
        """Pause the game"""
        pygame.mixer.music.pause()

        # Create main pause text
        main_text_render = self.title_font.render(main_text, True, Game.GREEN)
        main_rect = main_text_render.get_rect()
        main_rect.center = (Game.WINDOW_WIDTH // 2, Game.WINDOW_HEIGHT // 2)

        # Create sub pause text
        sub_text_render = self.title_font.render(sub_text, True, Game.WHITE)
        sub_rect = sub_text_render.get_rect()
        sub_rect.center = (Game.WINDOW_WIDTH // 2, Game.WINDOW_HEIGHT // 2 + 64)

        # Display the pause text
        Game.display_surface.fill(Game.BLACK)
        Game.display_surface.blit(main_text_render, main_rect)
        Game.display_surface.blit(sub_text_render, sub_rect)
        pygame.display.update()

        # Pause the game until user hits enter or quits
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                        pygame.mixer.music.unpause()
                elif event.type == pygame.QUIT:
                    is_paused = False
                    self.running = False
                    pygame.mixer.music.stop()

    def reset_game(self):
        """Reset the game"""
        self.score = 0
        self.round_number = 1
        self.round_time = self.STARTING_ROUND_TIME
        self.zombie_creation_time = self.STARTING_ZOMBIE_CREATION_TIME
        # Reset game values
        # TODO: assign the following to these self variables
        # 0 to score, 1 to round_number, self.STARTING_ROUND_TIME to round_time
        # self.STARTING_ZOMBIE_CREATION_TIME to zombie_creation_time,

        # Reset the player
        self.my_player.health = self.my_player.STARTING_HEALTH
        self.my_player.reset()
        # TODO: assign self.my_player.STARTING_HEALTH to self.my_player.health
        # TODO: call self.my_player.reset()

        # Empty sprite groups
        self.zombie_group.empty()
        self.ruby_group.empty()
        self.bullet_group.empty()
        # TODO: call .empty() on the following sprite groups
        # zombie_group, ruby_group, bullet_group
        pygame.mixer.music.play(-1, 0.0)
        # TODO: call pygame.mixer.music.play() passing in -1, and 0.0
