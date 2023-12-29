---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'C·ASE: Learning Conditional Adversarial Skill Embeddings for Physics-based Characters'
subtitle: ''
summary: ''
authors:
- Zhiyang Dou
- Xuelin Chen
- Qingnan Fan
- Taku Komura
- Wenping Wang

tags:
- 'Physics-based Character Animation'
- 'GAIL'
- 'RL'

categories: []
date: '2023-12-01'
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
abstract: We present C·ASE, an efficient and effective framework that learns Conditional Adversarial Skill Embeddings for physics-based characters. C·ASE enables the physically simulated character to learn a diverse repertoire of skills while providing controllability in the form of direct manipulation of the skills to be performed. This is achieved by dividing the heterogeneous skill motions into distinct subsets containing homogeneous samples for training a low-level conditional model to learn the conditional behavior distribution. The skill-conditioned imitation learning naturally offers explicit control over the character’s skills after training. The training course incorporates the focal skill sampling, skeletal residual forces, and element-wise feature masking to balance diverse skills of varying complexities, mitigate dynamics mismatch to master agile motions and capture more general behavior characteristics, respectively. Once trained, the conditional model can produce highly diverse and realistic skills, outperforming state-of-the-art models, and can be repurposed in various downstream tasks. In particular, the explicit skill control handle allows a high-level policy or a user to direct the character with desired skill specifications, which we demonstrate is advantageous for interactive character animation.
publication: 'SIGGRAPH Asia 2023'
---
