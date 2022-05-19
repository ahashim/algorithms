# 🧮 Critter Algorithms

### Virality

Given the properties of a squeak being the number of likes $\large L$, the
number of dislikes $\large D$, and the number of resqueaks $\large R$, we can
calculate the order of virality $\large \vartheta$ with the formula

$$
    \large
    \begin{array}{c}
      \vartheta \ = \ \sqrt{\frac{L}{D}} \
      \times \
      \log{(L \ + \ D)} \
      \times \
      \log{R}
    \end{array}
$$

where the coefficient of virality $\large k\in\lbrace 0, \frac{1}{\vartheta} \rbrace$

$$
    \large
    \begin{array}{c}
      k \ = \ \begin{cases}
        0 &\text{if } \vartheta \ = \ 0 \\
        \frac{1}{\vartheta} &\text{if } \vartheta \ > \ 0
      \end{cases}
    \end{array}
$$

and the number of blocks elapsed since publishing the squeak $\large x$, we have the
full virality formula $V$ which only applies to squeaks with at least one like
$\large L$ and and one resqueak $\large R$:

$$
    \large
    \begin{array}{c}
      V \ = \ \begin{cases}
        \frac{1}{x \ + \ k} &\text{if } L \ > \ 0 \ \And R \ > \ 0 \\
        \frac{0}{x} &\text{otherwise}
      \end{cases}
    \end{array}
$$
