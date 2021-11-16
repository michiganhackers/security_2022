# Ironman
## Contributors
Anisha Aggarwal

## Categories:
Forensics

## Description
Can you find the flag with only this image?

## Idea:
The idea behind this challenge is to hide the flag within the image using basic steganography techniques.
To hide the flag I simply created a text file called flag.txt which contained the flag and compressed it 
into a zip file. I then appended the zip file to the image file using the following command: 
`cat flag.txt >> babygroot.jpg`

## Solution:
To find the flag:

1. Open up the image in notepad and scroll all the way to the bottom to see signs that a zip file was added OR
run `binwalk -b ironman.jpg` to see that this is a jpg file with a zip file within

2. Run `binwalk -e ironman.jpg` which will extract the contents of the image into a new folder. You will then 
find flag.txt within the extracted folder.

## Flag
MHCTF{have_you_ever_tried_shwarma}
