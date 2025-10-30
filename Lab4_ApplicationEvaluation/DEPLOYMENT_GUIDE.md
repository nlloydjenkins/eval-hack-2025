# Creating Your Own Application Endpoint for Lab 4

Since the shared APPLICATION_ENDPOINT is not available, you have several options:

## Option 1: Use Mock Endpoint (Fastest - For Learning)

We've created a mock endpoint that simulates a RAG application without needing any deployment.

**To use the mock endpoint:**

1. In `Manual_Evaluation.ipynb`, find this line:
   ```python
   from application_endpoint import ApplicationEndpoint
   ```

2. Change it to:
   ```python
   from application_endpoint_mock import ApplicationEndpoint
   ```

3. You don't need APPLICATION_ENDPOINT or APPLICATION_KEY in your `.credentials.env`

4. Run the evaluation - it will use simulated responses

**Pros:** Fast, no Azure resources needed, great for learning the evaluation framework
**Cons:** Not testing a real application, responses are simple keyword-based

---

## Option 2: Deploy Your Own RAG Application to Azure

To create a real RAG application endpoint, you have several options:

### 2A. Deploy with Azure AI Foundry (Recommended)

1. **Go to Azure AI Foundry** (https://ai.azure.com)

2. **Navigate to your project** (Eval-Hack-Project)

3. **Create a Prompt Flow:**
   - Go to "Prompt flow" → "Create"
   - Choose "Chat with your data" template
   - Upload the Microsoft Responsible AI PDF from `Lab4_ApplicationEvaluation/Data/`
   - Configure with your Azure OpenAI deployment (gpt-4.1 or gpt-5-mini)

4. **Deploy the flow:**
   - Test it in the playground
   - Click "Deploy" → "Real-time endpoint"
   - Give it a name (e.g., "rag-eval-endpoint")
   - Wait for deployment (5-10 minutes)

5. **Get the endpoint details:**
   - Go to "Deployments" → Your deployment
   - Copy the "REST endpoint" URL
   - Copy the "Primary key"

6. **Update `.credentials.env`:**
   ```
   APPLICATION_ENDPOINT="<your-endpoint-url>"
   APPLICATION_KEY="<your-primary-key>"
   ```

### 2B. Deploy with Azure Machine Learning

1. **Create a managed endpoint:**
   ```bash
   az ml online-endpoint create --name rag-eval-endpoint
   ```

2. **Deploy your model/application:**
   - Package your RAG app as a deployment
   - Deploy to the endpoint
   - Get endpoint URL and key

### 2C. Deploy to Azure Container Apps or App Service

If you have a containerized RAG application:

1. **Deploy to Azure Container Apps:**
   ```bash
   az containerapp create \
     --name rag-eval-app \
     --resource-group Eval-Hack \
     --image your-rag-image:latest \
     --target-port 80
   ```

2. **Get the URL and configure authentication**

---

## Option 3: Use Azure OpenAI Directly (Simplified)

You can modify `application_endpoint.py` to call Azure OpenAI directly instead of a deployed RAG app:

```python
from openai import AzureOpenAI
import os

class ApplicationEndpoint:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
            api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT")
        )
        
    def __call__(self, query: str, context: str = ""):
        response = self.client.chat.completions.create(
            model=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
            messages=[
                {"role": "system", "content": "You are an expert on Microsoft Responsible AI."},
                {"role": "user", "content": query}
            ]
        )
        
        return {
            "query": query,
            "response": response.choices[0].message.content
        }
```

---

## Recommendation

For learning purposes, **start with Option 1 (Mock Endpoint)**. It lets you understand how the evaluation framework works without deployment complexity.

If you want to evaluate a real application, **Option 2A (Azure AI Foundry)** is the easiest path to deploy a proper RAG application.
