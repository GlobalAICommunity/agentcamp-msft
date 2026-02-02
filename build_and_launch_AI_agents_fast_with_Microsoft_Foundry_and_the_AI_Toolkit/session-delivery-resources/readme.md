## How to deliver this session

🥇 Thanks for delivering this session!

Prior to delivering the workshop please:

1.  Read this document and all included resources included in their entirety.
2.  Watch the video presentation
3.  Create a new GitHub issue if you have any questions or feedback.


## 📁 File Summary

| Resources          | Links                            | Description |
|-------------------|----------------------------------|-------------------|
| Session Delivery Deck     |  [Deck](../agentcamp_build_and_launch_AI_agents_fast_with_Microsoft_Foundry_and_the_AI_Toolkit.pptx/agentcamp_build_and_launch_AI_agents_fast_with_Microsoft_Foundry_and_the_AI_Toolkit.pptx) | The session delivery slides |
| Full Session | [Recording Link](https://youtu.be/3fFXFpAYC4M) | The full session presentation |

## 🕐Timing

The breakout is divided into multiple sections including 31 slides and 5 demos.

| Time        | Description 
--------------|-------------
0:00 - 3:04   | Intro and overview
3:05 - 4:19   | GenAI ops
4:20 - 12:20  | Meet the models
12:21 - 19:52 | Design your agent
19:53 - 31:15 | Evaluate your agent responses
31:16 - 38:35 | From prototype to production
38:36 - 40:15 | Wrap up and Q&A

## 🖥️Demo Videos

Select the demo name to view instructions for how to deliver the demo. A full transcript with timing is included for each demo. You can also find a copy of the full transcript within the speaker notes of the breakout slide deck.

| Demo        | Description | Video 
--------------|-------------|-------------
[Explore and Compare Models](./demos-instructions/01-explore-compare-models.md)   | Use **GitHub Copilot Agent Mode** to get model recommendations. Browse the **Model Catalog** in the AI Toolkit and compare 2 models within the **Model Playground**. | [Demo video](https://aka.ms/AAxqj4z)
[Create Agents with Agent Builder](./demos-instructions/02-create-agents.md)   | Create the Cora agent in the **Agent Builder** and define its system prompt. |  [Demo video](https://aka.ms/AAxq4rm)
[Add Tools to an Agent in Agent Builder](./demos-instructions/03-add-tools.md)   | Connect the Cora agent to the **Zava MCP server** and add the **get_products_by_name** tool. | [Demo video](https://aka.ms/AAxqc9k)
[Evaluate Agent Responses](./demos-instructions/04-evaluate-agent-responses.md)   |  Use **GitHub Copilot Agent Mode** to get evalator recommendations. Run both **manual** and **AI-assisted** evaluations for the agent output. | [Demo video](https://aka.ms/AAxqc9h)
[Export Agent Code](./demos-instructions/05-export-agent-code.md)   | Export the code from the **Agent Builder** for the Cora agent. Chat with the Cora agent live via the ageng UI. | [Demo video](https://aka.ms/AAxq4rl)

## 🏋️Prepare Your Environment

The demos for this breakout are designed to be run in a GitHub Codespaces for easy setup. The container includes the following:
- PostgresSQL dataset for Zava
- **Customer Sales Server** that does basic product search using traditional name-based matching
- A web app of the Cora agent app

### Prerequisites

#### Required Accounts

- [Azure](https://signup.azure.com/) subscription
- [GitHub](https://www.github.com) with a [GitHub Copilot](https://github.com/github-copilot/signup) subscription

#### Development Environment (for local setup)

- [Python 3.10](https://www.python.org/downloads/) (or higher)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli-windows?view=azure-cli-latest&pivots=winget) - Used for Azure authentication and resource management
- [Visual Studio Code](https://code.visualstudio.com/download)
  - [AI Toolkit](https://aka.ms/AIToolkit) extension
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension
  - [Azure Resources](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureresourcegroups) extension
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
- [Microsoft Foundry](https://ai.azure.com) project (created with the **new** Foundry experience)
  - **GPT-4.1-mini** model deployment

### Setup the Demo

**Open the repository in the GitHub Codespaces**

The recommended approach to run this session demos is using **GitHub Codespaces** - a cloud-hosted development environment with all the necessary tools and dependencies pre-installed as per configuration files embedded in this repo. This will allow you to focus on learning and prototyping without worrying about local setup.

To launch a codespace you need a **GitHub account**. If you do not have one, you can create a free account at [https://github.com/signup](https://github.com/signup).

1. From the GitHub repository landing page, click on the green **Code** button and select **Create codespace on main** from the **Codespaces** tab.

    ![Create Codespace](../../img/create_codespace.png)

> [!WARNING]
> The codespace creation process might take a few minutes, as all the necessary dependencies and tools are being set up in the cloud environment.

2. Once the codespace is created, you'll see a Visual Studio Code environment loaded in your browser.

3. You might choose to continue working in the browser or click on the **Open in VS Code** button to open it in the desktop application (recommended option).

    ![Open in VS Code](../../img/open_in_vscode.png)


**Confirm extensions are installed**

Confirm that the codespace has installed the following extensions:
- [Azure Resources](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureresourcegroups)
- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [AI Toolkit](https://aka.ms/AIToolkit)

If any extension is missing, install before moving forward.

> [!NOTE]
> The [Microsoft Foundry](https://marketplace.visualstudio.com/items?itemName=TeamsDevApp.vscode-ai-foundry) extension is installed as a bundle with the [AI Toolkit](https://aka.ms/AIToolkit). The [Azure Resources](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureresourcegroups) extension is installed as a bundle with the [Microsoft Foundry](https://marketplace.visualstudio.com/items?itemName=TeamsDevApp.vscode-ai-foundry) extension.

**Deploy Azure Resources to your Azure subscription**

To execute this session demos you will need to create a Microsoft Foundry project with the **gpt-4.1-mini** model deployed.
You can use the following button to deploy the required resources:[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FGlobalAICommunity%2Fagentcamp-msft%2Frefs%2Fheads%2Fmain%2Finfra%2Farm_template.json).

> [!IMPORTANT]
> Microsoft Foundry requires an Azure subscription. A **free trial** provides $200 credit for 30 days. Some features may incur costs after the trial. Check the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) to estimate costs.

> [!WARNING]
> **Free Tier Limitations:** The Azure free subscription has significant constraints that may prevent full implementation of this challenge:
> - **Model access:** Some advanced models (e.g., GPT-5, Claude) may not be available or have very limited quotas
> - **Rate limits:** Strict API call limits (e.g., requests per minute, tokens per day)
> - **Region restrictions:** Free tier resources may only be available in limited regions
> - **Feature restrictions:** Some Microsoft Foundry features (agent orchestration, evaluations) may require pay-as-you-go
> - **Credit exhaustion:** $200 credit can be consumed quickly with heavy AI model usage

> [!NOTE]
> If you are delivering this session in the context of the [AgentCamp 2026](https://globalai.community/agentcamp) series of events held by the Global AI Community, you might be eligible to redeem a time-limited sponsored Azure subscription. Pls refer to your local Global AI Chapter leads for more details.

**Sign-in to the Azure Resources extension and set your default project.**

1. In the **Azure Resources** extension, select **Sign in to Azure**.
1. Sign-in to the account that has your Microsoft Foundry project and GPT-4.1-mini deployed model.
1. Once signed in, expand your subscription in the **Azure Resources** extension and then expand **Microsoft Foundry**.
1. Right click your Microsoft Foundry project name and selct **Open in Microsoft Foundry Extension**. This action sets the default project.
1. If your project is **not** set as the default project, hover over the project name in the **Microsoft Foundry** extension and click the **Switch Default Project in Azure Extension** icon (*note: the icon looks like 3 lines and is only visble when hovering over the project name*).
1. In the **Pick a project** window, select the subscription that has your Microsoft Foundry project.
1. In the **Pick a project** window, select your Microsoft Foundry project.

**Authenticate via the Azure CLI**

1. Open the terminal in Visual Studio Code.
1. Run the command `az login` or `az login --tenant {your tenant} --use-device-code`.
1. Copy the code the terminate and navigate to the URL provided.
1. Enter the code.
1. Sign-in to the same tenant used to create your Microsoft Foundry project.
1. In the Visual Studio Code terminal, select your subscription.

**Setup environment variables**
1. In the terminal, run the command: `cp .env.example .env`
1. Open your new `.env` file.
1. Update the placeholder for `AZURE_AI_FOUNDRY_ENDPOINT="<your_Microsoft_Foundry_endpoint>"` (*note: you can locate the **project endpoint** on the welcome screen of the new Microsoft Foundry experience; ex: https://{foundry-resource-name}.services.ai.azure.com/api/projects/{project-name}*)

**Start the Customer Sales Server**

1. Navigate to the **.vscode/mcp.json** file.
1. Click **Start** above the **zava-customer-sales-stdio** server.

**Start the Cora web app**

1. In the terminal, run the command `python src/python/web_app/web_app.py`.
1. In the browser, navigate to [https://localhost:8000](http://localhost:8000).
1. Confirm that the green **Connected** label displays in the top-right of the UI.

**Tips for running demos on stage**

This session includes multiple demos and walking through each steps live might be time consuming. Consider using the 'Save version' functionality of the AI Toolkit to save different versions of your agent and quickly switch between them during the demo.
You can find the 'Save version' button by scrolling to the bottom of the left pane in the Agent Builder.
