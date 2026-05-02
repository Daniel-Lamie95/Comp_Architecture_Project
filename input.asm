START, LOAD 5
ADD 3
STORE 10
OUTPUT
HALT
; --- injected invalid lines for testing
invlid_text_here
?!@@ malformed-instruction
MOV R0, #XYZ ; invalid immediate value
THIS_IS_NOT_ASM
