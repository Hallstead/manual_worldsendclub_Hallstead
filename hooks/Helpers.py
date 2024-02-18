from typing import Optional
from BaseClasses import MultiWorld
from .. import Helpers


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(world: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    if category_name == "Story" or category_name == "Path" or category_name == "Key Items":
        if Helpers.get_option_value(world, player, "GameMode") == 0:
            return True
        return False
    if category_name == "Acts":
        if Helpers.get_option_value(world, player, "GameMode") == 1:
            return True
        return False
    return None
