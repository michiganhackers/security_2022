# Halloween Costume
## Contributors
Kipras Januska
Abbie Tooman
Jiye Choi

## Flag

MHCTF{astronaut}

## Idea

To use multiple encryption methods to encode one string.

## Solution

Decode the string using a Vigenere cipher with the keyphrase "boo". Then decode the resulting string using a shift cipher with a key of 6.
