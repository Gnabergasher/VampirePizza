import os
from pygame import Surface, image, transform
from variables import HEIGHT, WIDTH, WINDOW_RES
G = []

for filename in os.listdir():
    if filename.endswith(".jpg"):
        x = filename.split(".")
        x = x[0].replace('-', '_').lower()


# Lists of all included assets

image_list = ['alien', 'anchovy_cannon', 'anchovy', 'asterisk', 'asterisk2', 'ball', 'Banana', 'basil1', 'basil2',
              'bat1', 'bat2', 'bear', 'bike1', 'bike2', 'bunny', 'cake', 'car1', 'car2', 'car3', 'cat1', 'cat2', 'cat3',
              'cat4', 'cat5', 'cheese', 'circuit', 'clock', 'cthulu_pizza', 'dashboard', 'dog1', 'dog2', 'dog3',
              'dragon', 'explosion', 'file1', 'file2', 'garlic', 'gem1blue', 'gem1green', 'gem1Red', 'gem2blue',
              'gem2green', 'gem2Red', 'gem3blue', 'gem3green', 'gem3Red', 'gem4blue', 'gem4green', 'gem4Red', 'grace1',
              'grace2', 'happy_tool', 'hashtag', 'herb', 'laptop', 'lightbulb', 'lightningbolt', 'lion', 'lizard',
              'magnify', 'medgehog', 'meteor', 'monsterfood_frank', 'monsterfood_mummy', 'monsterfood_were', 'moth',
              'mozzarella', 'mushroom_happy', 'mushroom_scared', 'mushroom_tiny', 'oil_can', 'olive1', 'olive2', 'one',
              'orb1', 'orb2', 'orb3', 'orb4', 'orb5', 'orb6', 'pencil', 'pepper', 'pepperoni', 'pepperoni1',
              'pepperoni2', 'pepperoni3', 'pig1', 'pig2', 'pig3', 'pizza_box', 'pizza_scooter', 'pizza_table',
              'pizza30health', 'pizza60health', 'pizzacutter', 'pizza_slice', 'python1', 'python2', 'robot',
              'rubber_duck', 'sad_hammer', 'space_ship1', 'space_ship2', 'star1', 'stars', 'super_meg', 'sushi1',
              'sushi2', 'taco', 'thumbs_down', 'tiger', 'tomato_running', 'tomato_slice', 'tomato_yellow',
              'tomato_zonk', 'tomato', 'trashcan', 'troll', 'umbrella', 'unicorn', 'vampire',
              'video_game_cartridge', 'video_game_controller', 'video_game', 'were_pizza', 'wormhole',
              'zero', 'zombie_pizza']

background_list = ['cave_background', 'creepy_restaurant', 'galaxy', 'restaurant',
                   'road_background', 'space_grid', 'space_background']

# Images

alien_img = image.load('alien.png')
alien_surf = Surface.convert_alpha(alien_img)
ALIEN = transform.scale(alien_surf, (HEIGHT, WIDTH))

anchovy_cannon_img = image.load('anchovy-cannon.png')
anchovy_cannon_surf = Surface.convert_alpha(anchovy_cannon_img)
ANCHOVY_CANNON = transform.scale(anchovy_cannon_surf, (HEIGHT, WIDTH))

anchovy_img = image.load('anchovy.png')
anchovy_surf = Surface.convert_alpha(anchovy_img)
ANCHOVY = transform.scale(anchovy_surf, (HEIGHT//2, WIDTH//2))

asterisk_img = image.load('asterisk.png')
asterisk_surf = Surface.convert_alpha(asterisk_img)
ASTERISK = transform.scale(asterisk_surf, (HEIGHT, WIDTH))

asterisk2_img = image.load('asterisk2.png')
asterisk2_surf = Surface.convert_alpha(asterisk2_img)
ASTERISK2 = transform.scale(asterisk2_surf, (HEIGHT, WIDTH))

ball_img = image.load('ball.png')
ball_surf = Surface.convert_alpha(ball_img)
BALL = transform.scale(ball_surf, (HEIGHT, WIDTH))

Banana_img = image.load('Banana.png')
Banana_surf = Surface.convert_alpha(Banana_img)
BANANA = transform.scale(Banana_surf, (HEIGHT, WIDTH))

basil1_img = image.load('basil1.png')
basil1_surf = Surface.convert_alpha(basil1_img)
BASIL1 = transform.scale(basil1_surf, (HEIGHT, WIDTH))

basil2_img = image.load('basil2.png')
basil2_surf = Surface.convert_alpha(basil2_img)
BASIL2 = transform.scale(basil2_surf, (HEIGHT, WIDTH))

bat1_img = image.load('bat1.png')
bat1_surf = Surface.convert_alpha(bat1_img)
BAT1 = transform.scale(bat1_surf, (HEIGHT, WIDTH))

bat2_img = image.load('bat2.png')
bat2_surf = Surface.convert_alpha(bat2_img)
BAT2 = transform.scale(bat2_surf, (HEIGHT, WIDTH))

bear_img = image.load('bear.png')
bear_surf = Surface.convert_alpha(bear_img)
BEAR = transform.scale(bear_surf, (HEIGHT, WIDTH))

bike1_img = image.load('bike1.png')
bike1_surf = Surface.convert_alpha(bike1_img)
BIKE1 = transform.scale(bike1_surf, (HEIGHT, WIDTH))

bike2_img = image.load('bike2.png')
bike2_surf = Surface.convert_alpha(bike2_img)
BIKE2 = transform.scale(bike2_surf, (HEIGHT, WIDTH))

bunny_img = image.load('bunny.png')
bunny_surf = Surface.convert_alpha(bunny_img)
BUNNY = transform.scale(bunny_surf, (HEIGHT, WIDTH))

cake_img = image.load('cake.png')
cake_surf = Surface.convert_alpha(cake_img)
CAKE = transform.scale(cake_surf, (HEIGHT, WIDTH))

car1_img = image.load('car1.png')
car1_surf = Surface.convert_alpha(car1_img)
CAR1 = transform.scale(car1_surf, (HEIGHT, WIDTH))

car2_img = image.load('car2.png')
car2_surf = Surface.convert_alpha(car2_img)
CAR2 = transform.scale(car2_surf, (HEIGHT, WIDTH))

car3_img = image.load('car3.png')
car3_surf = Surface.convert_alpha(car3_img)
CAR3 = transform.scale(car3_surf, (HEIGHT, WIDTH))

cat1_img = image.load('cat1.png')
cat1_surf = Surface.convert_alpha(cat1_img)
CAT1 = transform.scale(cat1_surf, (HEIGHT, WIDTH))

cat2_img = image.load('cat2.png')
cat2_surf = Surface.convert_alpha(cat2_img)
CAT2 = transform.scale(cat2_surf, (HEIGHT, WIDTH))

cat3_img = image.load('cat3.png')
cat3_surf = Surface.convert_alpha(cat3_img)
CAT3 = transform.scale(cat3_surf, (HEIGHT, WIDTH))

cat4_img = image.load('cat4.png')
cat4_surf = Surface.convert_alpha(cat4_img)
CAT4 = transform.scale(cat4_surf, (HEIGHT, WIDTH))

cat5_img = image.load('cat5.png')
cat5_surf = Surface.convert_alpha(cat5_img)
CAT5 = transform.scale(cat5_surf, (HEIGHT, WIDTH))

cheese_img = image.load('cheese.png')
cheese_surf = Surface.convert_alpha(cheese_img)
CHEESE = transform.scale(cheese_surf, (HEIGHT, WIDTH))

circuit_img = image.load('circuit.png')
circuit_surf = Surface.convert_alpha(circuit_img)
CIRCUIT = transform.scale(circuit_surf, (HEIGHT, WIDTH))

clock_img = image.load('clock.png')
clock_surf = Surface.convert_alpha(clock_img)
CLOCK = transform.scale(clock_surf, (HEIGHT, WIDTH))

cthulu_pizza_img = image.load('cthulu-pizza.png')
cthulu_pizza_surf = Surface.convert_alpha(cthulu_pizza_img)
CTHULU_PIZZA = transform.scale(cthulu_pizza_surf, (HEIGHT, WIDTH))

dashboard_img = image.load('dashboard.png')
dashboard_surf = Surface.convert_alpha(dashboard_img)
DASHBOARD = transform.scale(dashboard_surf, (HEIGHT, WIDTH))

dog1_img = image.load('dog1.png')
dog1_surf = Surface.convert_alpha(dog1_img)
DOG1 = transform.scale(dog1_surf, (HEIGHT, WIDTH))

dog2_img = image.load('dog2.png')
dog2_surf = Surface.convert_alpha(dog2_img)
DOG2 = transform.scale(dog2_surf, (HEIGHT, WIDTH))

dog3_img = image.load('dog3.png')
dog3_surf = Surface.convert_alpha(dog3_img)
DOG3 = transform.scale(dog3_surf, (HEIGHT, WIDTH))

dragon_img = image.load('dragon.png')
dragon_surf = Surface.convert_alpha(dragon_img)
DRAGON = transform.scale(dragon_surf, (HEIGHT, WIDTH))

explosion_img = image.load('explosion.png')
explosion_surf = Surface.convert_alpha(explosion_img)
EXPLOSION = transform.scale(explosion_surf, (HEIGHT, WIDTH))

file1_img = image.load('file1.png')
file1_surf = Surface.convert_alpha(file1_img)
FILE1 = transform.scale(file1_surf, (HEIGHT, WIDTH))

file2_img = image.load('file2.png')
file2_surf = Surface.convert_alpha(file2_img)
FILE2 = transform.scale(file2_surf, (HEIGHT, WIDTH))

garlic_img = image.load('garlic.png')
garlic_surf = Surface.convert_alpha(garlic_img)
GARLIC = transform.scale(garlic_surf, (HEIGHT, WIDTH))

gem1blue_img = image.load('gem1blue.png')
gem1blue_surf = Surface.convert_alpha(gem1blue_img)
GEM1BLUE = transform.scale(gem1blue_surf, (HEIGHT, WIDTH))

gem1green_img = image.load('gem1green.png')
gem1green_surf = Surface.convert_alpha(gem1green_img)
GEM1GREEN = transform.scale(gem1green_surf, (HEIGHT, WIDTH))

gem1Red_img = image.load('gem1Red.png')
gem1Red_surf = Surface.convert_alpha(gem1Red_img)
GEM1RED = transform.scale(gem1Red_surf, (HEIGHT, WIDTH))

gem2blue_img = image.load('gem2blue.png')
gem2blue_surf = Surface.convert_alpha(gem2blue_img)
GEM2BLUE = transform.scale(gem2blue_surf, (HEIGHT, WIDTH))

gem2green_img = image.load('gem2green.png')
gem2green_surf = Surface.convert_alpha(gem2green_img)
GEM2GREEN = transform.scale(gem2green_surf, (HEIGHT, WIDTH))

gem2Red_img = image.load('gem2Red.png')
gem2Red_surf = Surface.convert_alpha(gem2Red_img)
GEM2RED = transform.scale(gem2Red_surf, (HEIGHT, WIDTH))

gem3blue_img = image.load('gem3blue.png')
gem3blue_surf = Surface.convert_alpha(gem3blue_img)
GEM3BLUE = transform.scale(gem3blue_surf, (HEIGHT, WIDTH))

gem3green_img = image.load('gem3green.png')
gem3green_surf = Surface.convert_alpha(gem3green_img)
GEM3GREEN = transform.scale(gem3green_surf, (HEIGHT, WIDTH))

gem3Red_img = image.load('gem3Red.png')
gem3Red_surf = Surface.convert_alpha(gem3Red_img)
GEM3RED = transform.scale(gem3Red_surf, (HEIGHT, WIDTH))

gem4blue_img = image.load('gem4blue.png')
gem4blue_surf = Surface.convert_alpha(gem4blue_img)
GEM4BLUE = transform.scale(gem4blue_surf, (HEIGHT, WIDTH))

gem4green_img = image.load('gem4green.png')
gem4green_surf = Surface.convert_alpha(gem4green_img)
GEM4GREEN = transform.scale(gem4green_surf, (HEIGHT, WIDTH))

gem4Red_img = image.load('gem4Red.png')
gem4Red_surf = Surface.convert_alpha(gem4Red_img)
GEM4RED = transform.scale(gem4Red_surf, (HEIGHT, WIDTH))

grace1_img = image.load('grace1.png')
grace1_surf = Surface.convert_alpha(grace1_img)
GRACE1 = transform.scale(grace1_surf, (HEIGHT, WIDTH))

grace2_img = image.load('grace2.png')
grace2_surf = Surface.convert_alpha(grace2_img)
GRACE2 = transform.scale(grace2_surf, (HEIGHT, WIDTH))

happy_tool_img = image.load('happy-tool.png')
happy_tool_surf = Surface.convert_alpha(happy_tool_img)
HAPPY_TOOL = transform.scale(happy_tool_surf, (HEIGHT, WIDTH))

hashtag_img = image.load('hashtag.png')
hashtag_surf = Surface.convert_alpha(hashtag_img)
HASHTAG = transform.scale(hashtag_surf, (HEIGHT, WIDTH))

herb_img = image.load('herb.png')
herb_surf = Surface.convert_alpha(herb_img)
HERB = transform.scale(herb_surf, (HEIGHT, WIDTH))

laptop_img = image.load('laptop.png')
laptop_surf = Surface.convert_alpha(laptop_img)
LAPTOP = transform.scale(laptop_surf, (HEIGHT, WIDTH))

lightbulb_img = image.load('lightbulb.png')
lightbulb_surf = Surface.convert_alpha(lightbulb_img)
LIGHTBULB = transform.scale(lightbulb_surf, (HEIGHT, WIDTH))

lightningbolt_img = image.load('lightningbolt.png')
lightningbolt_surf = Surface.convert_alpha(lightningbolt_img)
LIGHTNINGBOLT = transform.scale(lightningbolt_surf, (HEIGHT, WIDTH))

lion_img = image.load('lion.png')
lion_surf = Surface.convert_alpha(lion_img)
LION = transform.scale(lion_surf, (HEIGHT, WIDTH))

lizard_img = image.load('lizard.png')
lizard_surf = Surface.convert_alpha(lizard_img)
LIZARD = transform.scale(lizard_surf, (HEIGHT, WIDTH))

magnify_img = image.load('magnify.png')
magnify_surf = Surface.convert_alpha(magnify_img)
MAGNIFY = transform.scale(magnify_surf, (HEIGHT, WIDTH))

medgehog_img = image.load('medgehog.png')
medgehog_surf = Surface.convert_alpha(medgehog_img)
MEDGEHOG = transform.scale(medgehog_surf, (HEIGHT, WIDTH))

meteor_img = image.load('meteor.png')
meteor_surf = Surface.convert_alpha(meteor_img)
METEOR = transform.scale(meteor_surf, (HEIGHT, WIDTH))

monsterfood_frank_img = image.load('monsterfood-frank.png')
monsterfood_frank_surf = Surface.convert_alpha(monsterfood_frank_img)
MONSTERFOOD_FRANK = transform.scale(monsterfood_frank_surf, (HEIGHT, WIDTH))

monsterfood_mummy_img = image.load('monsterfood-mummy.png')
monsterfood_mummy_surf = Surface.convert_alpha(monsterfood_mummy_img)
MONSTERFOOD_MUMMY = transform.scale(monsterfood_mummy_surf, (HEIGHT, WIDTH))

monsterfood_were_img = image.load('monsterfood-were.png')
monsterfood_were_surf = Surface.convert_alpha(monsterfood_were_img)
MONSTERFOOD_WERE = transform.scale(monsterfood_were_surf, (HEIGHT, WIDTH))

moth_img = image.load('moth.png')
moth_surf = Surface.convert_alpha(moth_img)
MOTH = transform.scale(moth_surf, (HEIGHT, WIDTH))

mozzarella_img = image.load('mozzarella.png')
mozzarella_surf = Surface.convert_alpha(mozzarella_img)
MOZZARELLA = transform.scale(mozzarella_surf, (HEIGHT, WIDTH))

mushroom_happy_img = image.load('mushroom-happy.png')
mushroom_happy_surf = Surface.convert_alpha(mushroom_happy_img)
MUSHROOM_HAPPY = transform.scale(mushroom_happy_surf, (HEIGHT, WIDTH))

mushroom_scared_img = image.load('mushroom-scared.png')
mushroom_scared_surf = Surface.convert_alpha(mushroom_scared_img)
MUSHROOM_SCARED = transform.scale(mushroom_scared_surf, (HEIGHT, WIDTH))

mushroom_tiny_img = image.load('mushroom-tiny.png')
mushroom_tiny_surf = Surface.convert_alpha(mushroom_tiny_img)
MUSHROOM_TINY = transform.scale(mushroom_tiny_surf, (HEIGHT, WIDTH))

oil_can_img = image.load('oil-can.png')
oil_can_surf = Surface.convert_alpha(oil_can_img)
OIL_CAN = transform.scale(oil_can_surf, (HEIGHT, WIDTH))

olive1_img = image.load('olive1.png')
olive1_surf = Surface.convert_alpha(olive1_img)
OLIVE1 = transform.scale(olive1_surf, (HEIGHT, WIDTH))

olive2_img = image.load('olive2.png')
olive2_surf = Surface.convert_alpha(olive2_img)
OLIVE2 = transform.scale(olive2_surf, (HEIGHT, WIDTH))

one_img = image.load('one.png')
one_surf = Surface.convert_alpha(one_img)
ONE = transform.scale(one_surf, (HEIGHT, WIDTH))

orb1_img = image.load('orb1.png')
orb1_surf = Surface.convert_alpha(orb1_img)
ORB1 = transform.scale(orb1_surf, (HEIGHT, WIDTH))

orb2_img = image.load('orb2.png')
orb2_surf = Surface.convert_alpha(orb2_img)
ORB2 = transform.scale(orb2_surf, (HEIGHT, WIDTH))

orb3_img = image.load('orb3.png')
orb3_surf = Surface.convert_alpha(orb3_img)
ORB3 = transform.scale(orb3_surf, (HEIGHT, WIDTH))

orb4_img = image.load('orb4.png')
orb4_surf = Surface.convert_alpha(orb4_img)
ORB4 = transform.scale(orb4_surf, (HEIGHT, WIDTH))

orb5_img = image.load('orb5.png')
orb5_surf = Surface.convert_alpha(orb5_img)
ORB5 = transform.scale(orb5_surf, (HEIGHT, WIDTH))

orb6_img = image.load('orb6.png')
orb6_surf = Surface.convert_alpha(orb6_img)
ORB6 = transform.scale(orb6_surf, (HEIGHT, WIDTH))

pencil_img = image.load('pencil.png')
pencil_surf = Surface.convert_alpha(pencil_img)
PENCIL = transform.scale(pencil_surf, (HEIGHT, WIDTH))

pepper_img = image.load('pepper.png')
pepper_surf = Surface.convert_alpha(pepper_img)
PEPPER = transform.scale(pepper_surf, (HEIGHT, WIDTH))

pepperoni_img = image.load('pepperoni.png')
pepperoni_surf = Surface.convert_alpha(pepperoni_img)
PEPPERONI = transform.scale(pepperoni_surf, (HEIGHT, WIDTH))

pepperoni1_img = image.load('pepperoni1.png')
pepperoni1_surf = Surface.convert_alpha(pepperoni1_img)
PEPPERONI1 = transform.scale(pepperoni1_surf, (HEIGHT, WIDTH))

pepperoni2_img = image.load('pepperoni2.png')
pepperoni2_surf = Surface.convert_alpha(pepperoni2_img)
PEPPERONI2 = transform.scale(pepperoni2_surf, (HEIGHT, WIDTH))

pepperoni3_img = image.load('pepperoni3.png')
pepperoni3_surf = Surface.convert_alpha(pepperoni3_img)
PEPPERONI3 = transform.scale(pepperoni3_surf, (HEIGHT, WIDTH))

pig1_img = image.load('pig1.png')
pig1_surf = Surface.convert_alpha(pig1_img)
PIG1 = transform.scale(pig1_surf, (HEIGHT, WIDTH))

pig2_img = image.load('pig2.png')
pig2_surf = Surface.convert_alpha(pig2_img)
PIG2 = transform.scale(pig2_surf, (HEIGHT, WIDTH))

pig3_img = image.load('pig3.png')
pig3_surf = Surface.convert_alpha(pig3_img)
PIG3 = transform.scale(pig3_surf, (HEIGHT, WIDTH))

pizza_box_img = image.load('pizza-box.png')
pizza_box_surf = Surface.convert_alpha(pizza_box_img)
PIZZA_BOX = transform.scale(pizza_box_surf, (HEIGHT, WIDTH))

pizza_scooter_img = image.load('pizza-scooter.png')
pizza_scooter_surf = Surface.convert_alpha(pizza_scooter_img)
PIZZA_SCOOTER = transform.scale(pizza_scooter_surf, (HEIGHT, WIDTH))

pizza_table_img = image.load('pizza-table.png')
pizza_table_surf = Surface.convert_alpha(pizza_table_img)
PIZZA_TABLE = transform.scale(pizza_table_surf, (HEIGHT, WIDTH))

pizza30health_img = image.load('pizza30health.png')
pizza30health_surf = Surface.convert_alpha(pizza30health_img)
PIZZA30HEALTH = transform.scale(pizza30health_surf, (HEIGHT, WIDTH))

pizza60health_img = image.load('pizza60health.png')
pizza60health_surf = Surface.convert_alpha(pizza60health_img)
PIZZA60HEALTH = transform.scale(pizza60health_surf, (HEIGHT, WIDTH))

pizzacutter_img = image.load('pizzacutter.png')
pizzacutter_surf = Surface.convert_alpha(pizzacutter_img)
PIZZACUTTER = transform.scale(pizzacutter_surf, (HEIGHT, WIDTH))

pizza_slice_img = image.load('pizza_slice.png')
pizza_slice_surf = Surface.convert_alpha(pizza_slice_img)
PIZZA_SLICE = transform.scale(pizza_slice_surf, (HEIGHT, WIDTH))

python1_img = image.load('python1.png')
python1_surf = Surface.convert_alpha(python1_img)
PYTHON1 = transform.scale(python1_surf, (HEIGHT, WIDTH))

python2_img = image.load('python2.png')
python2_surf = Surface.convert_alpha(python2_img)
PYTHON2 = transform.scale(python2_surf, (HEIGHT, WIDTH))

robot_img = image.load('robot.png')
robot_surf = Surface.convert_alpha(robot_img)
ROBOT = transform.scale(robot_surf, (HEIGHT, WIDTH))

rubber_duck_img = image.load('rubber-duck.png')
rubber_duck_surf = Surface.convert_alpha(rubber_duck_img)
RUBBER_DUCK = transform.scale(rubber_duck_surf, (HEIGHT, WIDTH))

sad_hammer_img = image.load('sad-hammer.png')
sad_hammer_surf = Surface.convert_alpha(sad_hammer_img)
SAD_HAMMER = transform.scale(sad_hammer_surf, (HEIGHT, WIDTH))

space_ship1_img = image.load('space-ship1.png')
space_ship1_surf = Surface.convert_alpha(space_ship1_img)
SPACE_SHIP1 = transform.scale(space_ship1_surf, (HEIGHT, WIDTH))

space_ship2_img = image.load('space-ship2.png')
space_ship2_surf = Surface.convert_alpha(space_ship2_img)
SPACE_SHIP2 = transform.scale(space_ship2_surf, (HEIGHT, WIDTH))

star1_img = image.load('star1.png')
star1_surf = Surface.convert_alpha(star1_img)
STAR1 = transform.scale(star1_surf, (HEIGHT, WIDTH))

stars_img = image.load('stars.png')
stars_surf = Surface.convert_alpha(stars_img)
STARS = transform.scale(stars_surf, (HEIGHT, WIDTH))

super_meg_img = image.load('super-meg.png')
super_meg_surf = Surface.convert_alpha(super_meg_img)
SUPER_MEG = transform.scale(super_meg_surf, (HEIGHT, WIDTH))

sushi1_img = image.load('sushi1.png')
sushi1_surf = Surface.convert_alpha(sushi1_img)
SUSHI1 = transform.scale(sushi1_surf, (HEIGHT, WIDTH))

sushi2_img = image.load('sushi2.png')
sushi2_surf = Surface.convert_alpha(sushi2_img)
SUSHI2 = transform.scale(sushi2_surf, (HEIGHT, WIDTH))

taco_img = image.load('taco.png')
taco_surf = Surface.convert_alpha(taco_img)
TACO = transform.scale(taco_surf, (HEIGHT, WIDTH))

thumbs_down_img = image.load('thumbs-down.png')
thumbs_down_surf = Surface.convert_alpha(thumbs_down_img)
THUMBS_DOWN = transform.scale(thumbs_down_surf, (HEIGHT, WIDTH))

tiger_img = image.load('tiger.png')
tiger_surf = Surface.convert_alpha(tiger_img)
TIGER = transform.scale(tiger_surf, (HEIGHT, WIDTH))

tomato_running_img = image.load('tomato-running.png')
tomato_running_surf = Surface.convert_alpha(tomato_running_img)
TOMATO_RUNNING = transform.scale(tomato_running_surf, (HEIGHT, WIDTH))

tomato_slice_img = image.load('tomato-slice.png')
tomato_slice_surf = Surface.convert_alpha(tomato_slice_img)
TOMATO_SLICE = transform.scale(tomato_slice_surf, (HEIGHT, WIDTH))

tomato_yellow_img = image.load('tomato-yellow.png')
tomato_yellow_surf = Surface.convert_alpha(tomato_yellow_img)
TOMATO_YELLOW = transform.scale(tomato_yellow_surf, (HEIGHT, WIDTH))

tomato_zonk_img = image.load('tomato-zonk.png')
tomato_zonk_surf = Surface.convert_alpha(tomato_zonk_img)
TOMATO_ZONK = transform.scale(tomato_zonk_surf, (HEIGHT, WIDTH))

tomato_img = image.load('tomato.png')
tomato_surf = Surface.convert_alpha(tomato_img)
TOMATO = transform.scale(tomato_surf, (HEIGHT, WIDTH))

trashcan_img = image.load('trashcan.png')
trashcan_surf = Surface.convert_alpha(trashcan_img)
TRASHCAN = transform.scale(trashcan_surf, (HEIGHT, WIDTH))

troll_img = image.load('troll.png')
troll_surf = Surface.convert_alpha(troll_img)
TROLL = transform.scale(troll_surf, (HEIGHT, WIDTH))

umbrella_img = image.load('umbrella.png')
umbrella_surf = Surface.convert_alpha(umbrella_img)
UMBRELLA = transform.scale(umbrella_surf, (HEIGHT, WIDTH))

unicorn_img = image.load('unicorn.png')
unicorn_surf = Surface.convert_alpha(unicorn_img)
UNICORN = transform.scale(unicorn_surf, (HEIGHT, WIDTH))

vampire_img = image.load('vampire.png')
vampire_surf = Surface.convert_alpha(vampire_img)
VAMPIRE = transform.scale(vampire_surf, (HEIGHT, WIDTH))

video_game_cartridge_img = image.load('video-game-cartridge.png')
video_game_cartridge_surf = Surface.convert_alpha(video_game_cartridge_img)
VIDEO_GAME_CARTRIDGE = transform.scale(video_game_cartridge_surf, (HEIGHT, WIDTH))

video_game_controller_img = image.load('video-game-controller.png')
video_game_controller_surf = Surface.convert_alpha(video_game_controller_img)
VIDEO_GAME_CONTROLLER = transform.scale(video_game_controller_surf, (HEIGHT, WIDTH))

video_game_img = image.load('video-game.png')
video_game_surf = Surface.convert_alpha(video_game_img)
VIDEO_GAME = transform.scale(video_game_surf, (HEIGHT, WIDTH))

were_pizza_img = image.load('were_pizza.png')
were_pizza_surf = Surface.convert_alpha(were_pizza_img)
WERE_PIZZA = transform.scale(were_pizza_surf, (HEIGHT, WIDTH))

wormhole_img = image.load('wormhole.png')
wormhole_surf = Surface.convert_alpha(wormhole_img)
WORMHOLE = transform.scale(wormhole_surf, (HEIGHT, WIDTH))

zero_img = image.load('zero.png')
zero_surf = Surface.convert_alpha(zero_img)
ZERO = transform.scale(zero_surf, (HEIGHT, WIDTH))

zombie_pizza_img = image.load('zombie_pizza.png')
zombie_pizza_surf = Surface.convert_alpha(zombie_pizza_img)
ZOMBIE_PIZZA = transform.scale(zombie_pizza_surf, (HEIGHT, WIDTH))


# Backgrounds

cave_background_img = image.load('cave_background.jpg')
cave_background_surf = Surface.convert_alpha(cave_background_img)
CAVE_BACKGROUND = transform.scale(cave_background_surf, WINDOW_RES)

creepy_restaurant_img = image.load('creepy-restaurant.jpg')
creepy_restaurant_surf = Surface.convert_alpha(creepy_restaurant_img)
CREEPY_RESTAURANT = transform.scale(creepy_restaurant_surf, WINDOW_RES)

galaxy_img = image.load('galaxy.jpg')
galaxy_surf = Surface.convert_alpha(galaxy_img)
GALAXY = transform.scale(galaxy_surf, WINDOW_RES)

restaurant_img = image.load('restaurant.jpg')
restaurant_surf = Surface.convert_alpha(restaurant_img)
RESTAURANT = transform.scale(restaurant_surf, WINDOW_RES)

road_background_img = image.load('road_background.jpg')
road_background_surf = Surface.convert_alpha(road_background_img)
ROAD_BACKGROUND = transform.scale(road_background_surf, WINDOW_RES)

space_grid_img = image.load('space-grid.jpg')
space_grid_surf = Surface.convert_alpha(space_grid_img)
SPACE_GRID = transform.scale(space_grid_surf, WINDOW_RES)

space_background_img = image.load('space_background.jpg')
space_background_surf = Surface.convert_alpha(space_background_img)
SPACE_BACKGROUND = transform.scale(space_background_surf, WINDOW_RES)


IMAGE_LIST = [ALIEN, ANCHOVY_CANNON, ANCHOVY, ASTERISK, ASTERISK2, BALL, BANANA, BASIL1, BASIL2,
              BAT1, BAT2, BEAR, BIKE1, BIKE2, BUNNY, CAKE, CAR1, CAR2, CAR3, CAT1, CAT2, CAT3,
              CAT4, CAT5, CHEESE, CIRCUIT, CLOCK, CTHULU_PIZZA, DASHBOARD, DOG1, DOG2, DOG3,
              DRAGON, EXPLOSION, FILE1, FILE2, GARLIC, GEM1BLUE, GEM1GREEN, GEM1RED, GEM2BLUE,
              GEM2GREEN, GEM2RED, GEM3BLUE, GEM3GREEN, GEM3RED, GEM4BLUE, GEM4GREEN, GEM4RED, GRACE1,
              GRACE2, HAPPY_TOOL, HASHTAG, HERB, LAPTOP, LIGHTBULB, LIGHTNINGBOLT, LION, LIZARD,
              MAGNIFY, MEDGEHOG, METEOR, MONSTERFOOD_FRANK, MONSTERFOOD_MUMMY, MONSTERFOOD_WERE, MOTH,
              MOZZARELLA, MUSHROOM_HAPPY, MUSHROOM_SCARED, MUSHROOM_TINY, OIL_CAN, OLIVE1, OLIVE2, ONE,
              ORB1, ORB2, ORB3, ORB4, ORB5, ORB6, PENCIL, PEPPER, PEPPERONI, PEPPERONI1,
              PEPPERONI2, PEPPERONI3, PIG1, PIG2, PIG3, PIZZA_BOX, PIZZA_SCOOTER, PIZZA_TABLE,
              PIZZA30HEALTH, PIZZA60HEALTH, PIZZACUTTER, PIZZA_SLICE, PYTHON1, PYTHON2, ROBOT,
              RUBBER_DUCK, SAD_HAMMER, SPACE_SHIP1, SPACE_SHIP2, STAR1, STARS, SUPER_MEG, SUSHI1,
              SUSHI2, TACO, THUMBS_DOWN, TIGER, TOMATO_RUNNING, TOMATO_SLICE, TOMATO_YELLOW,
              TOMATO_ZONK, TOMATO, TRASHCAN, TROLL, UMBRELLA, UNICORN, VAMPIRE, VIDEO_GAME_CARTRIDGE,
              VIDEO_GAME_CONTROLLER, VIDEO_GAME, WERE_PIZZA, WORMHOLE, ZERO, ZOMBIE_PIZZA]

BACKGROUND_LIST = [CAVE_BACKGROUND, CREEPY_RESTAURANT, GALAXY, RESTAURANT,
                    ROAD_BACKGROUND, SPACE_GRID, SPACE_BACKGROUND]