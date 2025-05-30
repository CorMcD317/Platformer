import pygame


class RubyMaker(pygame.sprite.Sprite):
    """A tile that is animated.  A ruby will be generated here."""

    def __init__(self, x, y, main_group):
        """Initialize the ruby maker"""
        super().__init__()

        #Animation frames
        self.ruby_sprites = []
        #TODO: create a self.ruby_sprites variables and assign an empty list to it.  HINT:  []

        #Rotating
        self.ruby_sprites.append(
            pygame.transform.scale(pygame.image.load("./assets/images/ruby/tile000.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("./assets/images/ruby/tile001.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("./assets/images/ruby/tile002.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("./assets/images/ruby/tile003.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("./assets/images/ruby/tile004.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("./assets/images/ruby/tile005.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("./assets/images/ruby/tile006.png"), (64, 64)))
        #TODO: so we've just added an image to our list of ruby_sprites.  repeate the previous line form tile's 001 to 006

        #Load image and get rect
        self.current_sprite = 0
        self.image = self.ruby_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        #TODO: assign 0 to self.current_sprite.  HINT:  When I say assign y to x I mean x = y
        #TODO: assign self.ruby_sprites[self.current_sprite] to self.image
        #TODO: assign self.image.get_rect() to self.image
        #TODO: assign (x, y) to self.rect.bottomleft

        #Add to the main group for drawing purposes
        def main_group(add):
            pass
        #TODO: call main_group's add() method passing self

    def update(self):
        """Update the ruby maker"""
        self.animate(self.ruby_sprites, 0.25)
        #TODO: call self.animate() passing in self.ruby_sprites and 0.25 into the function

    def animate(self, sprite_list, speed):
        """Animate the ruby maker"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]

