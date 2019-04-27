# ctf-usb-keyboard-parser

This is the updated script from https://teamrocketist.github.io/2017/08/29/Forensics-Hackit-2017-USB-ducker/

### Usage
```bash
$ python usbkeyboard.py <file>
```

### Extract file from pcap (might not work for every pcap)
```bash
$ tshark -r ./usb.pcap -Y 'usb.capdata' -T fields -e usb.capdata > usbPcapData
```
