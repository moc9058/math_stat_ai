Fix $f$ in $C_b(X)$ and define $f^\beta:\beta X\to\mathbb F$ by $f^\beta(\tau)=\langle f,\tau\rangle$ for every $\tau$ in $\beta X$. [Remember that $\beta X\subseteq C_b(X)^*$, so that this makes sense.] Clearly $f^\beta$ is continuous and $f^\beta\circ\Delta(x)=f^\beta(\delta_x)=\langle f,\delta_x\rangle=f(x)$. So $f^\beta\circ\Delta=f$ and (c) holds.

To show that $\beta X$ is unique, assume that $\Omega$ is a compact space and $\pi:X\to\Omega$ is a continuous map such that:

(a′) $\pi:X\to\pi(X)$ is a homeomorphism;

(b′) $\pi(X)$ is dense in $\Omega$;

(c′) if $f\in C_b(X)$, there is an $\tilde f$ in $C(\Omega)$ such that $\tilde f\circ\pi=f$.

Define $g:\Delta(X)\to\Omega$ by $g(\Delta(x))=\pi(x)$. In other words, $g=\pi\circ\Delta^{-1}$. The idea is to extend $g$ to a homeomorphism of $\beta X$ onto $\Omega$. If $\tau_0\in\beta X$, then (b) implies that there is a net $\{x_i\}$ in $X$ such that $\Delta(x_i)\to\tau_0$ in $\beta X$. Now $\{\pi(x_i)\}$ is a net in $\Omega$ and since $\Omega$ is compact, there is an $\omega_0$ in $\Omega$ such that $\pi(x_i)\xrightarrow[\mathrm{cl}]{}\omega_0$. If $F\in C(\Omega)$, let $f=F\circ\pi$; so $f\in C_b(X)$ (and $F=\tilde f$). Also, $f(x_i)=\langle f,\delta_{x_i}\rangle\to\langle f,\tau_0\rangle=f^\beta(\tau_0)$. But it is also true that $f(x_i)=F(\pi(x_i))\xrightarrow[\mathrm{cl}]{}F(\omega_0)$. Hence $F(\omega_0)=f^\beta(\tau_0)$ for any $F$ in $C(\Omega)$. This implies that $\omega_0$ is the unique cluster point of $\{\pi(x_i)\}$; thus $\pi(x_i)\to\omega_0$ (A.2.7). Let $g(\tau_0)=\omega_0$. It must be shown that the definition of $g(\tau_0)$ does not depend on the net $\{x_i\}$ in $X$ such that $\Delta(x_i)\to\tau_0$. This is left as an exercise. To summarize, it has been shown that

$$
\begin{gathered}
\text{There is a function }g:\beta X\to\Omega\\
\text{such that if }f\in C_b(X),\text{ then }f^\beta=\tilde f\circ g.
\end{gathered}
\tag{6.3}
$$

To show that $g:\beta X\to\Omega$ is continuous, let $\{\tau_i\}$ be a net in $\beta X$ such that $\tau_i\to\tau$. If $F\in C(\Omega)$, let $f=F\circ\pi$; so $f\in C_b(X)$ and $\tilde f=F$. Also, $f^\beta(\tau_i)\to f^\beta(\tau)$. But $F(g(\tau_i))=f^\beta(\tau_i)\to f^\beta(\tau)=F(g(\tau))$. It follows (6.1) that $g(\tau_i)\to g(\tau)$ in $\Omega$. Thus $g$ is continuous.

It is left as an exercise for the reader to show that $g$ is injective. Since $g(\beta X)\supseteq g(\Delta(X))=\pi(X)$, $g(\beta X)$ is dense in $\Omega$. But $g(\beta X)$ is compact, so $g$ is bijective. By (A.2.8), $g$ is a homeomorphism. ■

The compact set $\beta X$ obtained in the preceding theorem is called the *Stone–Čech compactification* of $X$. By properties (a) and (b), $X$ can be considered as a dense subset of $\beta X$ and the map $\Delta$ can be taken to be the inclusion map. With this convention, (c) can be interpreted as saying that every bounded continuous function on $X$ has a continuous extension to $\beta X$.

The space $\beta X$ is usually very much larger than $X$. In particular, it is almost never true that $\beta X$ is the one-point compactification of $X$. For example, if $X=(0,1]$, then the one-point compactification of $X$ is $[0,1]$. However, $\sin(1/x)\in C_b(X)$ but it has no continuous extension to $[0,1]$, so $\beta X\ne[0,1]$.

To obtain an idea of how large $\beta X\setminus X$ is, see Exercise 6, which indicates how to show that if $\mathbf N$ has the discrete topology, then $\beta\mathbf N\setminus\mathbf N$ has $2^{\aleph_0}$ pairwise disjoint open sets. The best source of information on the
