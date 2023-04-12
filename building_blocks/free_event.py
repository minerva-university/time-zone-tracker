"""
Basic initial sketch of free time blocks
"""

class Event:
    """
    Overlapped free time event block
    
    -datetime format:  YYYY-MM-DDTHH:MM:SS+TIME_ZONE_HH:TIME_ZONE_MM
    """
    def __init__(self, start_datetime, end_datetime):
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime


event1 = Event('2023-04-12T00:30:00+08:00', '2023-03-15T23:02:00+08:00')
event2 = Event('2023-04-12T09:30:00+08:00', '2023-04-12T10:30:00+08:00')
event3 = Event('2023-04-12T21:30:00+08:00', '2023-04-12T22:00:00+08:00')

free_blocks = [event1, event2, event3]