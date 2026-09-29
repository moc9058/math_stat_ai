(c) $\Rightarrow$ (a): Suppose $L$ is continuous at $h_0$ and $h$ is any point in $\mathcal H$. If $h_n\to h$ in $\mathcal H$, then $h_n-h+h_0\to h_0$. By assumption,
$L(h_0)=\lim[L(h_n-h+h_0)]=\lim[L(h_n)-L(h)+L(h_0)]=\lim L(h_n)-L(h)+L(h_0)$. Hence $L(h)=\lim L(h_n)$.

(b) $\Rightarrow$ (d): The definition of continuity at $0$ implies that $L^{-1}(\{\alpha\in\mathbb F:|\alpha|<1\})$ contains an open ball about $0$. So there is a $\delta>0$ such that $B(0;\delta)\subseteq L^{-1}(\{\alpha\in\mathbb F:|\alpha|<1\})$. That is, $\|h\|<\delta$ implies $|L(h)|<1$. If $h$ is an arbitrary element of $\mathcal H$ and $\varepsilon>0$, then $\|\delta(\|h\|+\varepsilon)^{-1}h\|<\delta$. Hence

$$
1>\left|L\left[\frac{\delta h}{\|h\|+\varepsilon}\right]\right|
=\frac{\delta}{\|h\|+\varepsilon}|L(h)|;
$$

thus

$$
|L(h)|<\frac{1}{\delta}(\|h\|+\varepsilon).
$$

Letting $\varepsilon\to0$ we see that (d) holds with $c=1/\delta$. $\blacksquare$

**3.2. Definition.** A *bounded linear functional* $L$ on $\mathcal H$ is a linear functional for which there is a constant $c>0$ such that $|L(h)|\leqslant c\|h\|$ for all $h$ in $\mathcal H$. In light of the preceding proposition, a linear functional is bounded if and only if it is continuous.

For a bounded linear functional $L:\mathcal H\to\mathbb F$, define

$$
\|L\|=\sup\{|L(h)|:\|h\|\leqslant1\}.
$$

Note that by definition, $\|L\|<\infty$; $\|L\|$ is called the *norm* of $L$.

**3.3. Proposition.** *If $L$ is a bounded linear functional, then*

$$
\begin{aligned}
\|L\|&=\sup\{|L(h)|:\|h\|=1\}\\
&=\sup\{|L(h)|/\|h\|:h\in\mathcal H,\ h\ne0\}\\
&=\inf\{c>0:|L(h)|\leqslant c\|h\|,\ h\text{ in }\mathcal H\}.
\end{aligned}
$$

*Also, $|L(h)|\leqslant\|L\|\|h\|$ for every $h$ in $\mathcal H$.*

**Proof.** Let $\alpha=\inf\{c>0:|L(h)|\leqslant c\|h\|,\ h\text{ in }\mathcal H\}$. It will be shown that $\|L\|=\alpha$; the remaining equalities are left as an exercise. If $\varepsilon>0$, then the definition of $\|L\|$ shows that $|L((\|h\|+\varepsilon)^{-1}h)|\leqslant\|L\|$. Hence $|L(h)|\leqslant\|L\|(\|h\|+\varepsilon)$. Letting $\varepsilon\to0$ shows that $|L(h)|\leqslant\|L\|\|h\|$ for all $h$. So the definition of $\alpha$ shows that $\alpha\leqslant\|L\|$. On the other hand, if $|L(h)|\leqslant c\|h\|$ for all $h$, then $\|L\|\leqslant c$. Hence $\|L\|\leqslant\alpha$. $\blacksquare$

Fix an $h_0$ in $\mathcal H$ and define $L:\mathcal H\to\mathbb F$ by $L(h)=\langle h,h_0\rangle$. It is easy to see that $L$ is linear. Also, the CBS inequality gives that $|L(h)|=|\langle h,h_0\rangle|\leqslant\|h\|\|h_0\|$. So $L$ is bounded and $\|L\|\leqslant\|h_0\|$. In fact, $L(h_0/\|h_0\|)=\langle h_0/\|h_0\|,h_0\rangle=\|h_0\|$, so that $\|L\|=\|h_0\|$. The main result of this section provides a converse to these observations.
