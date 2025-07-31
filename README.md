# LLM Summarization A/B Testing Pipeline

This project implements a lightweight experiment framework to **compare the performance of different LLMs or prompts** for text summarization. The goal is to simulate a real-world A/B testing environment to evaluate summarization quality across versions — a critical skill for model iteration and deployment.

---

## 🎯 Objectives

- Demonstrate the design of a basic **A/B testing framework** for LLM outputs
- Evaluate summarization quality using **prompt variants or different models**
- Log outputs, performance metrics, and evaluation scores
- Provide a minimal, reproducible example of **ML experimentation mindset**

---

## 🧩 Key Features

- ✅ Compare two LLMs (e.g., `T5` vs `GPT2`) or prompt variants
- ✅ Process real or synthetic documents (e.g., news, policies)
- ✅ Output summaries side-by-side with rating or scoring options
- ✅ Optionally log results to `Weights & Biases` or CSV
- ✅ Modular notebook and CLI-ready structure

---

## 🏗 Tech Stack

- Python 3.10+
- Hugging Face Transformers (`T5-small`, `GPT2`, `BART`, etc.)
- `datasets` or `pandas` for inputs
- `wandb` or `csv` for logging
- Jupyter notebook or simple CLI runner

---

## 📁 Folder Structure

```
llm-summarization-ab/
│
├── data/               # Input texts to summarize
├── models/             # Model configs and tokenizers
├── ab_pipeline/        # Compare, evaluate, log
│   ├── summarize.py
│   ├── evaluate.py
│   └── logger.py
├── compare_summaries.ipynb
└── README.md
```

---

## ⚙️ Example Usage

```python
from ab_pipeline import summarize, evaluate

summary_a = summarize(text, model="t5-small", prompt_style="short")
summary_b = summarize(text, model="gpt2", prompt_style="long")

print("A:", summary_a)
print("B:", summary_b)
evaluate(summary_a, summary_b)
```

---

## 📊 Evaluation Metrics

- Length comparison
- ROUGE score (optional)
- Human rating or manual notes
- Logging output samples for qualitative review

---

## 🧪 Use Cases

- Fine-tuning prompt templates
- Comparing LLMs before deployment
- Building reproducible summary testing pipelines

---

## 🤝 Credits

Created by [Niosha Hejazi](https://www.linkedin.com/in/nioshahejazi)  
Designed as a portfolio project to demonstrate experimentation mindset in LLM-based summarization workflows.
