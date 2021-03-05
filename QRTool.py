"""
Created on Mon Mar 01 2021

@author: Amber 
@description: 
This source code took from multiple online sources.
and QRTool is an Open Source Library to scan the QR code
"""


# Enable the code based on requirement
#DECODER

#import qrtools
qr = qrtools.QR()
data='name.png'
qr.decode(data)
print qr.data
