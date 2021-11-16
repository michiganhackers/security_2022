# Baby Groot
## Contributors
Anisha Aggarwal

## Categories:
Forensics

## Description
Can you find the flag with only this image?

## Idea:
The idea behind this challenge is to hide the flag within the image using basic steganography techniques.
To hide the flag I simply created a text file called flag.txt which contained the flag and appended it to the
image file using the following command: `cat flag.txt >> babygroot.jpg`

## Solution:
There are a couple ways to go about finding the flag.

1. Open up the image in notepad and search for "MHCTF{" (or scroll all the way to the bottom) to find the 
contents of flag.txt appended to the image file.

2. Running `strings babygroot.jpg | grep "MHCTF{"` turns the image into strings and then only 
displays strings that contain "MHCTF{".

## Flag
MHCTF{i_am_groot}
