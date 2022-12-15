from time import sleep, perf_counter
import keyboard
from tkinter import *

### Constants ###
MAP = [
    {
        "row": 0,
        "default_tile": "a",
        "tile_exceptions": {}
    },
    {
        "row": 1,
        "default_tile": "a",
        "tile_exceptions": {
            198: "fp"
        }
    },
    {
        "row": 2,
        "default_tile": "a",
        "tile_exceptions": {
            198: "fp"
        }
    },
    {
        "row": 3,
        "default_tile": "a",
        "tile_exceptions": {
            198: "fp"
        }
    },
    {
        "row": 4,
        "default_tile": "a",
        "tile_exceptions": {
            22: "q",
            80: "br",
            81: "br",
            82: "br",
            83: "br",
            84: "br",
            85: "br",
            86: "br",
            87: "br",
            91: "br",
            92: "br",
            93: "br",
            94: "q",
            109: "q",
            121: "br",
            122: "br",
            123: "br",
            128: "br",
            129: "q",
            130: "q",
            131: "br",
            188: "h",
            189: "h",
            198: "fp"
        }
    },
    {
        "row": 5,
        "default_tile": "a",
        "tile_exceptions": {
            187: "h",
            188: "h",
            189: "h",
            198: "fp"
        }
    },
    {
        "row": 6,
        "default_tile": "a",
        "tile_exceptions": {
            186: "h",
            187: "h",
            188: "h",
            189: "h",
            198: "fp"
        }
    },
    {
        "row": 7,
        "default_tile": "a",
        "tile_exceptions": {
            185: "h",
            186: "h",
            187: "h",
            188: "h",
            189: "h",
            198: "fp",
            203: "p",
            204: "p",
            205: "p",
        }
    },
    {
        "row": 8,
        "default_tile": "a",
        "tile_exceptions": {
            16: "q",
            20: "br",
            21: "q",
            22: "br",
            23: "q",
            24: "br",
            46: "pcl",
            47: "pcr",
            57: "pcl",
            58: "pcr",
            77: "br",
            78: "q",
            79: "br",
            94: "br",
            100: "br",
            106: "q",
            109: "q",
            112: "q",
            118: "br",
            129: "br",
            130: "br",
            137: "h",
            140: "h",
            151: "h",
            152: "h",
            155: "h",
            168: "br",
            169: "br",
            170: "q",
            171: "br",
            184: "h",
            185: "h",
            186: "h",
            187: "h",
            188: "h",
            189: "h",
            198: "fp",
            203: "wl",
            204: "br",
            205: "wr",
        }
    },
    {
        "row": 9,
        "default_tile": "a",
        "tile_exceptions": {
            38: "pcl",
            39: "pcr",
            46: "psl",
            47: "psr",
            57: "psl",
            58: "psr",
            136: "h",
            137: "h",
            140: "h",
            141: "h",
            150: "h",
            151: "h",
            152: "h",
            155: "h",
            156: "h",
            183: "h",
            184: "h",
            185: "h",
            186: "h",
            187: "h",
            188: "h",
            189: "h",
            198: "fp",
            202: "p",
            203: "br",
            204: "br",
            205: "br",
            206: "p"
        }
    },
    {
        "row": 10,
        "default_tile": "a",
        "tile_exceptions": {
            28: "pcl",
            29: "pcr",
            38: "psl",
            39: "psr",
            46: "psl",
            47: "psr",
            57: "psl",
            58: "psr",
            135: "h",
            136: "h",
            137: "h",
            140: "h",
            141: "h",
            142: "h",
            149: "h",
            150: "h",
            151: "h",
            152: "h",
            155: "h",
            156: "h",
            157: "h",
            163: "pcl",
            164: "pcr",
            179: "pcl",
            180: "pcr",
            182: "h",
            183: "h",
            184: "h",
            185: "h",
            186: "h",
            187: "h",
            188: "h",
            189: "h",
            198: "fp",
            202: "br",
            203: "br",
            204: "d",
            205: "br",
            206: "br"
        }
    },
    {
        "row": 11,
        "default_tile": "a",
        "tile_exceptions": {
            28: "psl",
            29: "psr",
            38: "psl",
            39: "psr",
            46: "psl",
            47: "psr",
            57: "psl",
            58: "psr",
            134: "h",
            135: "h",
            136: "h",
            137: "h",
            140: "h",
            141: "h",
            142: "h",
            143: "h",
            148: "h",
            149: "h",
            150: "h",
            151: "h",
            152: "h",
            155: "h",
            156: "h",
            157: "h",
            158: "h",
            163: "psl",
            164: "psr",
            179: "psl",
            180: "psr",
            181: "h",
            182: "h",
            183: "h",
            184: "h",
            185: "h",
            186: "h",
            187: "h",
            188: "h",
            189: "h",
            198: "h",
            202: "br",
            203: "br",
            204: "d",
            205: "br",
            206: "br"
        }
    },
    {
        "row": 12,
        "default_tile": "b",
        "tile_exceptions": {
            69: 'a',
            70: 'a',
            86: 'a',
            87: 'a',
            88: 'a',
            153: 'a',
            154: 'a'
        }
    },
    {
        "row": 13,
        "default_tile": "b",
        "tile_exceptions": {
            69: 'a',
            70: 'a',
            86: 'a',
            87: 'a',
            88: 'a',
            153: 'a',
            154: 'a'
        }
    }
]


WIN_SCREEN = """＜　　　　＼　　　　／　　　　　　　　　　　　　　＞
＜　　　　　＼　　／　　　　　　　　　　　　　　　＞
＜　　　　　　｜｜　　｜＝＝｜　｜　　｜　　　　　＞
＜　　　　　　｜｜　　｜　　｜　｜　　｜　　　　　＞
＜　　　　　　｜｜　　｜　　｜　｜　　｜　　　　　＞
＜　／＼　　　｜｜　　｜＝＝｜　｜＝＝｜　　／＼　＞
＜／　　＼　　　　　　　　　　　　　　　　／　　＼＞
＜＼　　／　　　　　　　　　　　　　　　　＼　　／＞
＜　＼／　　｜　　　　｜　｟｠　　　　　　　＼／　＞
＜　　　　　｜　　　　｜　　　　　　　　　　　　　＞
＜　　　　　｜　　　　｜　｜｜　｜＼　　　｜　　　＞
＜　　　　　｜　　　　｜　｜｜　｜　＼　　｜　　　＞
＜　　　　　｜　／＼　｜　｜｜　｜　　＼　｜　　　＞
＜　　　　　｜／　　＼｜　｜｜　｜　　　＼｜　　　＞"""
GAME_OVER_SCREEN = """＜　　　　　　　　　　　　　　　　　　　　　　　　＞
＜　｜＝＝＝＝　　　　　　　　　　　　｜＝＝＝　　＞
＜　｜　　　　　　　　　　　｜＼／｜　｜　　　　　＞
＜　｜　　＝｜　　／＼　　　｜　　｜　｜＝　　　　＞
＜　｜　　　｜　／＝＝＼　　｜　　｜　｜　　　　　＞
＜　｜＝＝＝＝／　　　　＼　｜　　｜　｜＝＝＝　　＞
＜　　　　　　　　　　　　　　　　　　　　　　　　＞
＜　　　　　　　　　　　　　　　　　　　　　　　　＞
＜　｜＝＝＝｜　　　　　　｜＝＝＝　　｜　＝＝　　＞
＜　｜　　　｜　｜　　｜　｜　　　　　｜／　　　　＞
＜　｜　　　｜　｜　　｜　｜＝　　　　｜　　　　　＞
＜　｜　　　｜　＼　　／　｜　　　　　｜　　　　　＞
＜　｜＝＝＝｜　　＼／　　｜＝＝＝　　｜　　　　　＞
＜　　　　　　　　　　　　　　　　　　　　　　　　＞"""
PLAYER_STARTING_COORDINATES = [2, 11]
TILE_HEIGHT = 14
TILE_WIDTH = 212
TILE_PIXEL_HEIGHT = 1
TILE_PIXEL_WIDTH = 1
IMAGE_HEIGHT = TILE_HEIGHT * TILE_PIXEL_HEIGHT
IMAGE_WIDTH = TILE_WIDTH * TILE_PIXEL_WIDTH
VIEW_WIDTH = 26
START_VIEW = [0, VIEW_WIDTH]
END_VIEW = [TILE_WIDTH - VIEW_WIDTH, TILE_WIDTH]
MAX_TIME = 400
### Player States
JUMPING = "JUMPING"
APEX = "APEX"
FALLING = "FALLING"
STANDING = "STANDING"
PLANTING = "PLANTING"
## TILES
AIR = 'a'
PLAYER = "play"
FLAG = "f"
FLAG_POLE = "fp"
HARD_BLOCK = "h"
QUESTION = "q"
BRICK = "b"
DOOR = "d"
### GAME STATE
IN_PROGRESS = "IN PROGRESS"
GAME_OVER = "GAME OVER"
GAME_WON = "GAME WON"
### WON STATE
LOWER_FLAG = "LOWER_FLAG"
DISMOUNT = "DISMOUNT"
RUN_TO_RIGHT = "RUN TO RIGHT"
TALLY = "TALLY"

"""
A note for the notes:
Functional in this context is referring to a purely functional method. it does not mutate any of the inputs. Its only effect
is a return

Mutates in this context is referring to a method that either does not return, or does return while also mutating one 
or more of the inputs
"""

nominal_to_full_width_translation = str.maketrans(
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[]^_`{|}~',
    '０１２３４５６７８９ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！゛＃＄％＆（）＊＋、ー。／：；〈＝〉？＠［］＾＿‘｛｜｝～')


def full_width(nominal_str):
    """Functional: Translate nominal strings (like this) into ｆｕｌｌ ｗｉｄｔｈ variants"""
    return nominal_str.translate(nominal_to_full_width_translation).replace(" ", "　")


class Driver:
    """Hosts the implementation details between the desktop TK version and the RoboCo version"""
    _draw_fn = None
    _is_key_pressed_fn = None

    def __init__(self, draw_fn, is_key_pressed_fn):
        self._draw_fn = draw_fn
        self._is_key_pressed_fn = is_key_pressed_fn

    def draw(self, frame):
        self._draw_fn(frame)

    def is_input_pressed(self, key):
        return self._is_key_pressed_fn(key)


class Banner:
    _name = "ROBIO"
    _score = 0
    _num_coins = 0
    _world = "1-1"
    _time_left = MAX_TIME

    def __init__(self):
        self._start_time = perf_counter()
        self._subsection_len, self._remainder = divmod(VIEW_WIDTH, 4)

    def check_time(self):
        time_since_start = int(perf_counter() - self._start_time)
        time_left = MAX_TIME - time_since_start
        self._time_left = time_left
        if time_left <= 0:
            raise GameOverException

    def add_coin(self):
        self._score += COIN_WORTH
        self._num_coins += 1

    def _spaced(self, label, align="LEFT"):
        fill_spaces = (self._subsection_len - len(label)) * " "
        if align == "CENTER":
            half_num, rem_num = divmod(len(fill_spaces), 2)
            half = half_num * " "
            rem = rem_num * " "
            return "{}{}{}{}".format(half, label, rem, half)
        if align == "LEFT":
            return "{}{}".format(label, fill_spaces)
        else:  # RIGHT
            return "{}{}".format(fill_spaces, label)

    def get_top_line(self):
        top_line = ""
        top_line += self._spaced(self._name)
        top_line += self._remainder * " "
        top_line += self._spaced("")
        top_line += self._spaced("WORLD")
        top_line += self._spaced("TIME")
        return full_width(top_line + "\n")

    def get_bottom_line(self):
        bottom_line = ""
        bottom_line += self._spaced("{:06d}".format(self._score))
        bottom_line += self._remainder * " "
        bottom_line += self._spaced("Ox{:02d}".format(self._num_coins))
        bottom_line += self._spaced("1-1", "CENTER")
        bottom_line += self._spaced(" " + str(self._time_left))
        return full_width(bottom_line + "\n")

    def get_banner(self):
        return self.get_top_line() + self.get_bottom_line()


def init():
    """Functional: initializes the tile grid using the provided map and tile_to_pixel dictionary. Also initializes
    sprites """
    tile_to_pixel = init_tiles()
    tile_grid = generate_tile_grid(MAP)
    sprites = {
        "player": {
            "coordinates": PLAYER_STARTING_COORDINATES,  # x, y # todo 192 for end testing 2 for start
            "state": STANDING,
            "tile": PLAYER,
            "velocity": [0, 0]  # x, y
        },
        "flag": {
            "coordinates": [198, 1],
            "tile": FLAG,
            "velocity": [0, 0]  # x, y
        },
        "enemies": [],
        "objects": {
            "blocks": [
                {
                    "type": "coin",
                    "amount": 1,
                    "strong": False,
                    "tile": QUESTION,
                    "coordinates": [16, 8]
                },
                {
                    "type": "brick",
                    "amount": None,
                    "strong": True,
                    "tile": BRICK,
                    "coordinates": [20, 8]
                },
                {
                    "type": "prize",
                    "amount": 1,
                    "prize"
                    "strong": True,
                    "tile": BRICK,
                    "coordinates": [20, 8]
                }
            ]
        }
    }
    return tile_grid, sprites, tile_to_pixel


### DRAW SPRITES ###
def draw_sprites(static_grid, sprites):
    """Functional: adds sprites to the static_grid and returns an updated grid"""
    tile_grid_with_sprites = copy_list(static_grid)
    # draw_objects(sprites["objects"], tile_grid_with_sprites)
    # draw_enemies(sprites["enemies"], tile_grid_with_sprites)
    draw_player(sprites["player"], tile_grid_with_sprites)
    draw_flag(sprites["flag"], tile_grid_with_sprites)
    return tile_grid_with_sprites


def draw_player(player, grid):
    """Mutates grid: adds the player to the grid"""
    p_x, p_y = player["coordinates"]
    grid[p_y][p_x] = player["tile"]


def draw_flag(flag, grid):
    """Mutates grid: adds the flag to the grid"""
    x, y = flag["coordinates"]
    grid[y][x] = flag["tile"]


def draw_enemies(enemies, grid):
    """Mutates grid: adds enemies to the grid"""
    for enemy in enemies:
        e_x, e_y = enemy["coordinates"]
        tile = enemy["tile"]
        grid[e_y][e_x] = tile


def draw_objects(objects, grid):
    """Mutates grid: adds objects to the grid"""
    for obj in objects:
        o_x, o_y = obj["coordinates"]
        tile = obj["tile"]
        grid[o_y][o_x] = tile


### END DRAW SPRITES ###
### HANDLE MOVEMENT ###
def handle_movement(grid, sprites, view):
    """Functional: Calculates the next coordination position of entities"""
    updated_sprites = copy_dict(sprites)
    handle_player_movement(updated_sprites["player"], grid, view)
    handle_flag_movement(updated_sprites["flag"], grid)
    handle_enemy_movement(updated_sprites["enemies"], grid)
    handle_object_movement(updated_sprites["objects"], grid)
    return updated_sprites


def handle_cutscene_movement(grid, sprites):
    """Functional: Special handler for cutscene movement. Breaks rules that exist normally in the game. Ignores
    everything but the player and flag """
    updated_sprites = copy_dict(sprites)
    handle_player_cutscene_movement(updated_sprites["player"], grid)
    handle_flag_movement(updated_sprites["flag"], grid)
    return updated_sprites


def handle_player_movement(player, grid, view):
    """Mutates player: Player movement handler that translate velocities into actual position changes"""
    p_x, p_y = player["coordinates"]
    v_x, v_y = player["velocity"]
    state = player["state"]
    tile_above, tile_below, tile_left, tile_right = get_adjacent_tiles(p_x, p_y, grid)
    v_y, p_y, state = handle_y(v_y, p_y, tile_above, tile_below, state)
    tile_above, tile_below, tile_left, tile_right = get_adjacent_tiles(p_x, p_y, grid)
    v_x, p_x = handle_x(v_x, p_x, tile_left, tile_right, p_x - 1 < view[0], is_player=True)
    player["velocity"] = [v_x, v_y]
    player["coordinates"] = [p_x, p_y]
    player["state"] = state


def handle_player_cutscene_movement(player, grid):
    """Mutates player: Special player handler for cutscene movement. Breaks rules that exist normally. Ignores blocks
    and certain velocities """
    p_x, p_y = player["coordinates"]
    v_x, v_y = player["velocity"]
    tile_below = safe_get(grid, p_y + 1, p_x)
    if v_y < 0 and tile_below is not None:  # going down
        if tile_below == AIR:
            p_y += 1
        else:
            v_y = 0
    if v_x > 0:  # going right
        v_x -= 1
        p_x += 1
    elif v_x < 0:  # going left
        v_x += 1
        p_x -= 1
    player["velocity"] = [v_x, v_y]
    player["coordinates"] = [p_x, p_y]


def handle_flag_movement(flag, grid):
    """Mutates flag: Handle flag movements, the flag only goes down"""
    p_x, p_y = flag["coordinates"]
    v_x, v_y = flag["velocity"]
    if v_y == 0:
        return
    tile_below = safe_get(grid, p_y + 1, p_x)
    if tile_below is FLAG_POLE:
        p_y += 1
        v_y += 1
    flag["coordinates"] = [p_x, p_y]
    flag["velocity"] = [v_x, v_y]


def handle_enemy_movement(enemies, grid):
    """Todo"""
    return


def handle_object_movement(objects, grid):
    """Todo"""
    return


def handle_y(v_y, p_y, tile_above, tile_below, state):
    """Functional: Generic y-axis movement handler. Updates entity states, velocities, and positions based on terrain"""
    if state is PLANTING:
        state = STANDING
    if v_y > 0:  # going up
        if tile_above == AIR:
            v_y -= 1  # slow down
            p_y -= 1  # go up less y is higher
            if v_y == 0:
                state = APEX
        else:
            v_y = 0
    elif v_y < 0 and tile_below is not None:  # going down
        if tile_below == AIR:
            p_y += 1
        else:
            v_y = 0
            state = PLANTING
    return v_y, p_y, state


def handle_x(v_x, p_x, tile_left, tile_right, at_left_bound, is_player=False):
    """Functional: Generic x-axis movement handler. Updates entity states, velocities, and positions based on terrain"""
    if v_x > 0:  # going right
        if tile_right is None or tile_right != AIR:
            v_x = 0
        else:
            v_x -= 1
            p_x += 1
    elif v_x < 0:  # going left
        if tile_left is None or tile_left != AIR or (is_player and at_left_bound):
            v_x = 0
        else:
            v_x += 1
            p_x -= 1
    return v_x, p_x


def check_for_falling(grid, sprites):
    """Functional: Checks if an entity is in a position where they should be falling, and updates their velocity
    and state accordingly if so. Also handles. Also determines when a Game Over state has been reached"""

    def check_entity_for_falling(entity):
        p_x, p_y = entity["coordinates"]
        v_x, v_y = entity["velocity"]
        state = entity["state"]
        tile_below = safe_get(grid, p_y + 1, p_x)
        if state is APEX:
            entity["state"] = FALLING
        elif v_y == 0 and tile_below is AIR:
            v_y = -1
            entity["velocity"] = [v_x, v_y]
            entity["state"] = FALLING
        elif v_y == 0 and tile_below is not AIR:
            entity["state"] = STANDING
        elif v_y <= 0 and tile_below is None:
            raise GameOverException

    new_sprites = copy_dict(sprites)
    check_entity_for_falling(new_sprites["player"])
    for enemy in new_sprites["enemies"]:
        check_entity_for_falling(enemy)
    return new_sprites


def check_inside_block(static_grid, sprites):
    """Functional: Checks if an entity is inside a block and tries to dislodge them if so"""

    def attempt_to_dislodge(entity, p_x, p_y):
        if safe_get(static_grid, p_y, p_x - 1) is not None:
            p_x -= 1
        elif safe_get(static_grid, p_y - 1, p_x) is not None:
            p_y -= 1
        elif safe_get(static_grid, p_y + 1, p_x) is not None:
            p_y = + 1
        elif safe_get(static_grid, p_y, p_x + 1) is not None:
            p_x += 1
        else:
            p_x, p_y = PLAYER_STARTING_COORDINATES
        entity["coordinates"] = [p_x, p_y]

    def check_entity_inside_block(entity):
        p_x, p_y = entity["coordinates"]
        static_grid_tile = safe_get(static_grid, p_y, p_x)
        if static_grid_tile is not AIR:
            attempt_to_dislodge(entity, p_x, p_y)

    new_sprites = copy_dict(sprites)
    check_entity_inside_block(new_sprites["player"])
    for enemy in new_sprites["enemies"]:
        check_entity_inside_block(enemy)
    return new_sprites


### END HANDLE MOVEMENT ###
### UTIL ###
def safe_get(grid, y, x):
    """Functional: Allows users to get coordinates on a grid without fear of an IndexError"""
    try:
        return grid[y][x]
    except IndexError:
        return None


def copy_dict(dictionary):
    """Functional: Recursively copies a dictionary with support for deep copy of dictionaries and lists"""
    new_dict = {}
    for key, value in dictionary.items():
        if type(value) == dict:
            value = copy_dict(value)
        elif type(value) == list:
            value = copy_list(value)
        new_dict[key] = value
    return new_dict


def copy_list(a_list):
    """Functional: Recursively copies a list with support for deep copy of dictionaries and lists"""
    new_list = []
    for item in a_list:
        if type(item) == list:
            item = copy_list(item)
        elif type(item) == dict:
            item = copy_dict(item)
        new_list.append(item)
    return new_list


def get_adjacent_tiles(x, y, grid):
    """Functional: Helper function to get cardinally adjacent tiles"""
    tile_above = safe_get(grid, y - 1, x)
    tile_below = safe_get(grid, y + 1, x)
    tile_left = safe_get(grid, y, x - 1)
    tile_right = safe_get(grid, y, x + 1)
    return tile_above, tile_below, tile_left, tile_right


### END UTIL ###


def convert_tiles_to_pixels(tile_grid, tile_to_pixel):
    pixels = []
    for y in range(0, IMAGE_HEIGHT):
        row = []
        for x in range(0, IMAGE_WIDTH):
            y_tile, y_tile_pixel = divmod(y, TILE_PIXEL_HEIGHT)
            x_tile, x_tile_pixel = divmod(x, TILE_PIXEL_WIDTH)
            tile = tile_grid[y_tile][x_tile]
            tile_pixels = tile_to_pixel[tile]
            pixel = tile_pixels[y_tile_pixel][x_tile_pixel]
            row.append(pixel)
        debug = len(row)
        pixels.append(row)
    return pixels


def generate_tile_grid(coordinates):
    tile_grid = []
    for row in range(0, TILE_HEIGHT):
        tile_grid.append(generate_tile_row(coordinates[row]))
    return tile_grid


def generate_tile_row(row):
    exceptions = row["tile_exceptions"]
    default_tile = row["default_tile"]
    row = []
    for x in range(0, TILE_WIDTH):
        if x in exceptions:
            tile = exceptions[x]
            row.append(tile)
        else:
            row.append(default_tile)
    return row


### RENDER ###
def render(tile_grid, view, tile_to_pixel, banner):
    image_pixels = convert_tiles_to_pixels(tile_grid, tile_to_pixel)
    frame = ""
    for row in image_pixels:
        tile_start = view[0]
        tile_end = view[1]
        pixel_start = tile_start * TILE_PIXEL_WIDTH
        pixel_end = tile_end * TILE_PIXEL_WIDTH
        render_row = row[pixel_start:pixel_end]
        row_text = ''.join(render_row)
        row_text += '\n'
        frame += row_text
    frame = banner.get_banner() + frame
    return frame



### END RENDER ###
### PLAYER ACTIONS ###
def move_left(player):
    v_x, v_y = player["velocity"]
    player["velocity"] = [v_x - 1, v_y]


def move_right(player):
    v_x, v_y = player["velocity"]
    player["velocity"] = [v_x + 1, v_y]


def jump(player):
    v_x, v_y = player["velocity"]
    state = player["state"]
    if state is STANDING and v_y == 0:
        v_y += 4
        state = JUMPING
    player["velocity"] = [v_x, v_y]
    player["state"] = state


### END PLAYER ACTIONS ###

def update_view(player, view):
    """Updates the view to contain the player. Keeps the player in the far left to middle
    of the screen. Does not mutate view or player"""
    p_x, p_y = player["coordinates"]
    dist_from_right = view[1] - p_x
    boundary = VIEW_WIDTH // 2
    if dist_from_right < boundary:
        adjust = boundary - dist_from_right
        view[0] += adjust
        view[1] += adjust
    if view[0] > END_VIEW[0] or view[1] > END_VIEW[1]:
        view = END_VIEW
    return view


class GameOverException(Exception):
    pass


def init_tiles():
    air_tile = [["　"]]
    block_tile = [["＠"]]
    brick_tile = [["＃"]]
    question_tile = [["？"]]
    pipe_stem_left_tile = [["｜"]]
    pipe_stem_right_tile = [["｜"]]
    pipe_cap_right_tile = [["＞"]]
    pipe_cap_left_tile = [["＜"]]
    hard_tile = [["＠"]]
    flag_pole_tile = [["｜"]]
    flag_tile = [["Ｏ"]]
    castle_parapet_tile = [["＾"]]
    castle_door_tile = [["　"]]
    castle_window_left_tile = [["［"]]
    castle_window_right_tile = [["］"]]
    player_tile = [["Ｘ"]]
    tiles = {
        "a": air_tile,
        "b": block_tile,
        "br": brick_tile,
        "q": question_tile,
        "psl": pipe_stem_left_tile,
        "psr": pipe_stem_right_tile,
        "pcl": pipe_cap_left_tile,
        "pcr": pipe_cap_right_tile,
        "h": hard_tile,
        "f": flag_tile,
        "fp": flag_pole_tile,
        "p": castle_parapet_tile,
        "d": castle_door_tile,
        "wl": castle_window_left_tile,
        "wr": castle_window_right_tile,
        "play": player_tile
    }
    return tiles


### HANDLE GAME WON ###
def check_for_game_won(grid, player):
    p_x, p_y = player["coordinates"]
    v_x, v_y = player["velocity"]
    tile_right = safe_get(grid, p_y, p_x + 1)
    if tile_right is FLAG_POLE and v_x > 0:
        return True
    return False


#

def lower_flag(grid, sprites):
    state = LOWER_FLAG
    new_sprites = copy_dict(sprites)
    player = new_sprites["player"]
    p_x, p_y = player["coordinates"]
    pv_x, pv_y = player["velocity"]
    flag = new_sprites["flag"]
    f_x, f_y = flag["coordinates"]
    fv_x, fv_y = flag["velocity"]
    # flag is above player
    tile_below_flag = safe_get(grid, f_y + 1, f_x)
    tile_left_of_player = safe_get(grid, p_y, p_x - 1)
    if f_x > p_x and f_y < p_y:
        fv_y -= 1
        sleep(0.25)
    elif tile_below_flag is not HARD_BLOCK and tile_below_flag is not PLAYER:
        fv_y -= 1
        pv_y -= 1
        sleep(0.25)
    elif tile_left_of_player is not HARD_BLOCK:
        pv_x += 1
        sleep(0.25)
    else:
        state = RUN_TO_RIGHT
        fv_x = 0
        fv_y = 0
        pv_x = 0
        pv_y = 0
    flag["velocity"] = [fv_x, fv_y]
    player["velocity"] = [pv_x, pv_y]
    return new_sprites, state


def run_to_right(grid, sprites):
    new_sprites = copy_dict(sprites)
    player = new_sprites["player"]
    state = RUN_TO_RIGHT
    p_x, p_y = player["coordinates"]
    pv_x, pv_y = player["velocity"]
    tile_above = safe_get(grid, p_y - 1, p_x)
    if tile_above is not DOOR:
        pv_x = 1
        sleep(0.25)
    else:
        state = TALLY
    player["velocity"] = [pv_x, pv_y]
    return new_sprites, state


### END HANDLE GAME WON

# def draw_banner():
#     name = "Roboio"
#     world = "1-1"
#     time
# goomba worth 100
# mushroom worth 1000
# flower woth 1000
# flag worth 5000
# coin worth 200 points
# 100 coins => new life
COIN_WORTH = 200
FLAG_WORTH = 5000


### GAME LOOP
def game_loop(driver: Driver, fps):
    sleep_time = 1 / fps
    view = START_VIEW
    static_grid, sprites, tile_to_pixel = init()
    game_state = IN_PROGRESS
    won_state = None
    banner = Banner()
    while True:
        try:
            if game_state is  IN_PROGRESS:
                banner.check_time()
            frame_grid = draw_sprites(static_grid, sprites)
            view = update_view(sprites["player"], view)
            frame = render(frame_grid, view, tile_to_pixel, banner)
            frame = debug(sprites, frame)
            driver.draw(frame)
            if game_state is IN_PROGRESS:
                if check_for_game_won(frame_grid, sprites["player"]):
                    game_state = GAME_WON
                    won_state = LOWER_FLAG
                    sprites["player"]["velocity"] = [0, 0]
                else:
                    sprites = check_inside_block(static_grid, sprites)
                    sprites = check_for_falling(frame_grid, sprites)
                    sprites = handle_movement(frame_grid, sprites, view)
                    sprites = update_player_with_inputs(driver, sprites)
                    sleep(sleep_time)
            elif game_state is GAME_WON:
                if won_state is TALLY:
                    sleep(1)
                    driver.draw(WIN_SCREEN)
                    sleep(5)
                    break
                else:
                    if won_state is LOWER_FLAG:
                        sprites, won_state = lower_flag(frame_grid, sprites)
                    elif won_state is RUN_TO_RIGHT:
                        sprites, won_state = run_to_right(frame_grid, sprites)
                    sprites = handle_cutscene_movement(frame_grid, sprites)
            else:
                driver.draw(GAME_OVER_SCREEN)
                sleep(5)
                break
        except GameOverException:
            game_state = GAME_OVER
            pass


### Impl varies from RoboCo to tk###
def update_player_with_inputs(driver: Driver, sprites):
    new_dict = copy_dict(sprites)
    new_player = new_dict["player"]
    if driver.is_input_pressed("w"):
        jump(new_player)
    if driver.is_input_pressed("d"):
        move_right(new_player)
    if driver.is_input_pressed("a"):
        move_left(new_player)
    return new_dict


def debug(sprites, frame):
    player_state = sprites["player"]["state"]
    vx, vy = sprites["player"]["velocity"]
    x, y = sprites["player"]["coordinates"]
    frame = frame + "\n" + player_state + " v: [{}, {}] c: [{}, {}]".format(vx, vy, x, y)
    return frame


## END GAME LOOP

######################################
# Python TK Driver
######################################
# from time import sleep, perf_counter
# import keyboard
# from tkinter import *

def main():
    fps = 15
    root = Tk()
    label = Label(root)
    label.pack()
    frame_text = StringVar()
    label = Label(root, textvariable=frame_text, font=("Times", "18"), fg='blue')
    label.pack()

    def screen_writer_fn(frame):
        frame_text.set(frame)
        root.update()

    is_key_pressed_fn = lambda key: keyboard.is_pressed(key)
    driver = Driver(screen_writer_fn, is_key_pressed_fn)
    game_loop(driver, fps)


if __name__ == '__main__':
    main()

######################################
# RoboCo Driver
######################################
# from inputs import *
# from controllables import *
# from sensors import *
# from scriptruntime import *
# from ports import *
# from color import *
# from math import tau
# from time import sleep
# input_stream_a = Input.stream("a")
# input_stream_d = Input.stream("d")
# input_stream_w = Input.stream("w")
#
# def main():
#     screen = init_screen()
#     fps = 15
#     def screen_writer_fn(frame):
#         screen.text = frame
#     is_key_pressed_fn = lambda key: Input.pressed(key)
#     driver = Driver(screen_writer_fn, is_key_pressed_fn)
#     game_loop(driver, fps)
#
# def init_screen():
#     screen = TextScreen(0)
#     screen.horizontal_alignment = TextScreen.HorizontalAlignment.LEFT
#     screen.vertical_alignment = TextScreen.VerticalAlignment.MIDDLE
#     screen.auto_size = False
#     screen.size = 70
#     return screen
#
#
# if __name__ == "__main__":
#     main()
#

