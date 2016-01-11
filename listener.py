#!/bin/python3

import argparse

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Processing messages coming from TELEGRAM-CLI as arguments')
    p.add_argument('msg', metavar='msg', type=str, help='received message')
    args = p.parse_args()

    print("MESSAGE VON HASI: " + args.msg)

