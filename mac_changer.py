#!/bin/python

import subprocess as sp
import optparse as op


def get_arguments():
    parser = op.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (opts, arguments) = parser.parse_args()

    if not opts.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not opts.new_mac:
        parser.error("[-] Please specify a New MAC Address, use --help for more info.")
    else:
        return opts


def change_mac(interface, new_mac):

    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    sp.call(["ifconfig", interface, "down"])
    sp.call(["ifconfig", interface, "hw", "ether", new_mac])
    sp.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
