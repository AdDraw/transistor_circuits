# CMOS Circuits

## Buffer

```math
  Q = A
```

### Truth Table

| A | Q |
| - | - |
| 0 | 0 |
| 1 | 1 |

## NOT/INV

```math
Q = \overline{A}
```

### Truth Table

| A | Q |
| - | - |
| 0 | 1 |
| 1 | 0 |

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

This means that:

- sum of products = `B * A_bar + A*B_bar`
- product of sums = `(A+B) * (A_bar + B_bar)`

#### NAND only Implementation

```math
\overline{\overline{A \sdot (\overline{A \sdot B})} \sdot \overline{B \sdot (\overline{A \sdot B})}}
```

Achieved through:

```math
XOR(A,B) = (\overline{A} \sdot B) + (\overline{B} \sdot A) = \overline{\overline{(\overline{A} \sdot B)} \sdot \overline{(\overline{B} \sdot A)}} = \\
= \overline{\overline{(\overline{A \sdot B} \sdot B)} \sdot \overline{(\overline{B \sdot A} \sdot A)}} \\

\overline{A} \sdot B = B \sdot \overline{A} + B \sdot \overline{B} = B \sdot (\overline{B} + \overline{A}) \\
B \sdot (\overline{B} + \overline{A}) = B \sdot \overline{B \sdot A} \\
B \sdot \overline{B} = 0 \\

\overline{B} \sdot A = A \sdot \overline{B} + A \sdot \overline{A} = A \sdot (\overline{B} + \overline{A}) \\
A \sdot (\overline{B} + \overline{A}) = A \sdot \overline{B \sdot A} \\
A \sdot \overline{A} = 0

```

![xor.svg](circuits_visual/xor.svg)

#### impl2

## XNOR2

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

![nand2.svg](circuits_visual/nand2.svg)

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
| :-:  | - | - |
|  00  | 1 | 1 |
|  01  | 1 | 1 |
|  10  | 1 | 1 |
|  11  | 1 | 0 |
