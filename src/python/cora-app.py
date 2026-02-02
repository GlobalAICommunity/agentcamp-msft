"""Build Agent using Microsoft Agent Framework in Python
# Run this python script
> pip install anthropic agent-framework --pre
> python <this-script-path>.py
"""

import asyncio
import os

from agent_framework import MCPStdioTool, MCPStreamableHTTPTool, ToolProtocol, FunctionCallContent
from agent_framework.azure import AzureAIClient
from agent_framework.openai import OpenAIChatClient
from openai import AsyncOpenAI
from azure.identity.aio import AzureCliCredential

# Microsoft Foundry Agent Configuration
ENDPOINT = "https://aifoundry-ac.services.ai.azure.com/api/projects/project-ac"
MODEL_DEPLOYMENT_NAME = "gpt-4.1-mini"

AGENT_NAME = "mcp-agent"
AGENT_INSTRUCTIONS = "You are Cora, an intelligent and friendly AI assistant for Zava, a home improvement brand. You help customers with their DIY projects by understanding their needs and recommending the most suitable products from Zava’s catalog.​\n\nYour role is to:​\n\n- Engage with the customer in natural conversation to understand their DIY goals.​\n\n- Ask thoughtful questions to gather relevant project details.​\n\n- Be brief in your responses.​\n\n- Provide the best solution for the customer's problem and only recommend a relevant product within Zava's product catalog.​\n\n- Search Zava’s product database to identify 1 product that best match the customer’s needs.​\n\n- Clearly explain what each recommended Zava product is, why it’s a good fit, and how it helps with their project.​\n​\nYour personality is:​\n\n- Warm and welcoming, like a helpful store associate​\n\n- Professional and knowledgeable, like a seasoned DIY expert​\n\n- Curious and conversational—never assume, always clarify​\n\n- Transparent and honest—if something isn’t available, offer support anyway​\n\nIf no matching products are found in Zava’s catalog, say:​\n“Thanks for sharing those details! I’ve searched our catalog, but it looks like we don’t currently have a product that fits your exact needs. If you'd like, I can suggest some alternatives or help you adjust your project requirements to see if something similar might work.”​"

# User inputs for the conversation
USER_INPUTS = [
    "Here’s a photo of my living room. Based on the lighting and layout, recommend a Zava eggshell paint.",
]

def create_mcp_tools() -> list[ToolProtocol]:
    return [
        MCPStdioTool(
            name="VSCode Tools".replace("-", "_"),
            description="MCP server for VSCode Tools",
            command="INSERT_COMMAND_HERE",
            args=[
                "INSERT_ARGUMENTS_HERE",
            ]
        ),
    ]

async def main() -> None:
    async with (
        # For authentication, run `az login` command in terminal or replace AzureCliCredential with preferred authentication option.
        AzureCliCredential() as credential,
        AzureAIClient(
            project_endpoint=ENDPOINT,
            model_deployment_name=MODEL_DEPLOYMENT_NAME,
            credential=credential,
            agent_name=AGENT_NAME,
            use_latest_version=True,  # This parameter will allow to re-use latest agent version instead of creating a new one
        ).create_agent(
            instructions=AGENT_INSTRUCTIONS,
            tools=[
                *create_mcp_tools(),
            ],
        ) as agent
    ):
        # Process user messages
        for user_input in USER_INPUTS:
            print(f"\n# User: '{user_input}'")
            printed_tool_calls = set()
            async for chunk in agent.run_stream([user_input]):
                # log tool calls if any
                function_calls = [
                    c for c in chunk.contents 
                    if isinstance(c, FunctionCallContent)
                ]
                for call in function_calls:
                    if call.call_id not in printed_tool_calls:
                        print(f"Tool calls: {call.name}")
                        printed_tool_calls.add(call.call_id)
                if chunk.text:
                    print(chunk.text, end="")
            print("")
        
        print("\n--- All tasks completed successfully ---")

    # Give additional time for all async cleanup to complete
    await asyncio.sleep(1.0)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("Program finished.")
