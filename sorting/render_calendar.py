from collections import namedtuple
from typing import List

Event = namedtuple('Event', ('start', 'finish'))

def find_max_simultaneous_events(A: List[Event]) -> int:
    # Create an endpoint object to store time and flag for
    # whether it is a starting time or an ending time.
    Endpoint = namedtuple('Endpoint', ('time', 'is_start'))
    # Setup array of enpoints
    endpoints = []
    for event in A:
        endpoints.append(
            (
                Endpoint(event.start, True),
                Endpoint(event.end, False),
        )
    # Sort by end time and break the tie by using the start time
    endpoints.sort(key=lambda event: (event.time, not event.is_start))
    max_num_of_sim_events, num_of_sim_events = 0, 0
    for endpoint in endpoints:
        if endpoint.is_start:
            num_of_sim_events += 1
            max_num_of_sim_events = max(max_num_of_sim_events, num_of_sim_events)
        else:
            num_of_sim_events -= 1
    return max_num_of_sim_events

