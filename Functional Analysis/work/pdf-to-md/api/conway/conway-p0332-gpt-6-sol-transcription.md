**3.1. Theorem.** (a) If $A$ is a closed densely defined symmetric operator with deficiency subspaces $\mathcal L_\pm$, and if $U:\mathcal H\to\mathcal H$ is defined by letting $U=0$ on $\mathcal L_+$ and

$$
U=(A-i)(A+i)^{-1} \tag{3.2}
$$

on $\mathcal L_+^\perp$, then $U$ is a partial isometry with initial space $\mathcal L_+^\perp$, final space $\mathcal L_-^\perp$, and such that $(1-U)(\mathcal L_+^\perp)$ is dense in $\mathcal H$.

(b) If $U$ is a partial isometry with initial and final spaces $\mathcal M$ and $\mathcal N$, respectively, and such that $(1-U)\mathcal M$ is dense in $\mathcal H$, then

$$
A=i(1+U)(1-U)^{-1} \tag{3.3}
$$

is a densely defined closed symmetric operator with deficiency subspaces $\mathcal L_+=\mathcal M^\perp$ and $\mathcal L_-=\mathcal N^\perp$.

(c) If $A$ is given as in (a) and $U$ is defined by (3.2), then $A$ and $U$ satisfy (3.3). If $U$ is given as in (b) and $A$ is defined by (3.3), then $A$ and $U$ satisfy (3.2).

**Proof.** (a) By (2.5c), $\operatorname{ran}(A\pm i)$ is closed and so $\mathcal L_\pm^\perp=\operatorname{ran}(A\pm i)$. By (2.5b), $\ker(A+i)=(0)$, so $(A+i)^{-1}$ is well defined on $\mathcal L_+^\perp$. Moreover, $(A+i)^{-1}\mathcal L_+^\perp\subseteq\operatorname{dom}A$ so that $U$ defined by (3.2) makes sense and gives a well-defined operator. If $h\in\mathcal L_+^\perp$, then $h=(A+i)f$ for a unique $f$ in $\operatorname{dom}A$. Hence $\|Uh\|^2=\|(A-i)f\|^2\overset{(2.5a)}{=}\|Af\|^2+\|f\|^2=\|(A+i)f\|^2=\|h\|^2$. Hence $U$ is a partial isometry, $(\ker U)^\perp=\mathcal L_+^\perp$, and $\operatorname{ran}U=\mathcal L_-^\perp$. Once again, if $f\in\operatorname{dom}A$ and $h=(A+i)f$, then $(1-U)h=h-(A-i)f=(A+i)f-(A-i)f=2if$. So $(1-U)\mathcal L_+^\perp=\operatorname{dom}A$ and is dense in $\mathcal H$.

(b) Now assume that $U$ is a partial isometry as in (b). It follows that $\ker(1-U)=(0)$. In fact, if $f\in\ker(1-U)$, then $Uf=f$; so $\|f\|=\|Uf\|$ and hence $f\in\text{initial }U$. Since $U^*U$ is the projection onto initial $U$, $f=U^*Uf=U^*f$; so $f\in\ker(1-U^*)=\operatorname{ran}(1-U)^\perp\subseteq[(1-U)\mathcal M]^\perp=(0)$ by hypothesis. Thus $f=0$ and $1-U$ is injective.

Let $\mathcal D=(1-U)\mathcal M$ and define $(1-U)^{-1}$ on $\mathcal D$. Because $1-U$ is bounded, $\operatorname{gra}(1-U)^{-1}$ is closed. If $A$ is defined as in (3.3), it follows that $A$ is a closed densely defined operator. If $f,g\in\mathcal D$, let $f=(1-U)h$ and $g=(1-U)k$, $h,k\in\mathcal M$. Hence

$$
\begin{aligned}
\langle Af,g\rangle
&=i\langle(1+U)h,(1-U)k\rangle\\
&=i[\langle h,k\rangle+\langle Uh,k\rangle-\langle h,Uk\rangle-\langle Uh,Uk\rangle].
\end{aligned}
$$

Since $h,k\in\mathcal M$, $\langle Uh,Uk\rangle=\langle h,k\rangle$; hence $\langle Af,g\rangle=i[\langle Uh,k\rangle-\langle h,Uk\rangle]$. Similarly, $\langle f,Ag\rangle=-i\langle(1-U)h,(1+U)k\rangle=-i[\langle h,Uk\rangle-\langle Uh,k\rangle]=\langle Af,g\rangle$. Hence $A$ is symmetric.

Finally, if $h\in\mathcal M$ and $f=(1-U)h$, then $(A+i)f=Af+if=i(1+U)h+i(1-U)h=2ih$. Thus $\operatorname{ran}(A+i)=\mathcal M$. Similarly, $(A-i)f=i(1+U)h-i(1-U)h=2Uh$, so that $\operatorname{ran}(A-i)=\operatorname{ran}U=\mathcal N$.

(c) Suppose $A$ is as in (a) and $U$ is defined as in (3.2). If $g\in(1-U)\mathcal L_+^\perp$, put $g=(1-U)h$, where $h\in\mathcal L_+^\perp=\operatorname{ran}(A+i)$. Hence $h=(A+i)f$ for some $f$ in $\operatorname{dom}A$. Thus $g=h-Uh=(A+i)f-(A-i)f=2if$; so $f=-\frac12ig$.
