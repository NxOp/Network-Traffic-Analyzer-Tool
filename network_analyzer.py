import os
import sys
import time
import random
from scapy.all import *

class NetworkAnalyzer:
    def __init__(self):
        pass

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        header = "\033[1;33;56m" + "cybehacker" + "\033[0m"
        print(header.center(os.get_terminal_size().columns))

    def random_color(self):
        return random.choice(['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[91m', '\033[92m', '\033[93m', '\033[94m'])

    def print_colored_banner(self):
        banner = """
      ___                                     ___           ___           ___           ___           ___           ___           ___     
     /\__\                     _____         /\__\         /\  \         /\  \         /\__\         /|  |         /\__\         /\  \    
    /:/  /          ___       /::\  \       /:/ _/_        \:\  \       /::\  \       /:/  /        |:|  |        /:/ _/_       /::\  \   
   /:/  /          /|  |     /:/\:\  \     /:/ /\__\        \:\  \     /:/\:\  \     /:/  /         |:|  |       /:/ /\__\     /:/\:\__\  
  /:/  /  ___     |:|  |    /:/ /::\__\   /:/ /:/ _/_   ___ /::\  \   /:/ /::\  \   /:/  /  ___   __|:|  |      /:/ /:/ _/_   /:/ /:/  /  
 /:/__/  /\__\    |:|  |   /:/_/:/\:|__| /:/_/:/ /\__\ /\  /:/\:\__\ /:/_/:/\:\__\ /:/__/  /\__\ /\ |:|__|____ /:/_/:/ /\__\ /:/_/:/__/___
 \:\  \ /:/  /  __|:|__|   \:\/:/ /:/  / \:\/:/ /:/  / \:\/:/  \/__/ \:\/:/  \/__/ \:\  \ /:/  / \:\/:::::/__/ \:\/:/ /:/  / \:\/:::::/  /
  \:\  /:/  /  /::::\  \    \::/_/:/  /   \::/_/:/  /   \::/__/       \::/__/       \:\  /:/  /   \::/~~/~      \::/_/:/  /   \::/~~/~~~~ 
   \:\/:/  /   ~~~~\:\  \    \:\/:/  /     \:\/:/  /     \:\  \        \:\  \        \:\/:/  /     \:\~~\        \:\/:/  /     \:\~~\     
    \::/  /         \:\__\    \::/  /       \::/  /       \:\__\        \:\__\        \::/  /       \:\__\        \::/  /       \:\__\    
     \/__/           \/__/     \/__/         \/__/         \/__/         \/__/         \/__/         \/__/         \/__/         \/__/    

        """
        colored_banner = self.random_color() + banner + '\033[0m'
        print(colored_banner.center(os.get_terminal_size().columns))
    
    def print_tool_details(self):
        details = [
            '\033[31mNetwork Traffic Analyzer Tool\033[0m',
            '\033[32m========================================\033[0m',
            '\033[33mThis tool captures and analyzes network traffic.\033[0m',
            '\033[34mIt provides basic traffic insights and packet analysis.\033[0m',
            '\033[35mPlease note that this tool is for demonstration purposes only.\033[0m'
        ]
        for line in details:
            print(line)
    
    def capture_traffic(self, interface):
        print("\033[36mCapturing traffic on interface:", interface, "\033[0m")
        try:
            sniff(iface=interface, prn=self.analyze_packet, filter="ip")
        except KeyboardInterrupt:
            print("\033[91mStopping capture...\033[0m")

    def analyze_packet(self, packet):
        # Your analysis logic here
        print("\033[92mPacket captured:", packet.summary(), "\033[0m")

    def main(self):
        self.clear_screen()
        self.print_colored_banner()
        self.print_tool_details()

        # Ask for relevant information
        interface = input("\033[93mEnter the interface to capture traffic (e.g., eth0): \033[0m")
        
        try:
            # Start capturing traffic
            self.capture_traffic(interface)
        except Exception as e:
            print("\033[91mAn error occurred:", e, "\033[0m")

if __name__ == "__main__":
    analyzer = NetworkAnalyzer()
    analyzer.main()
