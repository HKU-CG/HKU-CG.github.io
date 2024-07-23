---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'EMDM: Efficient Motion Diffusion Model for Fast and High-Quality Motion Generation'
subtitle: 'Project Lead: Zhiyang Dou'
summary: 
authors:
- Wenyang Zhou
- Zhiyang Dou
- Zeyu Cao
- Zhouyingcheng Liao
- Jingbo Wang
- Wenjia Wang
- Yuan Liu
- Taku Komura
- Wenping Wang
- Lingjie Liu


tags:
- '3D human motion generation'
- 'Diffusion Model'

categories: []
date: '2024-07-22'
lastmod: 2024-07-22T21:34:50Z
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
publishDate: '2024-07-22T21:34:50.388741Z'
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
abstract: We introduce Efficient Motion Diffusion Model (EMDM) for fast and high-quality human motion generation. Current state-of-the-art generative diffusion models have produced impressive results but struggle to achieve fast generation without sacrificing quality. On the one hand, previous works, like motion latent diffusion, conduct diffusion within a latent space for efficiency, but learning such a latent space can be a non-trivial effort. On the other hand, accelerating generation by naively increasing the sampling step size, e.g., DDIM, often leads to quality degradation as it fails to approximate the complex denoising distribution. To address these issues, we propose EMDM, which captures the complex distribution during multiple sampling steps in the diffusion model, allowing for much fewer sampling steps and significant acceleration in generation. This is achieved by a conditional denoising diffusion GAN to capture multimodal data distributions among arbitrary (and potentially larger) step sizes conditioned on control signals, enabling fewer-step motion sampling with high fidelity and diversity. To minimize undesired motion artifacts, geometric losses are imposed during network learning. As a result, EMDM achieves real-time motion generation and significantly improves the efficiency of motion diffusion models compared to existing methods while achieving high-quality motion generation. Our code is available at \url{https://github.com/Frank-ZY-Dou/EMDM}.
publication: 'ECCV 2024'
---
