# Cover


<a id="pdf-page-1"></a>
Universitext

Haim Brezis

# Functional Analysis, Sobolev Spaces and Partial Differential Equations

Springer



<a id="pdf-page-2"></a>
Universitext

For other titles in this series, go to  
www.springer.com/series/223



<a id="pdf-page-3"></a>



<a id="pdf-page-4"></a>
Haim Brezis

# Functional Analysis, Sobolev Spaces and Partial Differential Equations

Springer



<a id="pdf-page-5"></a>
Haim Brezis  
Distinguished Professor  
Department of Mathematics  
Rutgers University  
Piscataway, NJ 08854  
USA  
brezis@math.rutgers.edu

and

Professeur émérite, Université Pierre et Marie Curie (Paris 6)

and

Visiting Distinguished Professor at the Technion

*Editorial board:*  
Sheldon Axler, San Francisco State University  
Vincenzo Capasso, Università degli Studi di Milano  
Carles Casacuberta, Universitat de Barcelona  
Angus MacIntyre, Queen Mary, University of London  
Kenneth Ribet, University of California, Berkeley  
Claude Sabbah, CNRS, École Polytechnique  
Endre Süli, University of Oxford  
Wojbor Woyczyński, Case Western Reserve University

ISBN 978-0-387-70913-0  
DOI 10.1007/978-0-387-70914-7  
e-ISBN 978-0-387-70914-7  
Springer New York Dordrecht Heidelberg London

Library of Congress Control Number: 2010938382

Mathematics Subject Classification (2010): 35Rxx, 46Sxx, 47Sxx

© Springer Science+Business Media, LLC 2011  
All rights reserved. This work may not be translated or copied in whole or in part without the written permission of the publisher (Springer Science+Business Media, LLC, 233 Spring Street, New York, NY 10013, USA), except for brief excerpts in connection with reviews or scholarly analysis. Use in connection with any form of information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed is forbidden.

The use in this publication of trade names, trademarks, service marks, and similar terms, even if they are not identified as such, is not to be taken as an expression of opinion as to whether or not they are subject to proprietary rights.

Printed on acid-free paper

Springer is part of Springer Science+Business Media (www.springer.com)



<a id="pdf-page-6"></a>
*To Felix Browder, a mentor and close friend,*  
*who taught me to enjoy PDEs through the*  
*eyes of a functional analyst*



<a id="pdf-page-7"></a>



<a id="pdf-page-8"></a>
# Preface

This book has its roots in a course I taught for many years at the University of Paris. It is intended for students who have a good background in real analysis (as expounded, for instance, in the textbooks of G. B. Folland [2], A. W. Knapp [1], and H. L. Royden [1]). I conceived a program mixing elements from two distinct “worlds”: functional analysis (FA) and partial differential equations (PDEs). The first part deals with abstract results in FA and operator theory. The second part concerns the study of spaces of functions (of one or more real variables) having specific differentiability properties: the celebrated Sobolev spaces, which lie at the heart of the modern theory of PDEs. I show how the abstract results from FA can be applied to solve PDEs. The Sobolev spaces occur in a wide range of questions, in both pure and applied mathematics. They appear in linear and nonlinear PDEs that arise, for example, in differential geometry, harmonic analysis, engineering, mechanics, and physics. They belong to the toolbox of any graduate student in analysis.

Unfortunately, FA and PDEs are often taught in separate courses, even though they are intimately connected. Many questions tackled in FA originated in PDEs (for a historical perspective, see, e.g., J. Dieudonné [1] and H. Brezis–F. Browder [1]). There is an abundance of books (even voluminous treatises) devoted to FA. There are also numerous textbooks dealing with PDEs. However, a synthetic presentation intended for graduate students is rare. and I have tried to fill this gap. Students who are often fascinated by the most abstract constructions in mathematics are usually attracted by the elegance of FA. On the other hand, they are repelled by the never-ending PDE formulas with their countless subscripts. I have attempted to present a “smooth” transition from FA to PDEs by analyzing first the simple case of one-dimensional PDEs (i.e., ODEs—ordinary differential equations), which looks much more manageable to the beginner. In this approach, I expound techniques that are possibly too sophisticated for ODEs, but which later become the cornerstones of the PDE theory. This layout makes it much easier for students to tackle elaborate higher-dimensional PDEs afterward.

A previous version of this book, originally published in 1983 in French and followed by numerous translations, became very popular worldwide, and was adopted as a textbook in many European universities. A deficiency of the French text was the



<a id="pdf-page-9"></a>
lack of exercises. The present book contains a wealth of problems. I plan to add even more in future editions. I have also outlined some recent developments, especially in the direction of nonlinear PDEs.

## Brief user’s guide

1. Statements or paragraphs preceded by the bullet symbol • **are extremely important**, and it is essential to grasp them well in order to understand what comes afterward.

2. Results marked by the star symbol ⋆ **can be skipped** by the beginner; they are of interest only to advanced readers.

3. In each chapter I have labeled propositions, theorems, and corollaries in a continuous manner (e.g., Proposition 3.6 is followed by Theorem 3.7, Corollary 3.8, etc.). Only the remarks and the lemmas are numbered separately.

4. In order to simplify the presentation I assume that all vector spaces are over $\mathbb{R}$. Most of the results remain valid for vector spaces over $\mathbb{C}$. I have added in Chapter 11 a short section describing similarities and differences.

5. Many chapters are followed by numerous exercises. Partial solutions are presented at the end of the book. More elaborate problems are proposed in a separate section called “Problems” followed by “Partial Solutions of the Problems.” The problems usually require knowledge of material coming from various chapters. I have indicated at the beginning of each problem which chapters are involved. Some exercises and problems expound results stated without details or without proofs in the body of the chapter.

## Acknowledgments

During the preparation of this book I received much encouragement from two dear friends and former colleagues: Ph. Ciarlet and H. Berestycki. I am very grateful to G. Tronel, M. Comte, Th. Gallouet, S. Guerre-Delabrière, O. Kavian, S. Kichenassamy, and the late Th. Lachand-Robert, who shared their “field experience” in dealing with students. S. Antman, D. Kinderlehrer, and Y. Li explained to me the background and “taste” of American students. C. Jones kindly communicated to me an English translation that he had prepared for his personal use of some chapters of the original French book. I owe thanks to A. Ponce, H.-M. Nguyen, H. Castro, and H. Wang, who checked carefully parts of the book. I was blessed with two extraordinary assistants who typed most of this book at Rutgers: Barbara Miller, who is retired, and now Barbara Mastrian. I do not have enough words of praise and gratitude for their constant dedication and their professional help. They always found attractive solutions to the challenging intricacies of PDE formulas. Without their enthusiasm and patience this book would never have been finished. It has been a great pleasure, as



<a id="pdf-page-10"></a>
ever, to work with Ann Kostant at Springer on this project. I have had many opportunities in the past to appreciate her long-standing commitment to the mathematical community.

The author is partially supported by NSF Grant DMS-0802958.

*Haim Brezis*  
Rutgers University  
March 2010



<a id="pdf-page-11"></a>



<a id="pdf-page-12"></a>
# Contents

**Preface** — vii

**1 The Hahn–Banach Theorems. Introduction to the Theory of Conjugate Convex Functions** — 1  
1.1 The Analytic Form of the Hahn–Banach Theorem: Extension of Linear Functionals — 1  
1.2 The Geometric Forms of the Hahn–Banach Theorem: Separation of Convex Sets — 4  
1.3 The Bidual $E^{**}$. Orthogonality Relations — 8  
1.4 A Quick Introduction to the Theory of Conjugate Convex Functions — 10  
Comments on Chapter 1 — 17  
Exercises for Chapter 1 — 19

**2 The Uniform Boundedness Principle and the Closed Graph Theorem** — 31  
2.1 The Baire Category Theorem — 31  
2.2 The Uniform Boundedness Principle — 32  
2.3 The Open Mapping Theorem and the Closed Graph Theorem — 34  
2.4 Complementary Subspaces. Right and Left Invertibility of Linear Operators — 37  
2.5 Orthogonality Revisited — 40  
2.6 An Introduction to Unbounded Linear Operators. Definition of the Adjoint — 43  
2.7 A Characterization of Operators with Closed Range. A Characterization of Surjective Operators — 46  
Comments on Chapter 2 — 48  
Exercises for Chapter 2 — 49

**3 Weak Topologies. Reflexive Spaces. Separable Spaces. Uniform Convexity** — 55  
3.1 The Coarsest Topology for Which a Collection of Maps Becomes Continuous — 55



<a id="pdf-page-13"></a>
3.2 Definition and Elementary Properties of the Weak Topology $\sigma(E,E^*)$ — 57  
3.3 Weak Topology, Convex Sets, and Linear Operators — 60  
3.4 The Weak* Topology $\sigma(E^*,E)$ — 62  
3.5 Reflexive Spaces — 67  
3.6 Separable Spaces — 72  
3.7 Uniformly Convex Spaces — 76  
Comments on Chapter 3 — 78  
Exercises for Chapter 3 — 79

**4 $L^p$ Spaces** — 89  
4.1 Some Results about Integration That Everyone Must Know — 90  
4.2 Definition and Elementary Properties of $L^p$ Spaces — 91  
4.3 Reflexivity. Separability. Dual of $L^p$ — 95  
4.4 Convolution and regularization — 104  
4.5 Criterion for Strong Compactness in $L^p$ — 111  
Comments on Chapter 4 — 114  
Exercises for Chapter 4 — 118

**5 Hilbert Spaces** — 131  
5.1 Definitions and Elementary Properties. Projection onto a Closed Convex Set — 131  
5.2 The Dual Space of a Hilbert Space — 135  
5.3 The Theorems of Stampacchia and Lax–Milgram — 138  
5.4 Hilbert Sums. Orthonormal Bases — 141  
Comments on Chapter 5 — 144  
Exercises for Chapter 5 — 146

**6 Compact Operators. Spectral Decomposition of Self-Adjoint Compact Operators** — 157  
6.1 Definitions. Elementary Properties. Adjoint — 157  
6.2 The Riesz–Fredholm Theory — 159  
6.3 The Spectrum of a Compact Operator — 162  
6.4 Spectral Decomposition of Self-Adjoint Compact Operators — 165  
Comments on Chapter 6 — 168  
Exercises for Chapter 6 — 170

**7 The Hille–Yosida Theorem** — 181  
7.1 Definition and Elementary Properties of Maximal Monotone Operators — 181  
7.2 Solution of the Evolution Problem $\frac{du}{dt}+Au=0$ on $[0,+\infty)$, $u(0)=u_0$. Existence and uniqueness — 184  
7.3 Regularity — 191  
7.4 The Self-Adjoint Case — 193  
Comments on Chapter 7 — 197



<a id="pdf-page-14"></a>
**8 Sobolev Spaces and the Variational Formulation of Boundary Value Problems in One Dimension** — 201  
8.1 Motivation — 201  
8.2 The Sobolev Space $W^{1,p}(I)$ — 202  
8.3 The Space $W_0^{1,p}$ — 217  
8.4 Some Examples of Boundary Value Problems — 220  
8.5 The Maximum Principle — 229  
8.6 Eigenfunctions and Spectral Decomposition — 231  
Comments on Chapter 8 — 233  
Exercises for Chapter 8 — 235

**9 Sobolev Spaces and the Variational Formulation of Elliptic Boundary Value Problems in $N$ Dimensions** — 263  
9.1 Definition and Elementary Properties of the Sobolev Spaces $W^{1,p}(\Omega)$ — 263  
9.2 Extension Operators — 272  
9.3 Sobolev Inequalities — 278  
9.4 The Space $W_0^{1,p}(\Omega)$ — 287  
9.5 Variational Formulation of Some Boundary Value Problems — 291  
9.6 Regularity of Weak Solutions — 298  
9.7 The Maximum Principle — 307  
9.8 Eigenfunctions and Spectral Decomposition — 311  
Comments on Chapter 9 — 312

**10 Evolution Problems: The Heat Equation and the Wave Equation** — 325  
10.1 The Heat Equation: Existence, Uniqueness, and Regularity — 325  
10.2 The Maximum Principle — 333  
10.3 The Wave Equation — 335  
Comments on Chapter 10 — 340

**11 Miscellaneous Complements** — 349  
11.1 Finite-Dimensional and Finite-Codimensional Spaces — 349  
11.2 Quotient Spaces — 353  
11.3 Some Classical Spaces of Sequences — 357  
11.4 Banach Spaces over $\mathbb{C}$: What Is Similar and What Is Different? — 361

**Solutions of Some Exercises** — 371

**Problems** — 435

**Partial Solutions of the Problems** — 521

**Notation** — 583

**References** — 585

**Index** — 595



<a id="pdf-page-15"></a>

