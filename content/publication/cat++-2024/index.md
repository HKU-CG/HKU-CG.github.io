---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Coverage Axis++: Efficient Skeletal Points Selection for 3D Shape Skeletonization'
subtitle: 'Equal contributions: Zimeng and Zhiyang'
summary: 
authors:
- Zimeng Wang
- Zhiyang Dou
- Rui Xu
- Cheng Lin
- Yuan Liu
- Xiaoxiao Long
- Shiqing Xin
- Taku Komura
- Xiaoming Yuan
- Wenping Wang


tags:
- 'Geometric Modeling'
- 'Medial Axis Transform'

categories: []
date: '2024-06-27'
lastmod: 2024-06-27T21:34:50Z
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
publishDate: '2024-06-27T21:34:50.388741Z'
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
abstract:      We introduce Coverage Axis++, a novel and efficient approach to 3D shape skeletonization. The current state-of-the-art approaches for this task often rely on the watertightness of the input or suffer from substantial computational costs, thereby limiting their practicality. To address this challenge, Coverage Axis++ proposes a heuristic algorithm to select skeletal points, offering a high-accuracy approximation of the Medial Axis Transform (MAT) while significantly mitigating computational intensity for various shape representations. We introduce a simple yet effective strategy that considers shape coverage, uniformity, and centrality to derive skeletal points. The selection procedure enforces consistency with the shape structure while favoring the dominant medial balls, which thus introduces a compact underlying shape representation in terms of MAT. As a result, Coverage Axis++ allows for skeletonization for various shape representations (e.g., water-tight meshes, triangle soups, point clouds), specification of the number of skeletal points, few hyperparameters, and highly efficient computation with improved reconstruction accuracy. Extensive experiments across a wide range of 3D shapes validate the efficiency and effectiveness of Coverage Axis++. \ZY{Our codes are available at \url{https://github.com/Frank-ZY-Dou/Coverage_Axis}.
publication: 'SGP 2024'
---
