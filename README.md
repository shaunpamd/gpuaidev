# AI Developer Hub

Welcome to the **AI Developer Hub** repository! This project contains Jupyter Notebook tutorials and guides for training, fine-tuning, and inference using popular machine learning frameworks on AMD GPUs.

## Repository Structure

The tutorials are organized into three main categories:

- **Fine-Tuning**: Examples and guides for fine-tuning machine learning models.
- **Pretraining**: Tutorials on pretraining models from scratch.
- **Inference**: Resources for running inference with trained models.

### Directory Layout

```
github_repo/
├── docs/                          # Documentation for the tutorials
│   ├── index.md                   # Main documentation index
│   ├── fine_tune.md               # Fine-tuning tutorials index
│   ├── pretrain.md                # Pretraining tutorials index
│   ├── inference.md               # Inference tutorials index
│   └── notebooks/                 # Jupyter notebooks organized by category
│       ├── fine_tune/             # Fine-tuning notebooks
│       ├── pretrain/              # Pretraining notebooks
│       └── inference/             # Inference notebooks
```

### Getting Started


# Build and View Documentation Locally

This guide explains how to set up and view the documentation locally.

## Prerequisites

- Python 3.6 or later
- A virtual environment (recommended)

## Setup Instructions

1. **Clone the repository** and navigate to the `sphinx` directory:
   ```bash
   git clone <repository-url>
   cd gpuaidev-docs/docs/sphinx
   ```

2. **Activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install `pip-tools`**:
   ```bash
   pip install pip-tools
   ```

4. **Compile dependencies**:
   ```bash
   pip-compile requirements.in
   ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.in
   ```

6. **Build the documentation**:
   ```bash
   make html
   ```

7. **View the documentation locally**:
   Open the `build/index.html` file in your browser.

## Notes

- Ensure all dependencies are installed successfully.
- The `build/index.html` file contains the generated documentation in HTML format.
