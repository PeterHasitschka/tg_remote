#!/bin/python3

import argparse

from commandswitcher import CommandSwitcher

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Processing messages coming from TELEGRAM-CLI as arguments')
    p.add_argument('msg', metavar='msg', type=str, help='received message')
    args = p.parse_args()

    if args.msg == None:
        print("ERROR: Could not get message!")
        exit()

    cmd_switcher = CommandSwitcher(args.msg)
    cmd_switcher.execute()






