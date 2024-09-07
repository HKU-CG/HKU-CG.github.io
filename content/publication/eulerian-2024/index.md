---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'An Eulerian Vortex Method on Flow Maps'
subtitle: ''
summary: ''
authors:
- Sinan Wang
- Yitong Deng
- Molin Deng
- Hong-Xing Yu
- Junwei Zhou
- Duowen Chen
- Taku Komura
- Jiajun Wu
- Bo Zhu

tags:
- 'Fluid simulation'
- 'Vortex method'
- 'Flow map'
- 'Grid-based method'

categories: []
date: '2024-08-01'
lastmod: 2024-08-07T21:34:50Z
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
publishDate: '2021-01-15T21:34:50.388741Z'
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
abstract: We present an Eulerian vortex method based on the theory of flow maps to simulate the complex vortical motions of incompressible fluids. Central to our method is the novel incorporation of the flow-map transport equations for line elements, which, in combination with a bi-directional marching scheme for flow maps, enables the high-fidelity Eulerian advection of vorticity variables. The fundamental motivation is that, compared to impulse 𝒎, which has been recently bridged with flow maps to encouraging results, vorticity 𝝎 promises to be preferable for its numerically stability and physical interpretability. To realize the full potential of this novel formulation, we develop a new Poisson solving scheme for vorticity-to-velocity reconstruction that is both efficient and able to accurately handle the coupling near solid boundaries. We demonstrate the efficacy of our approach with a range of vortex simulation examples, including leapfrog vortices, vortex collisions, cavity flow, and the formation of complex vortical structures due to solid-fluid interactions.
publication: 'Siggraph Asia 2024 (ToG)'
---
