# Project: Brewing Automation System - Capstone Project
# Purpose Details: Dal Class
# Course: IST 440W - 001
# Author: Team Kegging
# Date Developed: 3/23
# Last Date Changed:3/23
# Rev

class dal:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    def get_host(self):
        return self.host
    def get_port(self):
        return self.port