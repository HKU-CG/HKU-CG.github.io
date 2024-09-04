---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'MotioNet: 3D Human Motion Reconstruction from Monocular Video with Skeleton Consistency'
subtitle: ''
summary: ''
authors:
- Mingyi Shi
- Kfir Aberman
- Andreas Aristidou
- Taku Komura
- Dani Lischinski
- Daniel Cohen-Or
- Baoquan Chen

tags:
- '3D motion reconstruction'

categories: []
date: '2020-07-01'
lastmod: 2020-01-15T21:34:50Z
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
publishDate: '2020-07-01T21:34:50.388741Z'
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
abstract: We introduce MotioNet, a deep neural network that directly reconstructs the motion of a 3D human skeleton from monocular video. While previous methods rely on either rigging or inverse kinematics (IK) to associate a consistent skeleton with temporally coherent joint rotations, our method is the first data-driven approach that directly outputs a kinematic skeleton, which is a complete, commonly used, motion representation. At the crux of our approach lies a deep neural network with embedded kinematic priors, which decomposes sequences of 2D joint positions into two separate attributes - a single, symmetric, skeleton, encoded by bone lengths, and a sequence of 3D joint rotations associated with global root positions and foot contact labels.
publication: 'ToG 2020'
---
