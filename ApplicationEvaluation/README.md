# Application Evaluation
## Overview
First key challenging in GenAI is its non-deterministic nature. Traditional assertion is not effective. We need different mechanism to evaluate the quality of GenAI application. AI Foundry introduction to Prompt flow starts by introduce tooling to support evaluation using metric such as Groundedness or Relevant. This has been particularly useful however it requires application implementation to have direct dependencies with Prompt flow and Python. This is not practical for all use cases. Azure Evaluation SDK has been proposed to decouple evaluation from applications implementation. 

Another challenge when working with Gen AI is having decent quality test data. Golden data set is particularly important to evaluate the quality of the GenAI application. It takes effort and normally require SMEs to generate quality Golden data set hence data set size tends to be limited and does not cover all use cases.

In this lab, you will learn how to run evaluators on manual data set, on an application target endpoint with built-in evaluators using the Azure AI Evaluation SDK then track the results and evaluation logs in Azure AI project. To extend the data set we will use AI Evaluation SDK to generate synthetic data set to enhance test coverage.

The application target endpoint will be provided. This is an RAG application that answer question related to[] Microsoft Responsible AI](Data/Microsoft-Responsible-AI-Standard-v2-General-Requirements-3.pdf) 

## Set up parameters
1. **Create a `.env` File under ApplicationEvaluation folder**  
- Store your Azure OpenAI configuration, AI Foundry details, and application credentials in separate key-value pairs.
```
AZURE_OPENAI_API_VERSION=2024-08-01-preview
AZURE_OPENAI_DEPLOYMENT=sample-deployment
AZURE_OPENAI_ENDPOINT=https://sample-aoai-endpoint.azure.com/
AZURE_OPENAI_KEY=sampleKey1234
AZURE_SUBSCRIPTION_ID=sample-subscription-id
AZURE_AI_FOUNDRY_RESOURCE_GROUP=sample-resource-group
AZURE_AI_FOUNDRY_PROJECT_NAME=sample-project
APPLICATION_ENDPOINT=https://sample-app-endpoint.azure.com/score # This will be provided via team channel
APPLICATION_KEY=sampleApplicationKey1234 # This will be provided via team channel
```

2. **Run `az login`**  
   - Use the Azure CLI to authenticate your account.
![Application Eval Diagram](applicationeval.png)

## Lab
The lab use a existing endpoint implemented in the application_endpoint.py. We have prepare a sample application to use. Please reach out to Ha Duong for end point detail.
If you want to use your own application endpoint then it is also possible with the same concept.

We have a set of note books for each scenario. Each notebook are independent from each other so you can choose to run 

| Notebook                                        | Description                                               |
|-------------------------------------------------|-----------------------------------------------------------|
|[Manual_Evaluation](Manual_Evaluation.ipynb)     | Application evaluation with golden data set               |
|[Simulate_Evaluation](Simulate_Evaluation.ipynb) | Generate and evaluate application with generate data set  |
