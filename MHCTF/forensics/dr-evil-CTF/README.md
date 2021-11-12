# Senior Photo MHCTF
##### by: Daniel Peacock

## Categories: 
Forensics / Cryptography
## Description:
Dr. Evil has stolen the flag from us! Can you solve this challenge to claim the flag back?

## Write-up:
Download the dr-evil folder, which contains password.txt, and dr-evil.jpg. 
Within password.txt, there seems to be an encoded message! You can easily decode the password by shifting the message ROT 13, which reveals the password. The password is password. How clever, Dr. Evil!

Next, we must work with the image of Dr. Evil to find the flag. In the command line, using the command 'steghide extract -sf dr-evil.jpg', and entering the password 'password' when prompted, you extract a zip file named 'not the flag.zip'. Hmmm. Dr. Evil must have put the flag in this zip file. 

Once you extract the contents of the zip, you have two new files, namely, 'not_a_jpeg.jpg' and 'f4ke_flag.txt'. Once you open 'f4ke_flag.txt', you find two interesting things. Oh look, A flag! Unfortunately, it's a dummy flag. However, you are given another password: 'mini_me'. Interesting.

Well we don't have the flag yet, but we have another jpeg. You can do a similar process with this jpeg to find the flag. Again in the command line, use the command 'steghige extract -sf not_a_jpeg.jpg', and enter 'mini_me' as the password, you extract a new file, 'flag.txt'. This has to be the flag!!

Opening flag.txt reveals the flag, 'MHCTF{sharks_with_frickin_laser_beams}'
## Flag:
MHCTF{sharks_with_frickin_laser_beams}
