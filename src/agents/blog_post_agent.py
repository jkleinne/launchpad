"""
Agent that acts as a junior copywriter, capable of generating a draft for a product
announcement blog post
"""

from google.adk.agents import LlmAgent

DEFAULT_MODEL = "gemini-2.5-flash"

def create_blog_post_agent(model: str) -> LlmAgent:
    """
    Create a blog post agent that generates a draft for a product announcement blog post.

    Args:
        model (str): The model to use for the agent. Defaults to "gemini-2.5-flash".

    Returns:
        LlmAgent: An instance of LlmAgent configured for blog post generation.
    """
    return LlmAgent(
        name="blog_post_agent",
        description="A junior copywriter that generates a draft for a product announcement blog post.",
        model=model or DEFAULT_MODEL,
        system_prompt="You are a junior copywriter tasked with generating a draft for a product announcement blog post.",
    )