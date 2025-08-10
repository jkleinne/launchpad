"""
root_agent entrypoint for ADK
"""
from google.adk.agents import LlmAgent
from src.agents.blog_post_agent import create_blog_post_agent
from src.agents.brief_enrichment_agent import create_brief_enrichment_agent

DEFAULT_MODEL = "gemini-2.5-flash"

def create_root_agent(model: str | None = None) -> LlmAgent:
    """
    Return the project's root agent.

    This coordinator agent acts as the central orchestrator. It takes a user
    prompt, uses the brief_enrichment_agent to create a full product brief,
    and then delegates content creation to other specialist agents.

    Returns:
        LlmAgent: An instance of the CampaignCoordinator LlmAgent.
    """
    brief_enrichment_agent = create_brief_enrichment_agent()
    blog_post_agent = create_blog_post_agent()

    coordinator_instruction = """
You are a Campaign Coordinator.

Use ONLY the tool `transfer_to_agent` to talk to sub-agents. Never call a tool
named after a sub-agent (e.g., 'brief_enrichment_agent'); it does not exist.

Follow this exact sequence and do not respond to the user until Step C:

A) Call `transfer_to_agent` with:
   {"agent_name": "brief_enrichment_agent",
    "input": {"user_request": $USER_INPUT}}

B) Take the RAW JSON string returned by Step A and immediately call
   `transfer_to_agent` again with:
   {"agent_name": "blog_post_agent",
    "input": {"product_brief_json": <the exact JSON from Step A>}}

C) Return ONLY the blog post text produced by the blog_post_agent.
Do not echo any JSON and do not stop after Step A.
"""


    return LlmAgent(
        name="campaign_coordinator",
        model=model or DEFAULT_MODEL,
        description="A campaign coordinator that manages content creation from start to finish.",
        instruction=coordinator_instruction,

        sub_agents=[
            brief_enrichment_agent,
            blog_post_agent,
            # social_media_agent,
        ],
    )

root_agent: LlmAgent = create_root_agent()