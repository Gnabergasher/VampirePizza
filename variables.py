# -------------------------------------------------------
# Define constant variables

# Define the parameters of the game window
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Define tile parameters
WIDTH = 100
HEIGHT = WIDTH

# Define Colors
WHITE = (255, 255, 255)
BROWN = (160, 82, 45)

# Set up rates
SPAWN_RATE = 60
FRAME_RATE = 60

# Set up Counters
STARTING_BUCKS = 15
BUCK_RATE = 120
STARTING_BUCK_BOOSTER = 1
STARTING_HEALTH = 100


# Set up win / lose conditions
MAX_BAD_REVIEWS = 3
MINUTES = 3
WIN_TIME = FRAME_RATE * 60 * MINUTES

# Define Speeds
FAST_SPEED = 3
REG_SPEED = 2
SLOW_SPEED = 1


list_of_variables = [WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_RES,
                     WIDTH, HEIGHT,
                     WHITE, BROWN,
                     SPAWN_RATE, FRAME_RATE,
                     STARTING_BUCKS, BUCK_RATE, STARTING_BUCK_BOOSTER, STARTING_HEALTH,
                     MAX_BAD_REVIEWS, MINUTES, WIN_TIME,
                     FAST_SPEED, REG_SPEED, SLOW_SPEED]