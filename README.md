# CMOS Circuits

Some Transistor Gates + Implementation for deepening my knowledge about transistor gates.

## NOT/INV

```math
Q = \overline{A}
```

### Truth Table

| A | Q |
| - | - |
| 0 | 1 |
| 1 | 0 |

### Transistor Implementation

![img](circuits_visual/inv.drawio.svg)

> there exist alternative implementations of the NOT gate / Inverter gate but this is the smallest in size(and probably also the fastest), other implementations use NAND or NOR gates that have both gate inputs tied to the same driver, this is because both NAND, NOR or XNOR gates are naturally inverting.

## Buffer

```math
  Q = A
```

### Truth Table

| A | Q |
| - | - |
| 0 | 0 |
| 1 | 1 |

### Transistor Implementation

![i](circuits_visual/buf.drawio.svg)

> 2 inverters back to back, in the end Output is equal to the input, regeneration of the signal happens because output is taken straight from the power rails(VDD/VSS) rather then the input

## OR2

```math
Q = A \lor B = A + B
```

### Truth Table

| A | B | Q |
| - | - | - |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### Karneugh net

| A\B | 0 | 1 |
| :-: | - | - |
|  0  | 0 | 1 |
|  1  | 1 | 1 |

## NOR2

```math
Q = \overline{A \lor B} = \overline{A + B}
```

### Truth Table

| A | B | Q |
| - | - | - |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

### Karneugh net

| A\B | 0 | 1 |
| :-: | - | - |
|  0  | 1 | 0 |
|  1  | 0 | 0 |

## XOR2

```math
  XOR(A,B) = A \oplus B = (A \land \overline{B}) \lor (\overline{A} \land B) = (A \lor B ) \land (\overline{A} \lor \overline{B})
```

> Inverted EQUALITY checker, if inputs are not the same then return True

### Truth Table

| A | B | Q |
| - | - | - |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### Karneugh net

| A\B | 0 | 1 |
| :-: | - | - |
|  0  | 0 | 1 |
|  1  | 1 | 0 |

- sum of products = $B \sdot \overline{A} + A \sdot \overline{B}$
- product of sums = $A+B \sdot \overline{A} + \overline{B}$

### Transistor Implementation

#### NAND2 only implementation(no inverters)

```math
\overline{\overline{A \sdot (\overline{A \sdot B})} \sdot \overline{B \sdot (\overline{A \sdot B})}}
```

Achieved through:

```math
XOR(A,B) = (\overline{A} \sdot B) + (\overline{B} \sdot A) = \overline{\overline{(\overline{A} \sdot B)} \sdot \overline{(\overline{B} \sdot A)}}
= \overline{\overline{(\overline{A \sdot B} \sdot B)} \sdot \overline{(\overline{B \sdot A} \sdot A)}} \\

\text{legend: } \\

\overline{A} \sdot B = B \sdot \overline{A} + B \sdot \overline{B} = B \sdot (\overline{B} + \overline{A}) = B \sdot (\overline{B} + \overline{A}) = B \sdot \overline{B \sdot A} \text{ ; } B \sdot \overline{B} = 0 \\

\overline{B} \sdot A = A \sdot \overline{B} + A \sdot \overline{A} = A \sdot (\overline{B} + \overline{A}) = A \sdot (\overline{B} + \overline{A}) = A \sdot \overline{B \sdot A} \text{ ; } A \sdot \overline{A} = 0

```

![xor.drawio.svg](circuits_visual/xor.drawio.svg)

> Size: 16 transistors = 4 x NAND2 = 4 x 4 = 16

#### NOR2 only implementation

```math
XOR(A,B) = (\overline{A} \sdot B) + (\overline{B} \sdot A) =  \overline{A + \overline{A + B}} + \overline{B + \overline{A + B}} = \overline{\overline{\overline{A + \overline{A + B}} + \overline{B + \overline{A + B}}}} = \overline{\overline{\overline{A + \overline{A + B}} + \overline{B + \overline{A + B}}}} = \overline{(\overline{\overline{A + \overline{A + B}} + \overline{B + \overline{A + B}}}) + (\overline{\overline{A + \overline{A + B}} + \overline{B + \overline{A + B}}})}\\
\text{legend: } \\
\overline{A} \sdot B = \overline{A} \sdot B + A \sdot \overline{A} = \overline{A}(A + B) = \overline{A + \overline{A + B}} \\
A \sdot \overline{B} = A \sdot \overline{B} + B \sdot \overline{B} = \overline{B}(A + B) = \overline{B + \overline{A + B}} \\
\overline{a} = \overline{a + a} \text{ ; } a = a + a
```

![xor_nor.drawio.svg](circuits_visual/xor_nor2.drawio.svg)

> Size: 20 transistors = 5 x NOR2 = 5 x 4 = 20

#### NOR + NAND implementation

```math
XOR(A,B) = (A \lor B ) \land (\overline{A} \lor \overline{B}) = \overline{\overline{A \lor B} \lor \overline{\overline{A} \lor \overline{B}}} = \overline{\overline{\overline{A} \land \overline{B}} \lor \overline{\overline{A \land B}}}
```

![xor2_mixed.drawio.svg](circuits_visual/xor2_mixed.drawio.svg)

> size: 20 transistors = 2 x NAND2 + 4 x NOT + 1 x NOR2 = 2 x 4 + 4 x 2 + 1 x 4 = 20

### XOR Transistor Implementation

To generate a XOR we will get:

```math
\text{Simple implementation (a)}:
\text{} \\
\text{XOR but CMOS logic is inverting this means that logic in the PDN has} \\
\text{to be the inversion of the inversion of the XOR to get a XOR and not XNOR at the output} \\
\text{that means that we have to implement a XNOR logic to the PDN to get a XOR at the output }
\\
XNOR = (A * B) + (\bar{A} * \bar{B}), \text{ when implementing this in the PDN we will get } \bar{XNOR} = XOR \\
PDN = \overline{(A * B) + (\overline{A} * \overline{B})}\\
\text{PUN can be achieved applying De Morgan's Law to the PDN logic equation } \\
PUN = DeMorgan(PDN) = \overline{ \overline{ \overline{(A * B)} * \overline{(\overline{A} * \overline{B})} } } = \overline{(A * B)} * \overline{(\overline{A} * \overline{B})} = (\overline{A} + \overline{B}) * \overline{\overline{A + B}} = (\overline{A} + \overline{B}) * (A + B)
\\ \text{}
\\ \text{Transistor optimal implementation b)}
\\ \text{In this case since XOR logic is double rail logic, inputs and inverted inputs have to be provided}
\\ \text{that means that PUN logic can be written kinda hackypacky}
\\ \text{PUN} = (A \sdot \overline{B}) + (\overline{A} \sdot B)
\\ \text{PDN} = \overline{XOR} = XNOR = (A \sdot B) + (\overline{A} \sdot \overline {B})
\\ \text{Only real requirement is that PUN and PDN logic is not active at the same time, since PUN drives 1 and PDN drives 0 we can take XOR PUN or PDN not as DEMorgan's computed equivalents but as 2 separate equations}
\\ \text{Option B is better because ??? less Drain capacitance ?? Easier to route?}
```

![xor_tran.drawio.svg](circuits_visuals/../circuits_visual/xor_tran.drawio.svg)

> size: 12 transistors = 1x8 + 2xNOT = 1x8 + 2x2 = 12

Schematic a) is created as if $\text{PDN} = \overline{\overline{XOR}} = \overline{XNOR(A,B)} = (A \sdot B) + (\overline{A} \sdot \overline {B})$ and PUN if we were to create a complementary PUN it would be equal to $\text{PUN} = XOR = (A + B) \sdot (\overline{A} + \overline {B})$. On the other hand b) represents XOR but PUN is taken from usual XOR equation as a sum of products. Logic checks out in b) because all 4 states of input values are covered and are not overlapping.

> Going from a) to b) could be imagined as untwisting a)'s PUN.

## XNOR2

> EQUALITY checker, if inputs are the same return True

### Truth Table

| A | B | Q |
| - | - | - |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### Karneugh net

| A\B | 0 | 1 |
| :-: | - | - |
|  0  | 1 | 0 |
|  1  | 0 | 1 |

## AND2

```math
AND(A,B) = A \land B = A \sdot B
```

### Truth Table

| A | B | Q |
| - | - | - |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## NAND2

```math
NAND2(A,B) = \overline{A \land B} = \overline{A \sdot B}
```

### Truth Table

| A | B | Q |
| - | - | - |
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### Gate Implementation

![nand2.drawio.svg](circuits_visual/nand2.drawio.svg)

### Transistor Implementation

## NAND3

```math
NAND3(A,B,C) = \overline{A \land B \land C} = \overline{A \sdot B \sdot C}
```

### Truth Table

| A | B | C | Q |
| - | - | - | - |
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

### Karneugh Net

| AB\C | 0 | 1 |
| :--: | - | - |
|  00  | 1 | 1 |
|  01  | 1 | 1 |
|  11  | 1 | 0 |
|  10  | 1 | 1 |

## XOR3

```math
XOR3(A,B,C) = \overline{A}\overline{B}C + A\overline{B}\overline{C} + \overline{A}B\overline{C} + ABC
```

### Truth Table

| A | B | C | Q |
| - | - | - | - |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

### Karneugh Net

| AB\C | 0 | 1 |
| :--: | - | - |
|  00  | 0 | 1 |
|  01  | 1 | 0 |
|  11  | 0 | 1 |
|  10  | 1 | 0 |

### Transistor Implementation

```math
XOR3(A,B,C)= \overline{A}\overline{B}C + A\overline{B}\overline{C} + \overline{A}B\overline{C} + ABC \\
\text{To make it into a PDN and PUN representation, we need to find the invert of this function to easily implemnent PDN}\\
\text{First: Take your XOR function and double invert it so } Y=\overline{\overline{Y}} \\
\overline{A}\overline{B}C + A\overline{B}\overline{C} + \overline{A}B\overline{C} + ABC = \overline{\overline{\overline{A}\overline{B}C + A\overline{B}\overline{C} + \overline{A}B\overline{C} + ABC}} \\
\text{Second: Take the }\overline{Y}\text{ and apply DeMorgan's Laws to eventually not have groups of inputs inverted together, ex. }\overline{(AB)}\text{ has to be avoided} \\
\overline{\overline{\overline{A}\overline{B}C} \sdot \overline{A\overline{B}\overline{C}} \sdot \overline{\overline{A}B\overline{C}} \sdot \overline{ABC}} = \overline{\overline{\overline{A+B}C} \sdot \overline{\overline{A+C}B} \sdot \overline{\overline{B+C}A} \sdot \overline{\overline{\overline{A}+\overline{B}}C}} = \\ \overline{(A+B+\overline{C}) \sdot (A+\overline{B}+C) \sdot (\overline{A}+B+C) \sdot (\overline{A}+\overline{B} + \overline{C})} \\
\text{Lastly: Having a }\overline{Y}\text{ XOR3 representation we can implement PDN and get PUN}

```

![XOR3](circuits_visual/xor3.drawio.svg "XOR3")
