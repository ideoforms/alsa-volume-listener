#!/usr/bin/env python3 

import argparse
import alsaaudio
from pythonosc.udp_client import SimpleUDPClient
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.dispatcher import Dispatcher

def main(alsa_control_name,
         osc_port):
    dispatcher = Dispatcher()
    mixer = alsaaudio.Mixer(alsa_control_name)

    def set_volume(address, *args):
        if len(args) != 1:
            raise ValueError("Invalid number of arguments (expected 1)")
        if not isinstance(args[0], float):
            raise ValueError("Argument is not a float")
        if args[0] < 0 or args[0] > 1:
            raise ValueError("Argument is outside of expected range")
        volume = int(args[0] * 100)
        mixer.setvolume(volume)
    dispatcher.map("/set_volume", set_volume)
    server = BlockingOSCUDPServer(("0.0.0.0", osc_port), dispatcher)

    server.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OSC server to set Alsa volume level")
    parser.add_argument("--alsa-control-name", default="Speaker")
    parser.add_argument("--osc-port", default=13007)
    args = parser.parse_args()

    main(alsa_control_name=args.alsa_control_name,
         osc_port=args.osc_port)
