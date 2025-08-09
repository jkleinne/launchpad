"""
root_agent entrypoint for ADK
"""
from google.adk.agents import LlmAgent 
from src.agents import create_blog_post_agent

def create_root_agent() -> LlmAgent:
    """
    Return the project's root agent.

    TODO: Currently delegating directly to blog_post_agent, but
    the idea is to have a coordinator_agent instantiated and defined as
    the root agent, which will then manage other agents like blog_post_agent.

    Returns:
        LlmAgent: An instance of LlmAgent meant to be configured as the root agent.
    """
    return create_blog_post_agent()

root_agent: LlmAgent = create_root_agent()