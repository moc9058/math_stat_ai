**4.5. Proposition.** If $\mathcal A$ is a $C^*$-algebra and $I$ is an ideal of $\mathcal A$, then for every $a$ in $I$ there is a sequence $\{e_n\}$ of positive elements in $I$ such that:

(a) $e_1\leq e_2\leq\cdots$ and $\|e_n\|\leq 1$ for all $n$;  
(b) $\|ae_n-a\|\to 0$ as $n\to\infty$.

In the preceding proposition the sequence $\{e_n\}$ depends on the element $a$. It is also true that there is a positive increasing net $\{e_i\}$ in $I$ such that $\|e_i a-a\|\to 0$ and $\|ae_i-a\|\to 0$ for every $a$ in $I$ (see p. 36 of Arveson [1976]).

We turn now to an important consequence of Theorem 4.3.

**4.6. Theorem.** If $\mathcal A$ is a $C^*$-algebra and $I$ is a closed ideal of $\mathcal A$, then for each $a+I$ in $\mathcal A/I$ define $(a+I)^*=a^*+I$. Then $\mathcal A/I$ with its quotient norm is a $C^*$-algebra.

To prove (4.6), a lemma is needed.

**4.7. Lemma.** If $I$ is an ideal in a $C^*$-algebra $\mathcal A$ and $a\in\mathcal A$, then
$$
\|a+I\|=\inf\{\|a-ax\|:x\in I,\ x\geq 0,\text{ and }\|x\|\leq 1\}.
$$

**Proof.** If $(\operatorname{ball} I)_+=\{x\in\operatorname{ball} I:x\geq 0\}$, then clearly $\|a+I\|\leq\inf\{\|a-ax\|:x\in(\operatorname{ball} I)_+\}$ since $aI\subseteq I$. Let $y\in I$ and let $\{e_n\}$ be a sequence in $(\operatorname{ball} I)_+$ such that $\|y-ye_n\|\to 0$ as $n\to\infty$. Now $0\leq 1-e_n\leq 1$, so $\|(a+y)(1-e_n)\|\leq\|a+y\|$. Hence
$$
\begin{aligned}
\|a+y\|&\geq\liminf\|(a+y)(1-e_n)\|\\
&=\liminf\|(a-ae_n)+(y-ye_n)\|\\
&=\liminf\|a-ae_n\|
\end{aligned}
$$
since $\|y-ye_n\|\to 0$. Thus $\|a+y\|\geq\inf_n\|a-ae_n\|\geq\inf\{\|a-ax\|:x\in(\operatorname{ball} I)_+\}$. Taking the infimum over all $y$ in $I$ gives the desired remaining inequality. ■

**Proof of Theorem 4.6.** The only difficult part of this proof is to show that $\|a+I\|^2=\|a^*a+I\|$ for every $a$ in $\mathcal A$. Since $x^*\in I$ whenever $x\in I$ (4.3), $\|a^*+I\|=\|a+I\|$ for all $a$ in $\mathcal A$. Thus the submultiplicativity of the norm in $\mathcal A/I$ (VII.2.6) implies
$$
\begin{aligned}
\|a^*a+I\|&=\|(a^*+I)(a+I)\|\\
&\leq\|a^*+I\|\|a+I\|\\
&=\|a+I\|^2.
\end{aligned}
$$

On the other hand, the preceding lemma gives that
$$
\begin{aligned}
\|a+I\|^2
&=\inf\{\|a-ax\|^2:x\in(\operatorname{ball} I)_+\}\\
&=\inf\{\|a(1-x)\|^2:x\in(\operatorname{ball} I)_+\}\\
&=\inf\{\|(1-x)a^*a(1-x)\|:x\in(\operatorname{ball} I)_+\}.
\end{aligned}
$$
