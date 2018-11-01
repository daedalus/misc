#!/usr/bin/env python
# Author Dario Clavijo 2018

#http://www.file-recovery.com/jpg-signature-format.htm
#typedef struct _JFIFHeader
#{
#  BYTE SOI[2];          /* 00h  Start of Image Marker     */
#  BYTE APP0[2];         /* 02h  Application Use Marker    */
#  BYTE Length[2];       /* 04h  Length of APP0 Field      */
#  BYTE Identifier[5];   /* 06h  "JFIF" (zero terminated) Id String */
#  BYTE Version[2];      /* 07h  JFIF Format Revision      */
#  BYTE Units;           /* 09h  Units used for Resolution */
#  BYTE Xdensity[2];     /* 0Ah  Horizontal Resolution     */
#  BYTE Ydensity[2];     /* 0Ch  Vertical Resolution       */
#  BYTE XThumbnail;      /* 0Eh  Horizontal Pixel Count    */
#  BYTE YThumbnail;      /* 0Fh  Vertical Pixel Count      */
#} JFIFHEAD;

#https://en.wikipedia.org/wiki/JPEG#JPEG_files
#'Short name'  'Bytes'   'Payload' 'Name'
#'SOI',0xFF,0xD8,'none', 'Start Of Image'  
#'SOF0',0xFF, 0xC0,'variable size','Start Of Frame (baseline DCT)   Indicates that this is a baseline DCT-based JPEG, and specifies the width, height, number of components, and component subsampling (e.g., 4:2:0).'
#'SOF2',0xFF,0xC2,'variable size','Start Of Frame (progressive DCT)    Indicates that this is a progressive DCT-based JPEG, and specifies the width, height, number of components, and component subsampling (e.g., 4:2:0).'
#'DHT' 0xFF, 0xC4,'variable size','Define Huffman Table(s) Specifies one or more Huffman tables.'
#'DQT' 0xFF, 0xDB,'variable size','Define Quantization Table(s)    Specifies one or more quantization tables.'
#'DRI' 0xFF, 0xDD,'4 bytes','Define Restart Interval Specifies the interval between RSTn markers, in Minimum Coded Units (MCUs). This marker is followed by two bytes indicating the fixed size so it can be treated like any other variable size segment.'
#'SOS' 0xFF, 0xDA,'variable size','Start Of Scan Begins a top-to-bottom scan of the image. In baseline DCT JPEG images, there is generally a single scan. Progressive DCT JPEG images usually contain multiple scans. This marker specifies which slice of data it will contain, and is immediately followed by entropy-coded data.'
#'RSTn',0xFF, '0xDn (n=0..7)', 'none','Restart Inserted every r macroblocks, where r is the restart interval set by a DRI marker. Not used if there was no DRI marker. The low three bits of the marker code cycle in value from 0 to 7.'
#'APPn',0xFF,0xEn,'variable size','Application-specific    For example, an Exif JPEG file uses an APP1 marker to store metadata, laid out in a structure based closely on TIFF.'
#'COM', 0xFF, 0xFE,'variable size','Comment Contains a text comment.'
#'EOI' ,0xFF, 0xD9,'none','End Of Image'    

import struct
import sys
import binascii

fp = open(sys.argv[1],"rb")
data = fp.read(20)
print "header hex:", binascii.hexlify(data)
header_fmt="@2s2sH5sBBBHHBB"
_JFIFHeader = struct.unpack(header_fmt,data)
SOI,APP0,Length,Identifier,Version_Maj,Version_Min,Units,Xdensity,Ydensity,XThumbnail,YThumbnail = _JFIFHeader
if SOI == '\xff\xd8':
    if APP0 == '\xff\xe0':
        print "APP0 Lenght:",Length
        print "Identifier:",Identifier
        print "Version: %d.%d" % (Version_Maj,Version_Min)
        print "Units:",Units
        print "XYdensity: %d,%d" %(Xdensity,Ydensity)
        print "Thumbnail: %d,%d" % (XThumbnail,YThumbnail)
    else:
        print "Bad APP0"
else:
    print "Bad SOI"

data = fp.read(4)
print binascii.hexlify(data)
if data[0] == '\xff': 
    #print hex(ord(data[1]))
    #& ord('\xf0')
    if (ord(data[1]) & ord('\xe0')) == ord('\xe0'): 
        data = fp.read(ord('\x0f') & ord(data[1]))
        print "Metadata:",data
        print fp.read(ord(data[3]))
