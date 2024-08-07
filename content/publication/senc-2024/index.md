---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'SENC: Handling Self-collision in Neural Cloth Simulation'
subtitle: ''
summary: ''
authors:
- Zhouyingcheng Liao
- Sinan Wang
- Taku Komura

tags:
- 'Neural cloth simulation'
- 'Self collision'

categories: []
date: '2024-07-01'
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
- '1'
abstract: We present SENC, a novel self-supervised neural cloth simulator that addresses the challenge of cloth self-collision. This problem has remained unresolved due to the gap in simulation setup between recent collision detection and response approaches and self-supervised neural simulators. The former requires collision-free initial setups, while the latter necessitates random cloth instantiation during training. To tackle this issue, we propose a novel loss based on Global Intersection Analysis (GIA). This loss extracts the volume surrounded by the cloth region that forms the penetration. By constructing an energy based on this volume, our self-supervised neural simulator can effectively address cloth self-collisions. Moreover, we develop a self-collision-aware graph neural network capable of learning to handle self-collisions, even for parts that are topologically distant from one another. Additionally, we introduce an effective external force scheme that enables the simulation to learn the cloth's behavior in response to random external forces. We validate the efficacy of SENC through extensive quantitative and qualitative experiments, demonstrating that it effectively reduces cloth self-collision while maintaining high-quality animation results.
publication: 'ECCV 2024'
---
