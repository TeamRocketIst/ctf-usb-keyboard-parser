#!/usr/bin/env python

import unittest
from usbkeyboard import read_use

inputs = "ctf_inputs/inputs/"
outputs = "ctf_inputs/outputs/"

class UsbTestCase(unittest.TestCase):

    def test_bsidessf2019_theKey(self):
        name = "bsidessf2019_theKey"
        with open(outputs+name+'.out', 'r') as f:
            self.assertEqual(read_use(inputs+name), f.read())

    def test_hackit2017_usbDucker(self):
        name = "hackit2017_usbDucker"
        with open(outputs+name+'.out', 'r') as f:
            self.assertEqual(read_use(inputs+name), f.read())

    def test_picoctf2017_justKeypTrying(self):
        name = "picoctf2017_justKeypTrying"
        with open(outputs+name+'.out', 'r') as f:
            self.assertEqual(read_use(inputs+name), f.read())

    def test_sha2017_abuseMail(self):
        name = "sha2017_abuseMail"
        with open(outputs+name+'.out', 'r') as f:
            self.assertEqual(read_use(inputs+name), f.read())

    def test_icectf2016_interceptedPartOne(self):
        name = "icectf2016_interceptedPartOne"
        with open(outputs+name+'.out', 'r') as f:
            self.assertEqual(read_use(inputs+name), f.read())

    def test_hacktm2020_strangePcap(self):
        name = "hacktm2020_strangePcap"
        with open(outputs+name+'.out', 'r') as f:
            self.assertEqual(read_use(inputs+name), f.read())

    def test_unknownCtf2020_unknownChallenge(self):
       name = "unknownCtf2020_unknownChallenge"
       with open(outputs+name+'.out', 'r') as f:
            self.assertEqual(read_use(inputs+name), f.read())

    def test_rgbctf2020_PI_1_MagicInTheAir(self):
       name = "rgbctf2020_PI_1_MagicInTheAir"
       with open(outputs+name+'.out', 'r') as f:
            self.assertEqual(read_use(inputs+name), f.read())

    def test_volgactf2021_stream(self):
       name = "volgactf2021_stream"
       with open(outputs+name+'.out', 'r') as f:
            self.assertEqual(read_use(inputs+name), f.read())

def main():
    unittest.main()

if __name__ == "__main__":
    main()
