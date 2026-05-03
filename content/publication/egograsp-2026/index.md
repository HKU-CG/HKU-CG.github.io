---
title: 'EgoGrasp: World-Space Hand-Object Interaction Estimation from Egocentric Videos'
authors:
- Hongming Fu
- Wenjia Wang
- Xiaozhen Qiao
- Rolandos Alexandros Potamias
- Taku Komura
- Shuo Yang
- Zheng Liu
- Bo Zhao

date: '2026-02-01T00:00:00Z'

# Schedule page publish date (NOT publication's date).
# publishDate: '2024-08-01T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['3']

# Publication name and optional abbreviated publication name.
publication: arXiv Preprint
publication_short: arXiv Preprint

abstract: |
  We propose EgoGrasp, the first method to reconstruct world-space hand-object interactions (W-HOI) from dynamic egoview videos, supporting open-vocabulary objects. Accurate W-HOI reconstruction is critical for embodied intelligence yet remains challenging. Existing HOI methods are largely restricted to local camera coordinates or single frames, failing to capture global temporal dynamics. While some recent approaches attempt world-space hand estimation, they overlook object poses and HOI constraints. Moreover, previous HOI estimation methods either fail to handle open-set categories due to their reliance on object templates or employ differentiable rendering that requires per-instance optimization, resulting in prohibitive computational costs. Finally, frequent occlusions in egocentric videos severely degrade performance. To overcome these challenges, we propose a multi-stage framework: (i) a robust pre-processing pipeline leveraging vision foundation models for initial 3D scene, hand and object reconstruction; (ii) a body-guided diffusion model that incorporates explicit egocentric body priors for hand pose estimation; and (iii) an HOI-prior-informed diffusion model for hand-aware 6DoF pose infilling, ensuring physically plausible and temporally consistent W-HOI estimation. We experimentally demonstrate that EgoGrasp can achieve state-of-the-art performance in W-HOI reconstruction, handling multiple and open vocabulary objects robustly.

# Summary. An optional shortened abstract.
# summary: 

tags:
- Hand-Object Interaction
- 3D Reconstruction
- Egocentric Vision

featured: true

links:
# - name: Custom Link
#   url: https://github.com/sebastianstarke/AI4Animation
url_pdf: 'https://arxiv.org/abs/2601.01050'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: 'https://mint-sjtu.github.io/EgoGrasp.io'
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'EgoGrasp'
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

