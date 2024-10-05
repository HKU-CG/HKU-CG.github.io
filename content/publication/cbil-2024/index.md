---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'CBIL: Collective Behavior Imitation Learning for Fish from Real Videos'
subtitle: 'Equal contributions: Yifan and Zhiyang'
summary: ''
authors:
- Yifan Wu
- Zhiyang Dou
- Yuko Ishiwaka
- Shun Ogawa
- Yuke Lou
- Wenping Wang
- Lingjie Liu
- Taku Komura

tags:
- 'Crowd Animation'
- 'Physics-based Character Animation'
- 'GAIL'
- 'RL'

categories: []
date: '2024-12-03'
lastmod: 2024-12-03T21:34:50Z
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
publishDate: '2024-10-03T21:34:50.388741Z'
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
abstract: Reproducing realistic collective behaviors presents a captivating yet formidable challenge. Traditional rule-based methods rely on hand-crafted principles, limiting motion diversity and realism in generated collective behaviors. Recent imitation learning methods learn from data but often require ground truth motion trajectories and struggle with authenticity, especially in high-density groups with erratic movements. In this paper, we present a scalable approach, Collective Behavior Imitation Learning (CBIL), for learning fish schooling behavior directly from videos, without relying on captured motion trajectories. Our method first leverages Video Representation Learning, where a Masked Video AutoEncoder (MVAE) extracts implicit states from video inputs in a self-supervised manner. The MVAE effectively maps 2D observations to implicit states that are compact and expressive for following the imitation learning stage. Then, we propose a novel adversarial imitation learning method to effectively capture complex movements of the schools of fish, allowing for efficient imitation of the distribution for motion patterns measured in the latent space. It also incorporates bio-inspired rewards alongside priors to regularize and stabilize training. Once trained, CBIL can be used for various animation tasks with the learned collective motion priors. We further show its effectiveness across different species. Finally, we demonstrate the application of our system in detecting abnormal fish behavior from in-the-wild videos.
publication: 'SIGGRAPH Asia 2024'
---
