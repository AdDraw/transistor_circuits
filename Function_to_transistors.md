

If you have a function `Y = X` and you want to represent it as a gate in CMOS then you can:

CMOS gate characteristics:

- naturally inverting
  - NMOS transistors in the PDN are active HIGH but pull the output to LOW (inversion)
    - HIGH = LOW -> HIGH = ~HIGH -> inversion
  - PMOS transistors in PUN are active LOW but pull the output to HIGH
    - LOW = HIGH -> LOW = ~LOW -> inversion
  - This is because, NMOS cannot pull to VDD, they pass a weak '1'
    - On the other hand, PMOS cannot fully pull to GND, they pass a 'weak' 0

This is because, if we look at a NMOS transistor that has Source and Gate tied to VDD, then VGS at some point won't be bigger than VT and at this point where VGS >= VT, then channel no longer will be formed, this is why NMOS transistors cannot be used in the PUN. Same can be said about PMOSes in PDN.
