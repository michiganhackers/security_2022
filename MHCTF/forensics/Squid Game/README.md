# Squid Game
## Contributors
Anisha Aggarwal

## Categories:
Forensics

## Description
Oh no! My friend was trying to send me their Netflix password, but accidently sent me a broken file.
No they are on vacation and I really need to binge Squid Game! Can you help me find the password?

## Idea:
The idea behind this challenge is to hide the flag within the image using file format knowledge.
To hide the flag I simply created a pdf file that contains the password and then changed the file extension 
from ".pdf" to ".jpg", essentially "breaking" it.

## Solution:
To find the flag:

1. Using a binary editor or opening the ifle in notepad allows you to see the file signature (indicating that 
this file is actually a pdf and not jpg file). Running `binwalk -b world_map.jpg` accomplishes the same thing.

2. Next, just change the extension from ".jpg" back to ".pdf", open up the file, and find the flag!

## Flag
MHCTF{$qu1dG@m3!}
