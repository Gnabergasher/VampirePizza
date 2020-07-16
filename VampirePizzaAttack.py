# Set up Game


import pygame
from pygame import *
from random import randint, choice
from time import sleep
import os
#  initialize pygame
pygame.init()

# Set up clock
clock = time.Clock()

# # -------------------------------------------------------
# # Define constant variables
#
# # Define the parameters of the game window
# WINDOW_WIDTH = 1100
# WINDOW_HEIGHT = 600
# WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)
#
# # Define tile parameters
# WIDTH = 100
# HEIGHT = WIDTH
#
# # Define Colors
# WHITE = (255, 255, 255)
# BROWN = (160, 82, 45)
#
# # Set up rates
# SPAWN_RATE = 360
# FRAME_RATE = 60
#
# # Set up Counters
# STARTING_BUCKS = 15
# BUCK_RATE = 120
# STARTING_BUCK_BOOSTER = 1
# STARTING_HEALTH = 100
#
#
# # Set up win / lose conditions
# MAX_BAD_REVIEWS = 3
# MINUTES = 3
# WIN_TIME = FRAME_RATE * 60 * MINUTES
#
# # Define Speeds
# FAST_SPEED = 3
# REG_SPEED = 2
# SLOW_SPEED = 1

# -------------------------------------------------------
# Load Assets
from variables import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_RES, WIDTH, HEIGHT,WHITE, BROWN, SPAWN_RATE, FRAME_RATE,\
    STARTING_BUCKS, BUCK_RATE, STARTING_BUCK_BOOSTER, STARTING_HEALTH, MAX_BAD_REVIEWS, MINUTES, WIN_TIME, FAST_SPEED,\
    REG_SPEED, SLOW_SPEED

# Create the game window
GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas!')

from load_assets import *
# Set up background image
#[, , , , , ]
BG = [CREEPY_RESTAURANT, GALAXY, RESTAURANT]
BACKGROUND = BG[randint(0,2)]

#Rename for book
VAMPIRE_PIZZA = VAMPIRE
MED_HEALTH = PIZZA60HEALTH
LOW_HEALTH = PIZZA30HEALTH
CUTTER = PIZZACUTTER
TABLE = PIZZA_TABLE
CANNON = ANCHOVY_CANNON



# -------------------------------------------------------
# Set up class objects

# Create an enemy object
class VampireSprite(sprite.Sprite):
    # Set up enemy instances
    def __init__(self):
        # Take all behavior rules from Sprite class & use
        # them for VampireSprite
        super().__init__()
        self.speed = REG_SPEED
        self.lane = randint(0, 4)
        all_vampires.add(self)
        self.image = VAMPIRE_PIZZA.copy()
        y = 50 + self.lane * 100
        self.rect = self.image.get_rect(center=(1100, y))
        self.health = STARTING_HEALTH

    # Set up enemy movement
    def update(self, game_window, counters):
        game_window.blit(BACKGROUND,
                         (self.rect.x, self.rect.y), self.rect)
        self.rect.x -= self.speed
        if self.health <= 0 or self.rect.x <= 100:
            self.kill()
            if self.rect.x <= 100:
                counters.bad_reviews += 1
        else:
            if self.health * 100 // STARTING_HEALTH > 60:
                self.image = VAMPIRE_PIZZA.copy()
            elif self.health * 100 // STARTING_HEALTH > 30:
                self.image = MED_HEALTH.copy()
            else:
                self.image = LOW_HEALTH.copy()
            game_window.blit(self.image, (self.rect.x, self.rect.y))

    # apply trap effects to enemies
    def attack(self, tile):
        if tile.trap == SLOW:
            self.speed = SLOW_SPEED
        if tile.trap == DAMAGE:
            self.health -= 1

class WerePizza(VampireSprite):

    def __init__(self):
        super(WerePizza, self).__init__()
        self.speed = FAST_SPEED
        self.image = WERE_PIZZA.copy()

    def attack(self, tile):
        if tile.trap == SLOW:
            self.speed = REG_SPEED
        if tile.trap == DAMAGE:
            self.health -= 1

    def update(self, game_window, counters):
        game_window.blit(BACKGROUND,
                         (self.rect.x, self.rect.y), self.rect)
        self.rect.x -= self.speed
        if self.health <= 0 or self.rect.x <= 100:
            self.kill()
            if self.rect.x <= 100:
                counters.bad_reviews += 1
        else:
            game_window.blit(self.image, (self.rect.x, self.rect.y))

class Counters:
    def __init__(self, pizza_bucks, buck_rate,
                 buck_booster, timer):
        self.loop_count = 0
        self.display_font = font.Font('pizza_font.ttf', 25)
        self.pizza_bucks = pizza_bucks
        self.buck_rate = buck_rate
        self.buck_booster = buck_booster
        self.bucks_rect = None
        self.timer = timer
        self.timer_rect = None
        self.bad_reviews = 0
        self.bad_rev_rect = None

    def increment_bucks(self):
        # Every BUCK_RATE ticks gives BUCK_BOOSTER pizza_bucks
        if self.loop_count % self.buck_rate == 0:
            self.pizza_bucks += self.buck_booster

    def draw_bucks(self, game_window):
        if self.bucks_rect:
            game_window.blit(BACKGROUND, (self.bucks_rect.x,
                                          self.bucks_rect.y), self.bucks_rect)
        bucks_surf = self.display_font.render(
            str(self.pizza_bucks), True, WHITE)
        self.bucks_rect = bucks_surf.get_rect()
        self.bucks_rect.x = WINDOW_WIDTH - 50
        self.bucks_rect.y = WINDOW_HEIGHT - 50
        game_window.blit(bucks_surf, self.bucks_rect)

    #Draw reviews on screen
    def draw_bad_reviews(self, game_window):
        # Test if there is a new number, if there is, erase old
        if self.bad_rev_rect:
            game_window.blit(BACKGROUND, (self.bad_rev_rect.x,
                                         self.bad_rev_rect.y), self.bad_rev_rect)
            # tell program font, content, and color
        bad_rev_surf = self.display_font.render(
                str(self.bad_reviews), True, WHITE)
            # set up rect to make number interactive
        self.bad_rev_rect = bad_rev_surf.get_rect()
            # put display in second to last column, bottom row (center points)
        self.bad_rev_rect.x = WINDOW_WIDTH - 150
        self.bad_rev_rect.y = WINDOW_HEIGHT - 50
            # display to game window
        game_window.blit(bad_rev_surf, self.bad_rev_rect)

    def draw_timer(self, game_window):
        # test for new time
        if self.timer_rect:
            # if so, erase old
            game_window.blit(BACKGROUND,(self.timer_rect.x,
                                         self.timer_rect.y), self.timer_rect)
            # select font content and color
        timer_surf = self.display_font.render(
                str((WIN_TIME - self.loop_count) // FRAME_RATE), True, WHITE)
            # set up rect to make number interactive
        self.timer_rect = timer_surf.get_rect()
        self.timer_rect.x = WINDOW_WIDTH - 250
        self.timer_rect.y = WINDOW_HEIGHT - 50
            # display to screen
        game_window.blit(timer_surf, self.timer_rect)

    def update(self, game_window):
        self.loop_count += 1
        self.increment_bucks()
        self.draw_bucks(game_window)
        self.draw_bad_reviews(game_window)
        self.draw_timer(game_window)


class Trap:
    def __init__(self, trap_kind, cost, trap_img):
        self.trap_kind = trap_kind
        self.cost = cost
        self.trap_img = trap_img

class TrapApplicator:
    def __init__(self):
        self.selected = None

    def select_trap(self, trap):
        if trap.cost <= counters.pizza_bucks:
            self.selected = trap

    def select_tile(self, tile, counters):
        self.selected = tile.set_trap(self.selected, counters)

class BackgroundTile(sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.trap = None
        self.rect = rect

class PlayTile(BackgroundTile):
    def set_trap(self, trap, counters):
        if trap and not self.trap:
            counters.pizza_bucks -= trap.cost
            self.trap = trap
            if trap == EARN:
                counters.buck_booster +=1
        return None

    def draw_trap(self, game_window, trap_applicator):
        if bool(self.trap):
            game_window.blit(self.trap.trap_img,
                             (self.rect.x, self.rect.y))

class ButtonTile(BackgroundTile):
    def set_trap(self, trap, counters):
        if counters.pizza_bucks >= self.trap.cost:
            return self.trap
        else:
            return None

    def draw_trap(self, game_window, trap_applicator):
        if trap_applicator.selected:
            if trap_applicator.selected == self.trap:
                draw.rect(game_window, (238, 190, 47),
                          (self.rect.x, self.rect.y, WIDTH, HEIGHT), 5)

class InactiveTile(BackgroundTile):
    def set_trap(self, trap, counters):
        return None

    def draw_trap(self, game_window, trap_applicator):
        pass

# -------------------------------------------------------
# Create class instances and groups
all_vampires = sprite.Group()

enemy_types = []
enemy_types.append(VampireSprite)
enemy_types.append(WerePizza)

# Create an instance of Counters
counters = Counters(STARTING_BUCKS, BUCK_RATE, STARTING_BUCK_BOOSTER, WIN_TIME)

SLOW = Trap('SLOW', 5, GARLIC)
DAMAGE = Trap('DAMAGE', 3, CUTTER)
EARN = Trap('EARN', 7, PEPPERONI)

trap_applicator = TrapApplicator()
# -------------------------------------------------------
# Initialize and draw the background grid
tile_grid = []
tile_color = WHITE
for row in range(6):
    row_of_tiles = []
    tile_grid.append(row_of_tiles)
    for column in range(11):
        tile_rect = Rect(WIDTH * column, HEIGHT * row,
                         WIDTH, HEIGHT)
        if column <= 1:
            new_tile = InactiveTile(tile_rect)
        else:
            if row == 5:
                if 2 <= column <= 4:
                    new_tile = ButtonTile(tile_rect)
                    new_tile.trap = [SLOW, DAMAGE, EARN][column - 2]
                else:
                    new_tile = InactiveTile(tile_rect)
            else:
                new_tile = PlayTile(tile_rect)
        row_of_tiles.append(new_tile)
        if row == 5 and 2 <= column <= 4:
            BACKGROUND.blit(new_tile.trap.trap_img,
                            (new_tile.rect.x, new_tile.rect.y))
        if column != 0 and row != 5:
            if column !=1:
                draw.rect(BACKGROUND, tile_color,
                    (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT), 1)


# Display the background image to the screen
GAME_WINDOW.blit(BACKGROUND, (0, 0))

# -------------------------------------------------------
# Game Loop

game_running = True
program_running = True
while game_running:
    # ---------------------------------------------------
    # Check for events

    # Start loop to check for and handle events
    for event in pygame.event.get():
        # exit loop on quit
        if event.type == QUIT:
            game_running = False
            program_running = False
        elif event.type == MOUSEBUTTONDOWN:
            coordinates = mouse.get_pos()
            x = coordinates[0]
            y = coordinates[1]
            tile_y = y // 100
            tile_x = x // 100
            trap_applicator.select_tile(
                tile_grid[tile_y][tile_x], counters)

    # ---------------------------------------------------
    # spawn sprites
    if randint(1, SPAWN_RATE) == 1:
        choice(enemy_types)()

    # draw background grid
    for tile_row in tile_grid:
        for tile in tile_row:
            if tile.trap:
                GAME_WINDOW.blit(BACKGROUND, (tile.rect.x, tile.rect.y), tile.rect)
    # ---------------------------------------------------
    # Set up collision detection
    for vampire in all_vampires:
        tile_row = tile_grid[vampire.rect.y // 100]
        vamp_left_side = vampire.rect.x // 100
        vamp_right_side = (vampire.rect.x +
                           vampire.rect.width) // 100
        if 0 <= vamp_left_side <= 10:
            left_tile = tile_row[vamp_left_side]
        else:
            left_tile = None
        if 0 <= vamp_right_side <= 10:
            right_tile = tile_row[vamp_right_side]
        else:
            right_tile = None
        if left_tile:
            vampire.attack(left_tile)
        if right_tile:
            if right_tile != left_tile:
                vampire.attack(right_tile)
    # ---------------------------------------------------
    # Set win / lose
    if (counters.bad_reviews >= MAX_BAD_REVIEWS) or (counters.loop_count >= WIN_TIME):
        game_running = False




    # update displays

    for vampire in all_vampires:
        vampire.update(GAME_WINDOW, counters)
    for tile_row in tile_grid:
        for tile in tile_row:
            tile.draw_trap(GAME_WINDOW, trap_applicator)

    # Update Counters
    counters.update(GAME_WINDOW)

    # Update all images on screen
    display.update()



    # Set the frame rate
    clock.tick(FRAME_RATE)

# End of main game loop
# -------------------------------------------------------
end_font = font.Font('pizza_font.ttf', 50)
if program_running:
    if counters.bad_reviews >= MAX_BAD_REVIEWS:
        end_surf = end_font.render(f'YOU LOSE HAHAHHAHAHAHA \n {counters.bad_reviews}  BAD REVIEWS \n YOU ARE DOOMED!!', True, WHITE)
    else:
        end_surf = end_font.render(f'YOU WIN, A TRUE PIZZA WARRIOR', True, WHITE)
    GAME_WINDOW.blit(end_surf, (350,200))
    display.update()
    sleep(2)



# Clean Up Game
pygame.quit()
