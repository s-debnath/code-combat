# 841. Keys and Rooms
# Difficulty: Medium
# https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        can_visit = [False] * len(rooms)
        can_visit[0] = True
        has_visited = set()
        
        visit_room(rooms, 0, can_visit, has_visited)
        
        return all(can_visit)
        

def visit_room(rooms: List[List[int]], room_number: int, can_visit: List[bool], has_visited: set):
    if room_number in has_visited:
        return
    
    has_visited.add(room_number)
    
    for other_key in rooms[room_number]:
        can_visit[other_key] = True
        visit_room(rooms, other_key, can_visit, has_visited)
