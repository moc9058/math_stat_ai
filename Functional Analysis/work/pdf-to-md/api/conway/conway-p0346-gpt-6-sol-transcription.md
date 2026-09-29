Similarly, for each $\phi$ in $\mathcal L$

$$
S_\phi h=\int_0^\infty \phi(t)U(-t)h\,dt.
\tag{5.9}
$$

defines a bounded operator on $\mathcal H$.

For any $\phi$ in $\mathcal L$ and $t$ in $\mathbb R$,

$$
\begin{aligned}
U(t)T_\phi h
&=U(t)\int_0^\infty \phi(s)U(s)h\,ds\\
&=\int_0^\infty \phi(s)U(t+s)h\,ds\\
&=\int_t^\infty \phi(s-t)U(s)h\,ds.
\end{aligned}
$$

Similarly,

$$
U(t)S_\phi h=\int_{-t}^\infty \phi(s+t)U(-s)h\,ds.
$$

Now let $\mathcal L^{(1)}=$ all $\phi$ in $\mathcal L$ that are continuously differentiable with $\phi'$ in $\mathcal L$. For $\phi$ in $\mathcal L^{(1)}$,

$$
\begin{aligned}
-\frac{i}{t}[U(t)-1]T_\phi h
&=-\frac{i}{t}\int_t^\infty \phi(s-t)U(s)h\,ds
+\frac{i}{t}\int_0^\infty \phi(s)U(s)h\,ds\\
&=-i\int_t^\infty
\left[\frac{\phi(s-t)-\phi(s)}{t}\right]U(s)h\,ds
+\frac{i}{t}\int_0^t \phi(s)U(s)h\,ds.
\end{aligned}
$$

Now

$$
\left\|\int_0^t
\left[\frac{\phi(s-t)-\phi(s)}{t}\right]U(s)h\,ds\right\|
\leq \|h\|\sup\{|\phi(s-t)-\phi(s)|:0\leq s\leq1\}\to0
$$

as $t\to0$. Hence

$$
\begin{aligned}
\lim_{t\to0}\int_t^\infty
\left[\frac{\phi(s-t)-\phi(s)}{t}\right]U(s)h\,ds
&=-\int_0^\infty \phi'(s)U(s)h\,ds\\
&=-T_{\phi'}h.
\end{aligned}
$$

Since $s\mapsto\phi(s)U(s)h$ is continuous and $U(0)=1$, the Fundamental Theorem of Calculus implies that

$$
\lim_{t\to0}\frac1t\int_0^t\phi(s)U(s)h\,ds=\phi(0)h.
$$

Hence for $\phi$ in $\mathcal L^{(1)}$ and $h$ in $\mathcal H$,

$$
\lim_{t\to0}-\frac{i}{t}[U(t)-1]T_\phi h
=iT_{\phi'}h+i\phi(0)h.
\tag{5.10}
$$
