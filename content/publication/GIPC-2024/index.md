---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'GIPC: Fast and Stable Gauss-Newton Optimization of IPC Barrier Energy'
subtitle: ''
summary: ''
authors:
- Kemeng Huang
- Floyd M. Chitalu
- Huancheng Lin
- Taku Komura

tags:
- 'IPC'
- 'Barrier Hessian'
- 'Eigen Analysis'
- 'GPU'

categories: []
date: '2024-03-24'
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
publishDate: '2024-03-24T21:34:50.388741Z'
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
abstract: Barrier functions are crucial for maintaining an intersection- and inversion-free simulation trajectory but existing methods, which directly use distance can restrict implementation design and performance. We present an approach to rewriting the barrier function for arriving at an efficient and robust approximation of its Hessian. The key idea is to formulate a simplicial geometric measure of contact using mesh boundary elements, from which analytic eigensystems are derived and enhanced with filtering and stiffening terms that ensure robustness with respect to the convergence of a Project-Newton solver. A further advantage of our rewriting of the barrier function is that it naturally caters to the notorious case of nearly parallel edge-edge contacts for which we also present a novel analytic eigensystem. Our approach is thus well suited for standard second-order unconstrained optimization strategies for resolving contacts, minimizing nonlinear nonconvex functions where the Hessian may be indefinite. The efficiency of our eigensystems alone yields a 3× speedup over the standard Incremental Potential Contact (IPC) barrier formulation. We further apply our analytic proxy eigensystems to produce an entirely GPU-based implementation of IPC with significant further acceleration.
publication: 'ACM Transactions on Graphics (TOG)'
---
