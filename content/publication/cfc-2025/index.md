---
title: 'CFC: Simulating Character-Fluid Coupling using a Two-Level World Model'
authors:
- Zhiyang Dou
- Chen Peng
- Xinyu Lu
- Xiaohan Ye
- Lixing Fang
- Yuan Liu
- Wenping Wang
- Chuang Gan
- Lingjie Liu
- Taku Komura

date: '2025-12-01T00:00:00Z'
doi: '10.1145/3763318'

# Schedule page publish date (NOT publication's date).
# publishDate: '2024-08-01T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *ACM Transactions on Graphics (Proceedings of SIGGRAPH Asia 2025)*
publication_short: In *SIGGRAPH Asia 2025*

abstract: |
  Humans possess the ability to master a wide range of motor skills, using which they can quickly and flexibly adapt to the surrounding environment. Despite recent progress in replicating such versatile human motor skills, existing research often oversimplifies or inadequately captures the complex interplay between human body movements and highly dynamic environments, such as interactions with fluids. In this paper, we present a world model for Character-Fluid Coupling (CFC) for simulating human-fluid interactions via two-way coupling. We introduce a two-level world model which consists of a Physics-Informed Neural Network (PINN)-based model for fluid dynamics and a rigid body world model capturing body dynamics under various external forces. This hierarchical world model adeptly predicts the dynamics of fluid and its influence on rigid bodies, sidestepping the computational burden of fluid simulation and providing policy gradients for efficient policy training. Once trained, our system can control characters to complete high-level tasks while adaptively responding to environmental changes. We also present that the fluid initiates emergent behaviors of the characters, enhancing motion diversity and interactivity. Extensive experiments underscore the effectiveness of CFC, demonstrating its ability to produce high-quality, realistic human-fluid interaction animations.

# Summary. An optional shortened abstract.
# summary: 

tags:
- Physics-based Character Animation
- Fluid Simulation
- Deep Reinforcement Learning

featured: true

links:
# - name: Custom Link
#   url: https://github.com/sebastianstarke/AI4Animation
url_pdf: 'https://dl.acm.org/doi/10.1145/3763318'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: 'https://frank-zy-dou.github.io/projects/CFC/'
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'CFC'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: []`.
slides:

---

