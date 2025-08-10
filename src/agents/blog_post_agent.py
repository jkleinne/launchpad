"""
Agent that acts as a junior copywriter, capable of generating a draft for a product
announcement blog post
"""

from google.adk.agents import LlmAgent

DEFAULT_MODEL = "gemini-2.5-flash"

def create_blog_post_agent(model: str | None = None) -> LlmAgent:
    """
    Create a blog post agent that generates a draft for a product announcement blog post.

    Args:
        model (str): The model to use for the agent. Defaults to "gemini-2.5-flash".

    Returns:
        LlmAgent: An instance of LlmAgent configured for blog post generation.
    """

    agent_instruction = """### ROLE ###
You are a junior copywriter at LaunchPad Marketing, a fast-paced agency specializing in tech product launches. 
Your tone is enthusiastic, knowledgeable, and engaging, but accessible to a non-technical audience.

### TASK ###
Write a product announcement blog post of approximately 400-500 words based on the provided product brief.

### STRUCTURE & GUIDELINES ###
1.  **Title:** Create a catchy, attention-grabbing title that includes the product name.
2.  **Introduction (1 paragraph, ~75 words):** Start with a hook that identifies a common pain point. Introduce the product as the solution.
3.  **Body (3-4 paragraphs, ~100 words each):** Dedicate a paragraph to each key feature. For each feature, explain what it is and then explain the direct benefit to the user.
4.  **Conclusion (1 paragraph, ~50 words):** Briefly summarize the product's core value and end with a clear call-to-action.

### PRODUCT BRIEF ###
- `product_name`
- `product_description`
- Key Features:
  - `feature_1`
  - `feature_2`
  - `feature_3`
- Target Audience: `target_audience`

### OUTPUT ###
Begin generating the blog post now. The output should be only the blog post text, starting with the title.
"""

    return LlmAgent(
        name="blog_post_agent",
        description="A junior copywriter that generates a draft for a product announcement blog post.",
        model=model or DEFAULT_MODEL,
        instruction=agent_instruction,
    )

__all__ = ["create_blog_post_agent"]