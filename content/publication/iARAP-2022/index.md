---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Isotropic ARAP energy using Cauchy-Green invariants'
subtitle: ''
summary: ''
authors:
- Huancheng Lin
- Floyd M. Chitalu
- Taku Komura

tags:
- 'Mesh geometry models'
- 'Physical Simulation'

categories: []
date: '2022-11-30'
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
publishDate: '2022-11-30T21:34:50.388741Z'
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
abstract: Isotropic As-Rigid-As-Possible (ARAP) energy has been popular for shape editing, mesh parametrisation and soft-body simulation for almost two decades. However, a formulation using Cauchy-Green (CG) invariants has always been unclear, due to a rotation-polluted trace term that cannot be directly expressed using these invariants. We show how this incongruent trace term can be understood via an implicit relationship to the CG invariants. Our analysis reveals this relationship to be a polynomial where the roots equate to the trace term, and where the derivatives also give rise to closed-form expressions of the Hessian to guarantee positive semi-definiteness for a fast and concise Newton-type implicit time integration. A consequence of this analysis is a novel analytical formulation to compute rotations and singular values of deformation-gradient tensors without explicit/numerical factorization, which is significant, resulting in up to 3.5x speedup and benefits energy function evaluation for reducing solver time. We validate our energy formulation by experiments and comparison, demonstrating that our resulting eigendecomposition using the CG invariants is equivalent to existing ARAP formulations. We thus reveal isotropic ARAP energy to be a member of the "Cauchy-Green club", meaning that it can indeed be defined using CG invariants and therefore that the closed-form expressions of the resulting Hessian are shared with other energies written in their terms.
publication: 'ACM Transactions on Graphics (TOG)'
---
