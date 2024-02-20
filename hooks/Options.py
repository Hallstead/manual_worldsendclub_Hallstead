# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, SpecialRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world. 
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class GameMode(Choice):
    """
    Story Mode plays similar to the regular game and can be played from a new save or a completed one.
    Acts Mode is just playibg the Act levels in a random order
    """
    display_name = "Story Mode or Acts?"
    option_story = 0
    option_acts = 1

class Victory(Choice):
    """
    Good End is that you beat thr final boss and complete the story.
    Sticker Hunt has you collecting all the stickers as the goal.
    """
    display_name = "Victory Condition"
    option_good_end = 0
    option_sticker_hunt = 1

class Stickersanity(Toggle):
    """Should Sticker locations be included in the randomizer?"""
    display_name = "Stickersanity"

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["GameMode"] = GameMode
    options["VictoryChoice"] = Victory
    options["Stickersanity"] = Stickersanity
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options