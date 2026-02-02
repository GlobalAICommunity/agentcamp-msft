# Global AI AgentCamp - Building AI Agents with Microsoft Foundry and the AI Toolkit

This repository contains comprehensive resources to deliver either a breakout session or a hands-on workshop for building AI agents using the **AI Toolkit for Visual Studio Code** and **Microsoft Foundry**. The content is designed for developers looking to prototype, develop, and deploy enterprise-ready intelligent agents efficiently.

## 📚 What's Included

This repository provides two complete learning experiences:

### 1. **Breakout Session** (45 minutes, Level 200)
A speaker-led demonstration session with comprehensive delivery resources.

**Location:** [`build_and_launch_AI_agents_fast_with_Microsoft_Foundry_and_the_AI_Toolkit/`](build_and_launch_AI_agents_fast_with_Microsoft_Foundry_and_the_AI_Toolkit/)

**What's Included:**

- 📊 Presentation slides with speaker notes
- 📝 Step-by-step demo instructions
- 🎯 Five progressive demonstrations with back-up video recordings

**Getting Started:** Review the [session delivery resources](build_and_launch_AI_agents_fast_with_Microsoft_Foundry_and_the_AI_Toolkit/session-delivery-resources/readme.md) for detailed setup and delivery instructions.

---

### 2. **Hands-On Workshop** (75 minutes, Level 200)

An interactive, self-paced lab experience for participants to build their own multimodal agents.

**Location:** [`prototyping-multimodal-agents-with-microsoft-foundry-and-the-ai-toolkit/`](prototyping-multimodal-agents-with-microsoft-foundry-and-the-ai-toolkit/)

**What's Included:**

- 🚀 Complete step-by-step lab manual with screenshots

**Getting Started:** Start with the [introduction](prototyping-multimodal-agents-with-microsoft-foundry-and-the-ai-toolkit/instructions/00_Introduction.md) and follow the numbered modules.
---

## 🛠️ Technologies Covered

- **AI Toolkit for VS Code** - Unified interface for AI model development
- **Microsoft Foundry** - Enterprise-grade AI platform
- **Model Context Protocol (MCP)** - Standard protocol enabling agents to access external data and tools
- **Python** - Primary development language
- **PostgreSQL with pgvector** - Database with vector search capabilities

## 📂 Repository Structure

```
├── README.md                                          # This file
├── src/                                               # Shared source code
│   ├── python/                                        # Python implementations
│   │   ├── mcp_server/                               # MCP server implementations
│   │   │   └── customer_sales/                       # Customer sales tools
│   │   └── web_app/                                  # Web application
│   └── frontend/                                      # Frontend HTML/static files
│       └── static/                                    # Static assets
├── data/                                              # Sample datasets
├── img/                                               # Documentation images
├── infra/                                             # Infrastructure templates
├── scripts/                                           # Database Setup scripts
├── docker-compose.yml                                 # Database setup
├── build_and_launch_AI_agents_fast_with_Microsoft_Foundry_and_the_AI_Toolkit/
│   └── session-delivery-resources/                   # Breakout session materials
└── prototyping-multimodal-agents-with-microsoft-foundry-and-the-ai-toolkit/
    └── instructions/                                  # Workshop lab materials
```

## 💻 Shared Codebase

The repository includes a complete implementation of the **Zava Retail** scenario used across both sessions:

### Web Application (`src/python/web_app/`)

A chat-like web application that demonstrates how to interface with the **Cora agent**, an AI assistant that helps Zava customers discover products through natural conversation. The webapp showcases:

- Real-time chat interface with the agent
- Integration with Microsoft Foundry models
- MCP tool integration for product search
- Multi-modal interactions (text and images)

You can use it in your delivery to demonstrate the final agent experience you are aiming to build.

### Database (`data/database/`)

PostgreSQL database with pgvector extension hosting the **Zava Products Catalog**:

- 100+ product records with descriptions, pricing, and categories
- Vector embeddings for semantic product search
- Row-level security (RLS) configuration for multi-tenant scenarios
- Sample data and backup files for quick setup

### MCP Server (`src/python/mcp_server/customer_sales/`)

A Model Context Protocol (MCP) server implementation that exposes tools for:

- **Semantic product search** - Natural language queries across the product catalog
- **Product filtering** - Filter by category, price range, and attributes
- **Product details** - Retrieve comprehensive product information
- **Recommendations** - Context-aware product suggestions

This MCP server enables the Cora agent to access and search the product database in real-time, demonstrating how agents can be augmented with external data sources and tools. Thanks to the MCP standard, the agentic applications doesn't need to worry about the underlying implementation of the search tools or the data structure, focusing instead on generating useful responses based on the retrieved information.

## 🚀 Quick Start

### Prerequisites

- Visual Studio Code
- GitHub account (for Codespaces and GitHub-hosted models) - free tier is sufficient
- Azure subscription (for Microsoft Foundry resources)
- Basic Python knowledge

### Deploy Azure Resources to your Azure subscription

To execute both session demos you will need to create a Microsoft Foundry project with the **gpt-4.1-mini** model deployed.
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
