---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Surf-D: Generating High-Quality Surfaces of Arbitrary Topologies Using Diffusion Models'
subtitle: 'Equal contributions: Zhengming and Zhiyang'
summary: 
authors:
- Zhengming Yu
- Zhiyang Dou
- Xiaoxiao Long 
- Cheng Lin
- Zekun Li
- Yuan Liu 
- Norman Müller
- Taku Komura
- Marc Habermann
- Christian Theobalt
- Xin Li
- Wenping Wang

tags:
- 'Shape Generation'
- 'Shape Reconstruction'
- 'Topology'

categories: []
date: '2024-07-21'
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
abstract: We present Surf-D, a novel method for generating high-quality 3D shapes as Surfaces with arbitrary topologies using Diffusion models. Previous methods explored shape generation with different representations and they suffer from limited topologies and poor geometry details. To generate high-quality surfaces of arbitrary topologies, we use the Unsigned Distance Field (UDF) as our surface representation to accommodate arbitrary topologies. Furthermore, we propose a new pipeline that employs a point-based AutoEncoder to learn a compact and continuous latent space for accurately encoding UDF and support high-resolution mesh extraction. We further show that our new pipeline significantly outperforms the prior approaches to learning the distance fields, such as the grid-based AutoEncoder, which is not scalable and incapable of learning accurate UDF. In addition, we adopt a curriculum learning strategy to efficiently embed various surfaces. With the pretrained shape latent space, we employ a latent diffusion model to acquire the distribution of various shapes. Extensive experiments are presented on using Surf-D for unconditional generation, category conditional generation, image conditional generation, and text-to-shape tasks. The experiments demonstrate the superior performance of Surf-D in shape generation across multiple modalities as conditions.
publication: 'ECCV 2024'
---
