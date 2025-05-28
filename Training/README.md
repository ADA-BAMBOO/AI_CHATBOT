# BBO_Training.ipynb Overview

## Purpose

`BBO_Training.ipynb` is a comprehensive Jupyter Notebook that demonstrates the full pipeline for building, training, and evaluating a chatbot AI model specialized in the Cardano blockchain. The notebook is designed for use in Google Colab and leverages both open-source and proprietary tools to automate data processing, model training, and evaluation.

---

## Main Features

### 1. Library Installation & Environment Setup
- Installs all required Python libraries for data processing, web scraping, NLP, and deep learning (e.g., `transformers`, `torch`, `sentence-transformers`, `bitsandbytes`, `peft`, `llama-cpp-python`, etc.).
- Includes setup for Google Colab and Google Drive integration for data storage and model checkpoints.

### 2. Data Collection & Preprocessing
- Supports importing data from multiple sources: Google Drive, Google Sheets, `.docx`, `.xlsx`, `.txt`, and web scraping.
- Provides utilities for extracting and cleaning text from documents and web pages.
- Includes translation and sentence segmentation for multilingual data.
- Merges and normalizes text data for downstream processing.

### 3. Synthetic Data Generation (QA Pairs)
- Automatically generates question-answer pairs from context paragraphs using pre-trained models (e.g., T5 for question generation, Roberta for answer extraction).
- Paraphrases answers for diversity using models like BART.
- Supports batch processing and customization of data generation parameters.

### 4. Model Training Pipeline
- Fine-tunes large language models (LLaMA, BART, T5, Roberta, etc.) using LoRA/QLoRA for efficient training on consumer GPUs.
- Implements custom dataset classes and prompt formatting compatible with LLaMA-3 Instruct and ChatML-style prompts.
- Supports multi-GPU training, gradient checkpointing, and advanced training arguments.
- Integrates with HuggingFace Hub for model management and Weights & Biases for experiment tracking.

### 5. Retrieval-Augmented Generation (RAG)
- Builds a vector store of context embeddings using `sentence-transformers`.
- Retrieves relevant context for each question during training and inference.
- Supports updating and saving RAG dictionaries for efficient retrieval.

### 6. Evaluation & Metrics
- Calculates key evaluation metrics: Perplexity, Factual Accuracy, Hallucination Rate, and Relevance Score.
- Uses both embedding-based and Wikipedia-based methods for factuality and hallucination detection.
- Logs results to Excel reports for tracking model performance over time.

### 7. Model Saving & Export
- Saves trained models and tokenizers to Google Drive.
- Provides scripts to convert HuggingFace models to GGUF format for use with `llama.cpp` and local inference.
- Supports downloading and quantizing models for deployment on various hardware.

### 8. Inference & Chatbot Deployment
- Implements a chatbot interface for interactive Q&A using the fine-tuned model.
- Supports both context-aware (RAG) and context-free answering.
- Provides prompt templates and best practices for LLaMA-3 style chatbots.

---

## Usage Notes

- **Hardware:** Designed for GPU environments (Google Colab recommended). Some steps require significant RAM and VRAM.
- **Customization:** You can adapt the notebook for other domains by changing the data sources and prompt templates.
- **Dependencies:** All dependencies are installed at the top of the notebook. Ensure you have access to Google Drive and HuggingFace Hub for full functionality.
- **Data Privacy:** Be cautious with sensitive data, especially when using third-party APIs or cloud storage.

---

## Typical Workflow

1. **Install dependencies** and set up the environment.
2. **Collect and preprocess data** from various sources.
3. **Generate synthetic QA pairs** for training.
4. **Fine-tune the language model** with LoRA/QLoRA.
5. **Build and update RAG context embeddings**.
6. **Evaluate the model** using multiple metrics.
7. **Export and deploy the model** for inference or integration.

---

## Example Applications

- Building a domain-specific chatbot for Cardano or other blockchain projects.
- Automating the creation of QA datasets from unstructured documents.
- Research on retrieval-augmented generation and factuality in LLMs.
- Educational purposes for understanding the end-to-end NLP model training pipeline.

---

## File Structure

- **BBO_Training.ipynb**: Main notebook (this file)
- **/data/**: Folder for raw and processed data
- **/models/**: Folder for saving trained models and checkpoints
- **/scripts/**: Utility scripts for conversion and deployment

---

## Author & Contact

For questions, feedback, or contributions, please open an issue or contact the repository maintainer.

---