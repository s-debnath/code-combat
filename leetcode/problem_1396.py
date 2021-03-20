# 1396. Design Underground System
# Difficulty: Medium
# https://leetcode.com/problems/design-underground-system/

import statistics

class UndergroundSystem:

    def __init__(self):
        self.passenger_tracking = {}
        self.station_travel_stats = {}
        

    def checkIn(self, id: int, start_station: str, entry_time: int) -> None:
        if id in self.passenger_tracking:
            raise Exception("Passenger already checked in.")
        
        self.passenger_tracking[id] = (start_station, entry_time)
        

    def checkOut(self, id: int, end_station: str, exit_time: int) -> None:
        if id not in self.passenger_tracking:
            raise Exception("Passenger does not exist on train.")
        
        start_station, entry_time = self.passenger_tracking[id]
        del self.passenger_tracking[id]
        
        stats_key = (start_station, end_station)
        
        if stats_key not in self.station_travel_stats:
            self.station_travel_stats[stats_key] = []
        
        self.station_travel_stats[stats_key].append(exit_time - entry_time)
        

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        stats_key = (start_station, end_station)
        
        if stats_key not in self.station_travel_stats:
            return None
        
        return statistics.mean(self.station_travel_stats[stats_key])
        
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
