**Proof.** Actually it must be shown that $Kf\in L^2(\mu)$, but this will follow from the argument that demonstrates the boundedness of $K$. If $f\in L^2(\mu)$,

$$
\begin{aligned}
|Kf(x)|
&\leqslant \int |k(x,y)|\,|f(y)|\,d\mu(y)\\
&= \int |k(x,y)|^{1/2}|k(x,y)|^{1/2}|f(y)|\,d\mu(y)\\
&\leqslant
\left[\int |k(x,y)|\,d\mu(y)\right]^{1/2}
\left[\int |k(x,y)|\,|f(y)|^2\,d\mu(y)\right]^{1/2}\\
&\leqslant c_1^{1/2}
\left[\int |k(x,y)|\,|f(y)|^2\,d\mu(y)\right]^{1/2}.
\end{aligned}
$$

Hence

$$
\begin{aligned}
\int |Kf(x)|^2\,d\mu(x)
&\leqslant c_1\int\!\!\int |k(x,y)|\,|f(y)|^2\,d\mu(y)\,d\mu(x)\\
&=c_1\int |f(y)|^2\int |k(x,y)|\,d\mu(x)\,d\mu(y)\\
&\leqslant c_1c_2\|f\|^2.
\end{aligned}
$$

Now this shows that the formula used to define $Kf$ is finite a.e. $[\mu]$, $Kf\in L^2(\mu)$, and $\|Kf\|^2\leqslant c_1c_2\|f\|^2$. ■

The operator described above is called an *integral operator* and the function $k$ is called its kernel. There are conditions on the kernel other than the one in (1.6) that will imply that $K$ is bounded.

A particular example of an integral operator is the *Volterra operator* defined below.

**1.7. Example.** Let $k:[0,1]\times[0,1]\to\mathbb{R}$ be the characteristic function of $\{(x,y):y<x\}$. The corresponding operator $V:L^2(0,1)\to L^2(0,1)$ defined by $Vf(x)=\int_0^1 k(x,y)f(y)\,dy$ is called the *Volterra operator*. Note that

$$
Vf(x)=\int_0^x f(y)\,dy.
$$

Another example of an operator was defined in Example 1.5.3. The nonsurjective isometry defined there is called the *unilateral shift*. It will be studied in more detail later in this book. Note that any isometry is a bounded operator with norm 1.

## Exercises

1. Prove Proposition 1.1.
2. Prove Proposition 1.2.
