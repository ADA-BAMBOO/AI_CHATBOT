# I. Evaluate API Deployment

This section provides a detailed guide to deploy and run the Evaluate API in this repository.

---

## 1. System Requirements

- **Python**: Version 3.10 or higher
- **pip**: Python package manager
- **Git** (optional, for cloning the repository)
- **CUDA 12.1** (if using GPU with PyTorch CUDA support)

---

## 2. Clone the Repository

If you haven't already, clone the repository to your local machine:

```sh
git clone <your-repo-url>
cd Evaluate_git/Evaluate_Source
```

---

## 3. Install Dependencies

Install all required Python packages using the provided `requirements.txt` file:

```sh
pip install -r requirements.txt
```

> **Note:**  
> The API will also attempt to install dependencies automatically when you run it, but it is recommended to install them manually first to avoid permission issues.

For GPU support with PyTorch (CUDA 12.1), run:

```sh
pip install torch==2.3.1+cu121 torchvision==0.18.1+cu121 torchaudio==2.3.1+cu121 -f https://download.pytorch.org/whl/torch_stable.html
```

---

## 4. Run the API

Start the API server using the following command:

```sh
python main.py
```

- The server will start on `0.0.0.0:2222` by default.

---

## 5. Access the API

- **API Root:**  
  [http://127.0.0.1:2222](http://127.0.0.1:2222)

- **Swagger UI (API Documentation):**  
  [http://127.0.0.1:2222/docs](http://127.0.0.1:2222/docs)


---

## 6. Example Request

You can test the API using Swagger UI or with a tool like `curl` or Postman.

**Sample JSON:**
```json
{
  "question": "What is the capital of France?",
  "bot_answer": "Paris",
  "real_answer": "Paris"
}
```

**Sample curl command:**
```sh
curl -X POST "http://127.0.0.1:2222/evaluate/" ^
     -H "Content-Type: application/json" ^
     -d "{\"question\":\"What is the capital of France?\",\"bot_answer\":\"Paris\",\"real_answer\":\"Paris\"}"
```

---

## 7. Notes

- Ensure you are in the `Evaluate_Source` directory when running commands.
- If you want to change the port or host, modify the `uvicorn.run` parameters in `main.py`.
- The API will attempt to install dependencies at runtime, but pre-installing them is recommended.
- For GPU acceleration, ensure your system has CUDA 12.1 installed and compatible drivers.

---

## 8. Troubleshooting

- **Dependency Issues:**  
  Make sure all packages in `requirements.txt` are installed successfully.
- **Port Already in Use:**  
  Change the port in `main.py` if `2222` is occupied.
- **CUDA Errors:**  
  Verify your CUDA installation and driver compatibility.

---

## 9. Directory Structure

```
Evaluate_git/
└── Evaluate_Source/
    ├── main.py
    ├── requirements.txt
    ├── Evaluate/
    │   └── ... (your evaluation logic)
    └── ...
```

---

## 10. Contact

For further support, please open an issue in this

# II. N8n Automation Evaluate Deployment

This section explains how to deploy and use the N8n automation workflow for evaluation, using the provided JSON workflow file in the `N8N` directory.

---

## 1. Prerequisites

- **N8n**: Installed locally or accessible via cloud ([N8n installation guide](https://docs.n8n.io/getting-started/installation/))
- Access to Google Sheets and necessary API credentials
- (Optional) Access to other services referenced in the workflow (e.g., Supabase, Postgres, Gemini API)

---

## 2. Import the Workflow

1. Open your N8n instance in the browser.
2. Go to the **Workflows** section.
3. Click **Import** and select the file [`N8N/evaluate.json`](N8N/evaluate.json).
4. The workflow will appear in your list. Review and update any credentials or connections as needed.
---

## 3. Configure Credentials

- Set up credentials for:
  - **Google Sheets** (OAuth2)
  - **Supabase** (if used)
  - **Postgres** (if used)
  - **Google Gemini API** (if used)
- Assign the correct credentials to each node in the workflow.

---

## 4. Workflow Overview

The workflow automates the following steps:
- Reads questions and answers from a Google Sheet.
- Uses an AI agent to generate answers.
- Sends requests to the Evaluate API (`/evaluate/` endpoint).
- Appends evaluation results (BLEU, Factual Accuracy, etc.) to another Google Sheet.
- Optionally interacts with vector stores and embedding models for advanced evaluation.
---

## 5. Running the Workflow

- Trigger the workflow manually or set up an automated trigger (e.g., schedule, webhook).
- Monitor execution in the N8n UI.
- Results will be written to the configured output Google Sheet.

---

## 6. Customization

- Update Google Sheet IDs and sheet names in the workflow nodes as needed.
- Adjust API endpoint URLs if your Evaluate API is running on a different host or port.
- Modify mapping and logic to fit your data structure or evaluation requirements.

---

## 7. Troubleshooting

- **Credential Errors:** Ensure all required credentials are set up and assigned.
- **API Connection Issues:** Verify the Evaluate API is running and accessible from N8n.
- **Google Sheets Errors:** Check permissions and sharing settings for the sheets.

---

## 8. References

- [N8n Documentation](https://docs.n8n.io/)
- [N8n Google Sheets Integration](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/)
- [N8n API Request Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.httprequest/)