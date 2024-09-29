from dataclasses import dataclass, asdict
from typing import List, Tuple
from os import listdir

import json
import socket
import sys
import time

@dataclass
class Scenario:
    coordinates_points: List[Tuple[int,int,int,int]]

@dataclass
class Coords:
    coordinates: Tuple[int,int,int,int]

def load_scenario(file_path):
    with open(file_path) as scenario_file:
        scenario_struct = Scenario(json.loads(scenario_file.read()))
        return scenario_struct

def execute_scenario(socket, server_address, scenario):
    try:
        scs = load_scenario(scenario)
        for n in scs.coordinates_points["array"]:
            single_coords = Coords(coordinates = n)
            json_message = json.dumps(asdict(single_coords))
            sent = socket.sendto(json_message.encode(), server_address)
            time.sleep(2)

    finally:
        print("End of Scenario...")

def udp_send_coordinates(scenario, server_host="127.0.0.1", server_port=12345):
    print(f"Connecting to UDP server on {server_host}:{server_port}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (server_host, server_port)

    execute_scenario(sock, server_address, scenario)

    sock.close()

if __name__ == "__main__":
    scenarious_dir = "scenarious"
    scenarious = listdir(scenarious_dir)

    for scenario in scenarious:
        if len(sys.argv) == 3:
            _server_host = sys.argv[1]
            _server_port = int(sys.argv[2])
            udp_send_coordinates(scenarious_dir + "/" + scenario, server_host=_server_host, server_port=_server_port)
        else:
            udp_send_coordinates(scenarious_dir + "/" + scenario)
