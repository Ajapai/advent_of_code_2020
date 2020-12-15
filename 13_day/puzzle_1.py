#!/usr/bin/env python3

lines = open('input').read().splitlines()

timestamp = int(lines[0])
bus_ids = [int(bus_id) for bus_id in lines[1].split(",") if bus_id != "x"]
closest_departures = [0] * len(bus_ids)
for i, bus_id in enumerate(bus_ids):
    while closest_departures[i] < timestamp:
        closest_departures[i] += bus_ids[i]

print((min(closest_departures) - timestamp) * bus_ids[closest_departures.index(min(closest_departures))])
