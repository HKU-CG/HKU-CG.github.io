---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Neural Face Rigging for Animating and Retargeting Facial Meshes in the Wild'
subtitle: ''
summary: ''
authors:
- Dafei Qin
- Jun Saito
- Noam Aigerman
- Thibault Groueix
- Taku Komura


tags:
- 'Facial Rigging'
- 'Facial Animation'
- 'Retargeting'

categories: []
date: '2023-08-07'
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
abstract: We propose an end-to-end deep-learning approach for automatic rigging and retargeting of 3D models of human faces in the wild. Our approach, called Neural Face Rigging (NFR), holds three key properties\: (i) NFR's expression space maintains human-interpretable editing parameters for artistic controls;\n(ii) NFR is readily applicable to arbitrary facial meshes with different connectivity and expressions;\n(iii) NFR can encode and produce fine-grained details of complex expressions performed by arbitrary subjects.\n To the best of our knowledge, NFR is the first approach to provide realistic and controllable deformations of in-the-wild facial meshes, without the manual creation of blendshapes or correspondence. We design a deformation autoencoder and train it through a multi-dataset training scheme, which benefits from the unique advantages of two data sources\: a linear 3DMM with interpretable control parameters as in FACS, and 4D captures of real faces with fine-grained details. Through various experiments, we show NFR's ability to automatically produce realistic and accurate facial deformations across a wide range of existing datasets as well as noisy facial scans in-the-wild, while providing artist-controlled, editable parameters.
publication: 'SIGGRAPH 2023'
---
