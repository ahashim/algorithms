# 🧮 Critter Algorithms

### Virality

Given the following properties of a squeak:

- number of likes
  $$
      \Large L
  $$
- number of dislikes
  $$
      \Large D
  $$
- number of resqueaks
  $$
      \Large R
  $$

we can calculate the order of virality $\vartheta$ with the formula

$$
    \large
    \begin{array}{c}
      \vartheta = \sqrt{\frac{L}{D}}
      \times
      \log{(L + D)}
      \times
      \log{R}
    \end{array}
$$

where the coefficient of virality $k\in\lbrace 0, \frac{1}{\vartheta} \rbrace$

$$
    \large
    \begin{array}{c}
      k = \begin{cases}
        0 &\text{if } \vartheta = 0 \\
        \frac{1}{\vartheta} &\text{if } \vartheta > 0
      \end{cases}
    \end{array}
$$

and the number of blocks elapsed since publishing the squeak $x$, we have the
full virality formula $V$ which only applies to squeaks with at least one like
$L$ and and one resqueak $R$:

$$
    \large
    \begin{array}{c}
      V = \begin{cases}
        \frac{1}{x + k} &\text{if } L > 0 \ \And R > 0 \\
        \frac{0}{x} &\text{otherwise}
      \end{cases}
    \end{array}
$$
