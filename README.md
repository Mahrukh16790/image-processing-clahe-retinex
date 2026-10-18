# Image Processing: CLAHE & Retinex Contrast Enhancement

Contrast-enhancement pipelines in Python for diagnostic imaging — developed during the **GTAU (Großtieraugendiagnose)** research project at ICM e.V. Chemnitz, focused on large-animal eye diagnostics.

## 🎯 Problem

Diagnostic images often suffer from poor or uneven contrast, which makes automated and manual analysis unreliable. The goal: build reproducible enhancement pipelines that improve image contrast while preserving diagnostically relevant detail.

## 🔬 Approach

Two complementary enhancement techniques, implemented with OpenCV and NumPy:

1. **CLAHE** (Contrast Limited Adaptive Histogram Equalization) — local contrast enhancement with clipping to avoid noise amplification.
2. **Retinex** (Single/Multi-Scale) — illumination normalization that separates reflectance from lighting, improving visibility in unevenly lit images.

An automated **contrast-comparison workflow** evaluates both methods side by side (contrast metrics, before/after visualizations), increasing reproducibility of the enhancement step.

## 📁 Structure

```
├── notebooks/
│   └── 01_contrast_enhancement_walkthrough.ipynb  # end-to-end demo on sample images
├── src/
│   └── enhancement.py                             # CLAHE + Retinex implementations
├── requirements.txt
└── README.md
```

## 🚀 How to run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_contrast_enhancement_walkthrough.ipynb
```

## 📊 Results (from the GTAU project)

- Automated contrast-comparison workflows → **+25% reproducibility** of the enhancement pipeline
- Enhancement parameters tuned per imaging condition rather than hand-picked per image

## 🛠️ Tech

Python · OpenCV · NumPy · Matplotlib · Jupyter

## 🔜 Next steps

- [ ] Benchmark against additional enhancement baselines (histogram equalization, gamma correction)
- [ ] Add quantitative evaluation (EME, AMBE metrics) to the comparison workflow
- [ ] Package as an installable module with CLI
