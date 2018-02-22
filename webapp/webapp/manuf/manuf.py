#!/usr/bin/env python  
#coding: utf-8 

from __future__ import print_function
from collections import namedtuple
import argparse
import re
import sys
import io

try:
    from urllib2 import urlopen
    from urllib2 import URLError
except ImportError:
    from urllib.request import urlopen
    from urllib.error import URLError

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

Vendor = namedtuple('Vendor', ['manuf', 'comment'])

class MacParser(object):
    MANUF_URL = "https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf"
    def  __init__(self, manuf_name="./manuf", update=False):
        self._manuf_name = manuf_name
        if update:
            self.update()
        else:
            self.refresh()

    def refresh(self, manuf_name=None):
        if not manuf_name:
            manuf_name = self._manuf_name
        try:
            with io.open('/home/www/hiyoutest/webapp/webapp/manuf/manuf', "r", encoding="utf-8") as read_file:
                manuf_file = StringIO(read_file.read())
                print(read_file)
        except Exception, e:
            print(e)
        self._masks = {}
        for line in manuf_file:
            com = line.split("#", 1)
            arr = com[0].split()

            if len(arr) < 1:
                continue

            parts = arr[0].split("/")
            mac_str = self._strip_mac(parts[0])
            mac_int = self._get_mac_int(mac_str)
            mask = self._bits_left(mac_str)

            if len(parts) > 1:
                mask_spec = 48 - int(parts[1])
                if mask_spec > mask:
                    mask = mask_spec

            if len(com) > 1:
                result = Vendor(manuf=arr[1], comment=com[1].strip())
            else:
                result = Vendor(manuf=arr[1], comment=None)

            self._masks[(mask, mac_int >> mask)] = result
        manuf_file.close()

    def update(self, manuf_url=None, manuf_name=None, refresh=True):
        if not manuf_url:
            manuf_url = self.MANUF_URL
        if not manuf_name:
            manuf_name = self._manuf_name

      
        try:
            response = urlopen(manuf_url)
        except URLError:
            raise URLError("Failed downloading OUI database")

       
        if response.code is 200:
            with open(manuf_name, "wb") as write_file:
                write_file.write(response.read())
            if refresh:
                self.refresh(manuf_name)
        else:
            err = "{0} {1}".format(response.code, response.msg)
            raise URLError("Failed downloading database: {0}".format(err))

        response.close()

    def search(self, mac, maximum=1):

        vendors = []
        if maximum <= 0:
            return vendors
        mac_str = self._strip_mac(mac)
        mac_int = self._get_mac_int(mac_str)

        # If the user only gave us X bits, check X bits. No partial matching!
        for mask in range(self._bits_left(mac_str), 48):
            result = self._masks.get((mask, mac_int >> mask))
            if result:
                vendors.append(result)
                if len(vendors) >= maximum:
                    break
        return vendors

    def get_all(self, mac):

        vendors = self.search(mac)
        if len(vendors) == 0:
            return Vendor(manuf=None, comment=None)
        return vendors[0]

    def get_manuf(self, mac):

        return self.get_all(mac).manuf

    def get_comment(self, mac):

        return self.get_all(mac).comment

    # Gets the integer representation of a stripped mac string
    def _get_mac_int(self, mac_str):
        try:
            # Fill in missing bits with zeroes
            return int(mac_str, 16) << self._bits_left(mac_str)
        except ValueError:
            raise ValueError("Could not parse MAC: {0}".format(mac_str))

    # Regular expression that matches '-', ':', and '.' characters
    _pattern = re.compile(r"[-:\.]")

    # Strips the MAC address of '-', ':', and '.' characters
    def _strip_mac(self, mac):
        return self._pattern.sub("", mac)

    # Gets the number of bits left in a mac string
    @staticmethod
    def _bits_left(mac_str):
        return 48 - 4 * len(mac_str)

def main():
    """Simple command line wrapping for MacParser."""
    argparser = argparse.ArgumentParser(description="Parser utility for Wireshark's OUI database.")
    argparser.add_argument('-m', "--manuf",
                           help="manuf file path. Defaults to manuf in same directory",
                           action="store")
    argparser.add_argument("-u", "--update",
                           help="update manuf file from the internet",
                           action="store_true")
    argparser.add_argument("mac_address", nargs='?', help="MAC address to check")

    args = argparser.parse_args()
    if args.manuf:
        parser = MacParser(manuf_name=args.manuf, update=args.update)
    else:
        parser = MacParser(update=args.update)

    if args.mac_address:
        print(parser.get_all(args.mac_address))

    sys.exit(0)

if __name__ == "__main__":
    main()
