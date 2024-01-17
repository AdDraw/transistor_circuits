# Transistor theory

Mobility of holes i 2/3 times lower than electrons.

- Beta of PMOS sometimes should be adjusted to get unskewed gates(but it's not necessary since adjustments will result in wider Ts)
- PMOS of same W/L should be slower than NMOS

## Loose truths(at some technology node)

- Longer channel -> Less Current (lower I)
- Longer channel -> slower speed(longer path for carriers to traverse)
- Wider channel -> more current(Bigger I)

## Carriers

- "things" that carry charge
- transport charge in a transistor
- go through the channel
- 2 types:
  - electrons - carry negative charge
  - holes - carry positive charge

## Channel

- formed when VG > VT (kinda) and carriers flow from source under the gate

## Weak Inversion

- when space under the gate is partially filled with carriers but not fully
- substrate

## Inversion

- in case of the NMOS transistor where holes of the substrate are pushed deeper into the substrate under the force of the electric field applied from the gate and carriers from the source/drain flow under the gate
- inversion of polarity,
  - pre inversion - polarity is dominated by substrate's  majority charge(in case of doping it's either that there is more electrons or holes)
  - depletion - electric field pushes holes/electrons from under the gate deeper into the substrate
    - with rising Gate fied, more and more substrate "carriers" are pushed into the substrate
    - depletion - no carriers are present from the source but all charge has been pushed deeper into the substrate forming a depleted region
  - when nearing VT, more and more carriers from the source are attracted under the gate
    - at VT, cahnnel is created because polarity has been inverted, carriers fully cover the space under the gate

## Parameters

Na -
tox - gate oxide thickness
ni
Vt - threshold voltage
vt - thermal potential(usually 27e-6)
Vt0 - Vt at Vsb zero
y - body effect coeff
Cox - Oxide gate capactiance per width and unitary length
eox -
esi -
e0 -

## Body Effect

Due to nonzero Body potential -> Vsb is also nonzero, which means that `Vgs` = `Vg - (Vs+Vb)`, which means that to get past Vt, higher Vg has to be applied -> Vsb that is nonzero raises the Vt effective, this basically means that carriers are pulled into the source more thus to pull them back under the gate more force has to be present(in simple words)