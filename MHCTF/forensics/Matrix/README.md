# Matrix
## Contributors
Anisha Aggarwal

## Categories:
Forensics

## Description
Can you find the flag with only this image?

## Idea:
The idea behind this challenge is to hide the flag within the image using steganography techniques.
To hide the flag I simply chose the image I wanted and used exiftool to edit the metadata. I ran 
`exiftool -DocumentID="MHCTF{red_or_blue_pill}" matrix.jpg` to change the value of the DocumentID field in 
the image metadata to contain the flag.

## Solution:
To find the flag:

1. Run `exiftool matrix.jpg` to view the metadata and see that the DocumentID field contains the flag

## Flag
MHCTF{red_or_blue_pill}
