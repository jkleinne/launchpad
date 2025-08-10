"""
root_agent entrypoint for ADK
"""
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from src.agents import (
    create_blog_post_agent,
    create_brief_enrichment_agent,
    create_social_media_agent,
)

DEFAULT_MODEL = "gemini-2.5-flash"

def create_root_agent(model: str | None = None) -> LlmAgent:
    """
    Return the project's root agent.

    This coordinator agent acts as the central orchestrator. It takes a user
    prompt, uses a specialist agent to create a full product brief, and then
    delegates content creation (blog and social media) to other agents.

    Returns:
        LlmAgent: An instance of the CampaignCoordinator LlmAgent.
    """
    brief_enrichment_agent = create_brief_enrichment_agent()
    blog_post_agent = create_blog_post_agent()
    social_media_agent = create_social_media_agent()

    coordinator_instruction = """
You are a Campaign Coordinator. Your goal is to generate a complete marketing campaign package (a blog post and a set of social media posts) from a user's idea.

You have access to the following tools: `brief_enrichment_agent`, `blog_post_agent`, and `social_media_agent`.

Follow this exact sequence (non-negotiable):

1.  First, call the `brief_enrichment_agent` tool with the user's original request. This will flesh out the idea into a structured JSON product brief.
2.  Next, take the JSON output from the `brief_enrichment_agent` and call the `blog_post_agent` tool with it.
3.  Then, use the SAME JSON output from the `brief_enrichment_agent` again to call the `social_media_agent` tool.
4.  Finally, consolidate the outputs into a single, final JSON object. This object should have two keys: 'blog_post' containing the text from the `blog_post_agent`, and 'social_media_posts' containing the JSON object from the `social_media_agent`.
5.  Do not output any other text or conversational filler. Your final output must be only the consolidated JSON object.
"""

    return LlmAgent(
        name="campaign_coordinator",
        model=model or DEFAULT_MODEL,
        description="A campaign coordinator that manages content creation from start to finish.",
        instruction=coordinator_instruction,
        tools=[
            AgentTool(agent=brief_enrichment_agent),
            AgentTool(agent=blog_post_agent),
            AgentTool(agent=social_media_agent),
        ],
    )

root_agent: LlmAgent = create_root_agent()