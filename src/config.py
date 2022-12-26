# Parameters for generator
NUMBER_OF_WORKERS = 20
BLENDING_LIST = [
    "gaussian",
    # "poisson",  # takes a lot of time and results are not that good
    # "poisson-fast",  # only with Docker GPU
    "none",
    # "box",
    "motion",
    # "mixed",
    # "illumination",
    # "gamma_correction",
]

# Parameters for images
MIN_NO_OF_OBJECTS = 1
MAX_NO_OF_OBJECTS = 1
MIN_NO_OF_DISTRACTOR_OBJECTS = 1
MAX_NO_OF_DISTRACTOR_OBJECTS = 1
MAX_ATTEMPTS_TO_SYNTHESIZE = 20

# Parameters for objects in images
MIN_SCALE = 0.15  # min scale for scale augmentation (maximum extend in each direction, 1=same size as image)
MAX_SCALE = 0.4  # max scale for scale augmentation (maximum extend in each direction, 1=same size as image)
MAX_UPSCALING = 1.2  # increase size of foreground by max this defauft (1.2)
MAX_DEGREES = 30  # max rotation allowed during rotation augmentation
MAX_TRUNCATION_FRACTION = (
    0.3  # max fraction to be truncated = MAX_TRUNCACTION_FRACTION*(WIDTH/HEIGHT)
)
MIN_TRUNCATION_FRACTION = (
    0.25  # min fraction to be truncated = MIN_TRUNCACTION_FRACTION*(WIDTH/HEIGHT)
)
MAX_ALLOWED_IOU = 0.01  # IOU > MAX_ALLOWED_IOU is considered an occlusion, need dontocclude=True

# Parameters for image loading
MINFILTER_SIZE = 3

# Other
OBJECT_CATEGORIES = [
    {"id": 0, "name": "bus"},
    {"id": 1, "name": "car"},
    {"id": 2, "name": "cleanser"},
    {"id": 3, "name": "clock"},
    {"id": 4, "name": "cup"},
    {"id": 5, "name": "headphones"},
    {"id": 6, "name": "mouse"},
    {"id": 7, "name": "scissors"},
    {"id": 8, "name": "shoe"},
    {"id": 9, "name": "stapler"},
    {"id": 10, "name": "sunglasses"},
    {"id": 11, "name": "tape_cutter"},
    {"id": -1, "name": "distractor"},
]
# OBJECT_CATEGORIES = [
#     {"id": 0, "name": "pringles_bbq"},
#     {"id": 1, "name": "red_cup"},
#     {"id": -1, "name": "distractor"},
# ]  # note: distractor needs to be second position
IGNORE_LABELS = [OBJECT_CATEGORIES[-1]["id"]]  # list of category ID for which no annotations will be generated
INVERTED_MASK = False  # Set to true if white pixels represent background
SUPPORTED_IMG_FILE_TYPES = (".jpg", "jpeg", ".png", ".gif")
