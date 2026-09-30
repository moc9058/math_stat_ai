1.2 The Geometric Forms of the Hahn–Banach Theorem: Separation of Convex Sets

$$
g ( t x _ { 0 } ) = t , \quad t \in \mathbb { R } .
$$

It is clear that

$$
g ( x ) \leq p ( x ) \quad \forall x \in G
$$

(consider the two cases $t   >   0$ and $t \leq 0 )$ . It follows from Theorem 1.1 that there exists a linear functional f on E that extends g and satisfies

$$
f ( x ) \leq p ( x ) \quad \forall x \in E .
$$

In particular, we have $f ( x _ { 0 } ) = 1$ and that f is continuous by (9). We deduce from (10) that $f ( x ) < 1$ for every $x \in C$

Proof of Theorem 1.6. Set $C = A - B$ , so that C is convex (check!), C is open (since $C = \bigcup_{y \in B} (A - y))$ , and $0 \notin C$ (because $A \cap B = \varnothing )$ . By Lemma 1.3 there is some $f \in E ^ { \star }$ such that

$$
f ( z ) < 0 \quad \forall z \in C ,
$$

that is,

$$
f(x) < f(y) \quad \forall x \in A, \quad \forall y \in B.
$$

Fix a constant α satisfying

$$
\sup_{x \in A} f(x) \leq \alpha \leq \inf_{y \in B} f(y).
$$

Clearly, the hyperplane $[ f = \alpha ]$ separates A and B.

• **Theorem 1.7 (Hahn–Banach, second geometric form).** Let $A \subset E$ and $B \subset E$ be two nonempty convex subsets such that $A \cap B = \varnothing .$ . Assume that A is closed and B is compact. Then there exists a closed hyperplane that strictly separates A and B.

Proof. Set $C = A - B$ , so that C is convex, closed (check!), and $0 \notin C$ . Hence, there is some $r   >   0$ such that $B ( 0 , r ) \cap C = \varnothing .$ . By Theorem 1.6 there is a closed hyperplane that separates $B ( 0 , r )$ and C. Therefore, there is some $f \in E ^ { \star } ,   f \not \equiv 0 ,$ such that

$$
f(x - y) \leq f(rz) \quad \forall x \in A, \quad \forall y \in B, \quad \forall z \in B(0,1).
$$

It follows that $f(x - y) \leq - r \| f \| \quad \forall x \in A, \forall y \in B$ . Letting $\begin{array} { r } { \varepsilon = \frac { 1 } { 2 } r \| f \| > 0 } \end{array}$ , we obtain

$$
f(x) + \varepsilon \leq f(y) - \varepsilon \quad \forall x \in A, \quad \forall y \in B.
$$

Choosing α such that

$$
\sup_{x \in A} f(x) + \varepsilon \leq \alpha \leq \inf_{y \in B} f(y) - \varepsilon,
$$

we see that the hyperplane $[ f = \alpha ]$ strictly separates A and B.

Remark 4. Assume that $A \subset E$ and $B \subset E$ are two nonempty convex sets such that $A \cap B = \varnothing$ . If we make no further assumption, it is in general impossible to separate