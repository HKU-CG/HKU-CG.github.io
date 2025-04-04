---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization'
subtitle: 
summary: 
authors:
- Liang Pan
- Zeshi Yang
- Zhiyang Dou
- Wenjia Wang
- Buzhen Huang
- Bo Dai
- Taku Komura
- Jingbo Wang


tags:
- 'Physics-based Character Animation'
- 'RL'

categories: []
date: '2025-03-01'
lastmod: 2025-03-01T21:34:50Z
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
publishDate: '2025-01-01T21:34:50.388741Z'
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
abstract: The synthesis of realistic and physically plausible human-scene interaction animations presents a critical and complex challenge in computer vision and embodied AI. Recent advances primarily focus on developing specialized character controllers for individual interaction tasks, such as contacting and carrying, often overlooking the need to establish a unified policy for versatile skills. This limitation hinders the ability to generate high-quality motions across a variety of challenging human-scene interaction tasks that require the integration of multiple skills, e.g., walking to a chair and sitting down while carrying a box. To address this issue, we present TokenHSI, a unified controller designed to synthesize various types of human-scene interaction animations. The key innovation of our framework is the use of tokenized proprioception for the simulated character, combined with various task observations, complemented by a masking mechanism that enables the selection of tasks on demand. In addition, our unified policy network is equipped with flexible input size capabilities, enabling efficient adaptation of learned foundational skills to new environments and tasks. By introducing additional input tokens to the pre-trained policy, we can not only modify interaction targets but also integrate learned skills to address diverse challenges. Overall, our framework facilitates the generation of a wide range of character animations, significantly improving flexibility and adaptability in human-scene interactions.
publication: 'CVPR 2025'
---
