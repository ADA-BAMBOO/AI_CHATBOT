# BBO_Training.ipynb - Overview

This notebook demonstrates the complete pipeline for building, training, and evaluating a Cardano-focused chatbot AI model. It covers every step from data collection and preprocessing to model fine-tuning, evaluation, and deployment.

---

## Key Features

### 1. Environment & Library Setup
- Installs all required Python libraries for NLP, deep learning, data processing, and web scraping.
- Supports Google Colab and Google Drive integration for easy data and model management.

### 2. Data Collection & Preprocessing
- Loads and processes data from various sources: Google Drive, Google Sheets, `.docx`, `.xlsx`, `.txt`, and web scraping.
- Cleans, deduplicates, and merges text data.
- Includes translation and sentence segmentation for multilingual sources.
- Merges short sentences to ensure context-rich training samples.

### 3. Synthetic QA Data Generation
- Automatically generates question-answer pairs from context using pre-trained models (T5 for question generation, Roberta for answer extraction).
- Paraphrases answers for diversity using BART.
- Batch processing for large-scale data creation.

### 4. Model Training Pipeline
- Fine-tunes large language models (LLaMA, BART, T5, Roberta, etc.) using LoRA/QLoRA for efficient training on consumer GPUs.
- Implements custom dataset classes and prompt formatting compatible with LLaMA-3 Instruct and ChatML-style prompts.
- Supports multi-GPU training, gradient checkpointing, and advanced training arguments.
- Integrates with HuggingFace Hub and Weights & Biases for model and experiment management.

### 5. Retrieval-Augmented Generation (RAG)
- Builds a vector store of context embeddings using `sentence-transformers`.
- Retrieves relevant context for each question during training and inference.
- Supports updating and saving RAG dictionaries for efficient retrieval.

### 6. Evaluation & Metrics
- Calculates Perplexity, Factual Accuracy, Hallucination Rate, and Relevance Score.
- Uses both embedding-based and Wikipedia-based methods for factuality and hallucination detection.
- Logs results to Excel reports for tracking model performance.

### 7. Model Saving & Export
- Saves trained models and tokenizers to Google Drive.
- Provides scripts to convert HuggingFace models to GGUF format for use with `llama.cpp` and local inference.
- Supports downloading and quantizing models for deployment on various hardware.

### 8. Inference & Chatbot Deployment
- Implements a chatbot interface for interactive Q&A using the fine-tuned model.
- Supports both context-aware (RAG) and context-free answering.
- Provides prompt templates and best practices for LLaMA-3 style chatbots.

---

## Example Workflow

1. **Install dependencies** and set up the environment.
2. **Collect and preprocess data** from multiple sources.
3. **Generate synthetic QA pairs** for training.
4. **Fine-tune the language model** with LoRA/QLoRA.
5. **Build and update RAG context embeddings**.
6. **Evaluate the model** using multiple metrics.
7. **Export and deploy the model** for inference or integration.

---

## Usage Notes

- **Hardware:** Designed for GPU environments (Google Colab recommended). Some steps require significant RAM and VRAM.
- **Customization:** Adaptable for other domains by changing data sources and prompt templates.
- **Dependencies:** All dependencies are installed at the top of the notebook. Google Drive and HuggingFace Hub access are required for full functionality.
- **Data Privacy:** Be cautious with sensitive data, especially when using third-party APIs or cloud storage.

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