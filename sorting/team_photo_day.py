from collections import namedtuple
from typing import List

class Team:
    Player: namedtuple('Player', ('height'))
    def __init__(self, heights: List[int]):
        self.player_heights = [Player(height) for height in heights]
    # O(n log n)
    def valid_placement_exists(self, team_one: 'Team', team_two: 'Team') -> bool:
        # sort
        team_one.player_heights.sort()
        team_two.player_heights.sort()
        # go through teams and if any placement is invalid, return False
        for one, two in zip(team_one.player_heights, team_two.player_heights):
            if one > two:
                return False
        return True

