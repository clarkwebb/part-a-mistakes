#import "@preview/physica:0.9.4": *
#import "@preview/unify:0.7.1": *
#import "@preview/codly:1.3.0": *

#let title = [
  Silly mistakes in Part A
]
#let today = datetime.today()
#let codeblock(filename) = raw(read(filename), block: true, lang: filename.split(".").at(-1))

#show: codly-init
#codly(number-format: numbering.with("1"))

#set page(
  paper: "us-letter",
  numbering: "1",
)
#set par(
  justify: true,
)
#set text(
  font: "New Computer Modern",
  size: 11pt,
)
#set math.equation(numbering: it => {
  numbering("(1)", it)
})

#show heading.where(level: 1): set text(
  font: "New Computer Modern Sans",
  size: 16pt,
  weight: "bold",
)
#show heading.where(level: 2): set text(
  font: "New Computer Modern Sans",
  size: 13pt,
  weight: "bold",
)
#show heading: set heading(numbering: "1.")
#show bibliography: set heading(numbering: none)
#show figure: set block(breakable: true)

#place(
  top + center,
  float: true,
  scope: "parent",
  clearance: 2em,
)[
  #align(
  center,
  text(font: "New Computer Modern Sans", 19pt)[
    *#title*
    ]
  )

  Mia Clark-Webb et al.\
  #today.display("[day] [month repr:long] [year]")
  
]

= General advice
- If the question gives you an approximation, use it!
- Read the question carefully and think about what solution you want to obtain before starting complicated maths.

= Electromagnetism
- The magnetic field outside an object is not just the external field. Remember that the object changes the field as well.

= Quantum mechanics
- Don't forget to square when normalising a state, and don't forget to normalise in the first place.
- $0 dot 1$ is not $1$ (for example, in $j(j+1)$).
- Don't forget how to take the determinant of a $3 times 3$ matrix:
$ mat(delim: "|", a, b, c; d, e, f; g, h, i)
= a mat(delim: "|", e, f; h, i)
- b mat(delim: "|", d, f; g, i)
+ c mat(delim: "|", d, e; g, h) text(".") $

- Don't get the signs the wrong way round for perturbation theory. The signs in the denominator are always such that the second-order correction to the ground state energy is non-positive, and the order in the numerator is the other way round.
  That is,
$ ket(delta psi_0^((1))) &= sum_(n=1)^infinity braket(n, hat(H), 0)/(E_0 - E_n) ket(n) text(",") \
delta E_0^((2)) &= sum_(n=1)^infinity (lr(|braket(n, hat(H), 0)|)^2)/(E_0-E_n) <= 0 text(".") $

- Don't forget the $1\/2m$ factor in the Hamiltonian. It should be $-hbar^2\/2m$.
- $Delta x Delta p$ is not $<=hbar\/2$.
$ Delta x Delta p >= hbar /2 text(".") $

- The ground state is not zero energy.
- For spin-symmetric fermions, the fact that $ket(00)$ doesn't exist doesn't mean that there is no ground state.
  Instead, the ground state is $ket(01)$ or $ket(10)$.

= Miscellaneous
- $upright(e)^0 = 1$, not $0$.