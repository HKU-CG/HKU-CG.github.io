---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Analytic rotation-invariant modelling of anisotropic finite elements'
subtitle: ''
summary: ''
authors:
- Huancheng Lin
- Floyd M. Chitalu
- Taku Komura

tags:
- 'Finite Elements'
- 'Anisotropy'
- 'Orthotropy'
- 'Physical Simulation'

categories: []
date: '2024-08-09'
lastmod: 2021-01-15T21:34:50Z
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2024-08-09T21:34:50.388741Z'
publication_types:
# 1 Conference paper
# 2 Journal article
# 3 Preprint
# 4 Report
# 5 Book
# 6 Book section
# 7 Thesis
# 8 Patent
- '2'
abstract: Anisotropic hyperelastic distortion energies 
    are used to solve many problems in fields like computer graphics and engineering with applications in shape analysis, deformation, design, mesh parameterization, biomechanics and more. 
    However, formulating a robust anisotropic energy that is low-order and yet sufficiently non-linear remains a challenging problem for achieving the convergence promised by Newton-type methods in numerical optimization. 
    In this paper, we propose a novel analytic formulation of an anisotropic energy that is smooth everywhere, low-order, rotationally-invariant and at-least twice differentiable. 
    At its core, our approach utilizes implicit rotation factorizations with invariants of the Cauchy-Green tensor that arises from the deformation gradient.
    The versatility and generality of our analysis is demonstrated through a variety of examples, where we also show that the constitutive law suggested by the anisotropic version of the well-known \textit{As-Rigid-As-Possible} energy is the foundational parametric description of both passive and active elastic materials.
    The generality of our approach means that we can systematically derive the force and force-Jacobian expressions for use in implicit and quasistatic numerical optimization schemes, and we can also use our analysis to rewrite, simplify and speedup several existing anisotropic \textit{and} isotropic distortion energies with guaranteed inversion-safety.
publication: 'ACM Transactions on Graphics (TOG)'
---
