# How to pronounce GIF
*Forensics* - *Easy* - *100 points*
## Flag
DUCTF{aM_1_haXX0r_n0w?}

## Solution
After reading the problem context and seeing the GIF, it's clear that the GIF contains QR codes. The first issue
is extracting the QR codes from the GIF, which was accomplished by using an online tool that extracts frames
from GIFs. The next step was putting together each slice of the QR codes together, which ultimately revealed 10 
unique QR codes. After scanning them all, the two most interesting/suspicious are QR6 and QR8, with QR8 looking like a base64 encoded string. Intuition says to concatenate the two related strings and decode, which
successfully reveals the flag.

QR6 contains the string: RFVDVEZ7YU1

QR8 contains the string: fMV9oYVhYMHJfbjB3P30=

Together they form the base64 encoded string: RFVDVEZ7YU1fMV9oYVhYMHJfbjB3P30=

Decoding the string results in the flag: DUCTF{aM_1_haXX0r_n0w?}

## Notes
This challenge was relatively easy, just tedious when reconstructing the QR codes. It would have been better
with fewer QR codes or more QR codes that weren't split up.