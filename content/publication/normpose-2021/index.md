---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Normalized Human Pose Features for Human Action Video Alignment'
subtitle: ''
summary: ''
authors:
- Jingyuan Liu
- Mingyi Shi
- Qifeng Chen
- Hongbo Fu
- Chiew-Lan Tai

tags:
- 'Human Action Recognization'

categories: []
date: '2021-07-01'
lastmod: 2021-07-01T21:34:50Z
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
publishDate: '2021-07-01T21:34:50.388741Z'
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
abstract: We present a novel approach for extracting human pose features from human action videos. The goal is to let the pose features capture only the poses of the action while being invariant to other factors, including video backgrounds, the video subjects’ anthropometric characteristics and viewpoints. Such human pose features facilitate the comparison of pose similarity and can be used for downstream tasks, such as human action video alignment and pose retrieval. The key to our approach is to first normalize the poses in the video frames by mapping the poses onto a pre-defined 3D skeleton to not only disentangle subject physical features, such as bone lengths and ratios, but also to unify global orientations of the poses. Then the normalized poses are mapped to a pose embedding space of highlevel features, learned via unsupervised metric learning. We evaluate the effectiveness of our normalized features both qualitatively by visualizations, and quantitatively by a video alignment task on the Human3.6M dataset and an action recognition task on the Penn Action dataset.
publication: 'ICCV 2021 Oral'
---
