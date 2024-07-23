---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'TLControl: Trajectory and Language Control for Human Motion Synthesis'
subtitle: ''
summary: 
authors:
- Weilin Wan
- Zhiyang Dou
- Taku Komura
- Wenping Wang
- Dinesh Jayaraman
- Lingjie Liu



tags:
- '3D human motion generation'

categories: []
date: '2024-07-21'
lastmod: 2024-07-21T21:34:50Z
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
publishDate: '2024-07-21T21:34:50.388741Z'
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
abstract: Controllable human motion synthesis is essential for applications in AR/VR, gaming, movies, and embodied AI. Existing methods often focus solely on either language or full trajectory control, lacking precision in synthesizing motions aligned with user-specified trajectories, especially for multi-joint control. To address these issues, we present TLControl, a new method for realistic human motion synthesis, incorporating both low-level trajectory and high-level language semantics controls. Specifically, we first train a VQ-VAE to learn a compact latent motion space organized by body parts. We then propose a Masked Trajectories Transformer to make coarse initial predictions of full trajectories of joints based on the learned latent motion space, with user-specified partial trajectories and text descriptions as conditioning. Finally, we introduce an efficient test-time optimization to refine these coarse predictions for accurate trajectory control. Experiments demonstrate that TLControl outperforms the state-of-the-art in trajectory accuracy and time efficiency, making it practical for interactive and high-quality animation generation.
publication: 'ECCV 2024'
---
