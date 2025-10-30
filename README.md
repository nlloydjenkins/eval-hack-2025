## Set up
### Setting up the Dev Container

1. **Install Docker**: Ensure you have Docker installed on your machine. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).

2. **Open the Project in VS Code**: Open the `/workspaces/chat-and-hack-feb-2025` directory in Visual Studio Code.

3. **Install Dev Containers**: Install the "Dev Containers" extension from the VS Code marketplace.

4. **Reopen in Container**: Press `F1`, then select `Dev Containers: Reopen in Container`. This will build the dev container as specified in the `.devcontainer` folder.

5. **Wait for Setup**: Wait for the container to build and set up. This may take a few minutes.

6. **Verify**: Once the container is running, verify that all necessary services are up and running inside the container.

   You can verify the following services using these commands:
   
   ```bash
   # Check Python version (Expected: Python 3.11.x or higher)
   python --version
   
   # Check if conda is available (Expected: conda 24.x.x or higher)
   conda --version
   
   # Check Azure CLI version (Expected: azure-cli 2.x.x or higher)
   az --version
   
   # Check if Node.js is available (Expected: v20.x.x or higher)
   node --version
   
   # Check if npm is available (Expected: 10.x.x or higher)
   npm --version
   
   # Check if Git is available (Expected: git version 2.x.x or higher)
   git --version
   ```

### Setting up with Python or Conda Environment 

Create a virtual Python environment of you choice. 
To create one using conda, run the following command in bash terminal
```
conda create -n model_eval
conda init bash
```
**Note:** After running `conda init bash`, you will need to restart your terminal or run `source ~/.bashrc` for the changes to take effect.

Then activate the environment:
```
conda activate model_eval
```
To create one using python in powershell, run the following command in powershell terminal
```
python -m venv model_eval
.\model_eval\Scripts\Activate.ps1
```
To create one using python in bash, run the following command in bash terminal
```
python -m venv .model_eval
source .model_eval/bin/activates
```

### Building and running

Install the required packages by running the following command:
```
pip install -r requirements.txt
```

### Setting up Azure OpenAI Instance

1. **Create an Azure Account**: If you don't have an Azure account, create one at [Azure's official website](https://azure.microsoft.com/).

2. **Create an Azure OpenAI Resource**:
    - Go to the [Azure Portal](https://portal.azure.com/).
    - Click on "Create a resource" and search for "Azure OpenAI".
    - Click "Create" and fill in the required details to set up your Azure OpenAI resource.

3. **Deploy a Model**:
    - Navigate to your Azure OpenAI resource in the Azure Portal.
    - Go to the "Model deployments" section or click "Go to Azure OpenAI Studio".
    - In Azure OpenAI Studio, click on "Deployments" in the left navigation.
    - Click "Create new deployment" to deploy a new model.
    - Choose the model you want to deploy (e.g., GPT-4, GPT-4o, GPT-3.5-Turbo) and configure the necessary settings.
    - Give your deployment a name and click "Create".

4. **Get Endpoint and Key**:
    - After deploying the model, return to the Azure Portal and navigate to your Azure OpenAI resource.
    - Go to the "Keys and Endpoint" section under "Resource Management".
    - Copy the endpoint URL and one of the API keys. You will need these for the labs.

### Setting up Azure AI Foundry

Azure AI Foundry is Microsoft's unified platform for building, evaluating, and deploying AI applications. It provides tools for model evaluation, prompt engineering, and AI safety assessment.

#### Why Use Azure AI Foundry?

- **Integrated Evaluation Tools**: Built-in evaluators for quality, safety, and performance metrics
- **Managed Identity Support**: Secure, keyless authentication to Azure resources
- **Centralized Asset Management**: Manage models, data, and deployments in one place
- **Enterprise-Ready**: Role-based access control and compliance features

#### Step 1: Create an Azure AI Foundry Hub and Project

**⚠️ IMPORTANT**: You must create a **Hub** (not just a project) to use AI-assisted evaluators like `GroundednessProEvaluator`, `RelevanceEvaluator`, and other Azure AI Evaluation SDK features. A Hub provides the full Azure ML workspace infrastructure required by these evaluators.

1. **Navigate to Azure AI Foundry**:
   - Go to the [Azure AI Foundry portal](https://ai.azure.com/).
   - Sign in with your Azure credentials.

2. **Create a New Hub**:
   - Click on "All hubs" in the left navigation or click "+ New hub" if this is your first time.
   - Click "Create new hub" (or "+ New hub").
   - Fill in the required details:
     - **Hub name**: Enter a descriptive name (e.g., `Eval-Hack-Hub`)
     - **Subscription**: Select your Azure subscription
     - **Resource group**: Create new or select an existing resource group (e.g., `Eval-Hack`)
     - **Location**: Choose a region close to you (e.g., `swedencentral`)
   - Click "Next" to review settings.
   - Click "Create" to provision the hub.
   
   **Note**: Creating a hub automatically provisions supporting resources including:
   - Azure AI Services
   - Storage Account
   - Key Vault
   - Container Registry (optional)
   - Application Insights (optional)

3. **Create a New Project**:
   - Once the hub is created, you'll be prompted to create a project, or click "+ New project".
   - Enter a project name (e.g., `Eval-Hack-Project`).
   - Optionally add a description.
   - Click "Create".
   
   **Note**: Your project will be created under the hub you just created. The project path will be `<HubName>/<ProjectName>` (e.g., `Eval-Hack-Hub/Eval-Hack-Project`).

#### Step 2: Enable and Configure Managed Identity

1. **Enable System-Assigned Managed Identity**:
   - In the [Azure Portal](https://portal.azure.com/), search for your AI Foundry hub resource (e.g., `AI-Eval-Hack`).
   - The resource type will be "Azure Machine Learning" or "AI Hub".
   - In the left navigation, under "Security + networking", click on "Identity".
   - Under the "System assigned" tab, toggle "Status" to "On".
   - Click "Save" and confirm when prompted.
   - **Copy the Object (principal) ID** that appears - you'll need this for role assignments.

#### Step 3: Grant Storage Access Roles

1. **Navigate to the Storage Account**:
   - In the Azure Portal, go to your resource group.
   - Find and click on the Storage Account that was created with your AI Foundry hub.
   - The storage account name typically follows the pattern: `<hubname><randomchars>`.

2. **Assign Storage Blob Data Contributor Role**:
   - In the storage account, click on "Access Control (IAM)" in the left navigation.
   - Click "+ Add" → "Add role assignment".
   - In the "Role" tab, search for and select "Storage Blob Data Contributor".
   - Click "Next".
   - In the "Members" tab, select "Managed identity".
   - Click "+ Select members".
   - In the "Managed identity" dropdown, select "Machine Learning" (or "AI Hub").
   - Select your hub's managed identity (e.g., `AI-Eval-Hack`).
   - Click "Select", then "Review + assign", then "Review + assign" again.

3. **Assign Storage File Data Privileged Contributor Role**:
   - Repeat the same process for the "Storage File Data Privileged Contributor" role:
   - Access Control (IAM) → Add role assignment → Search for "Storage File Data Privileged Contributor".
   - Select the role → Next → Managed identity → Select your hub's managed identity.
   - Review + assign.

#### Step 4: Enable Storage Account Key Access

1. **Configure Storage Account Settings**:
   - In your Storage Account, click on "Configuration" under "Settings" in the left navigation.
   - Find the "Allow storage account key access" setting.
   - Ensure it is set to "Enabled".
   - If you made changes, click "Save" at the top.

   ![Storage account key access setting](Lab1_ai_evaluation/media/storage_account_keys.png)

#### Step 5: Understanding the New Azure AI Foundry UI

The Azure AI Foundry interface has been redesigned (2025 layout). Key differences from older documentation:

- **"Linked Resources" is replaced** with two new sections:
  
  1. **Azure Portal - Resource Management**:
     - **Projects**: View and manage all projects within a hub
     - **Identity**: Configure managed identities and role assignments
     
  2. **Azure AI Foundry Portal - My Assets**:
     - **Data + indexes**: Upload datasets, create vector indexes
     - **Models + endpoints**: Deploy and manage model endpoints
     - **Prompt flow**: Build and test prompt workflows
     - **Evaluation**: Run evaluations and view metrics

#### Step 6: Verify Your Setup

##### Verify in Azure Portal:

1. **Check Hub Resource**:
   - Go to the [Azure Portal](https://portal.azure.com/).
   - Navigate to your resource group.
   - Confirm you see your AI Foundry hub resource (type: Azure Machine Learning).

2. **Verify Managed Identity**:
   - Open the hub resource.
   - Go to Identity → System assigned.
   - Confirm "Status" is "On" and note the Object ID.

3. **Verify Storage Roles**:
   - Open the Storage Account from your resource group.
   - Go to Access Control (IAM) → Role assignments.
   - Search for your hub's managed identity name.
   - Confirm it has both "Storage Blob Data Contributor" and "Storage File Data Privileged Contributor" roles.

4. **Verify Storage Configuration**:
   - In the Storage Account, go to Configuration.
   - Confirm "Allow storage account key access" is "Enabled".

##### Verify in Azure AI Foundry Portal:

1. **Access Your Project**:
   - Go to [Azure AI Foundry portal](https://ai.azure.com/).
   - Click on "All hubs" and select your hub (e.g., `AI-Eval-Hack`).
   - Click on your project (e.g., `Eval-Hack`).

2. **Test Data Access**:
   - In the left navigation, click on "Data + indexes".
   - If you can view this page without errors, your data access is configured correctly.
   - Optionally, try uploading a small test file to verify write access.

3. **Test Model Endpoints**:
   - In the left navigation, click on "Models + endpoints".
   - If you can view this page without errors, your endpoint access is configured correctly.
   - You should see any deployed models from your Azure OpenAI resource if connected.

4. **Verify Connected Resources**:
   - In your project, go to "Settings" or click on the project name.
   - Look for "Connected resources" or "Azure OpenAI".
   - Confirm your Azure OpenAI resource is listed.
   - If not, you may need to add it:
     - Click "+ Add connection" or "+ New connection".
     - Select "Azure OpenAI Service".
     - Choose your Azure OpenAI resource.
     - Configure authentication (API key or managed identity).
     - Click "Add" or "Create".

#### Troubleshooting Common Issues:

- **"Forbidden" or "Access Denied" errors**: 
  - Verify managed identity roles are correctly assigned to the storage account.
  - Wait 5-10 minutes after role assignment for permissions to propagate.
  
- **Cannot see Models + endpoints**:
  - Ensure your Azure OpenAI resource is connected to the project.
  - Check that models are deployed in Azure OpenAI Studio.

- **Storage access errors**:
  - Confirm "Allow storage account key access" is enabled.
  - Verify the managed identity has both required storage roles.

- **Changes not taking effect**:
  - Refresh the browser or clear cache.
  - Log out and log back into Azure AI Foundry portal.



