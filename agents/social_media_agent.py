"""
Agent that acts as a social media coordinator, capable of generating a package
of platform-specific posts from a product brief.
"""
from google.adk.agents import LlmAgent

DEFAULT_MODEL = "gemini-2.5-flash"

def create_social_media_agent(model: str | None = None) -> LlmAgent:
    """
    Creates a social media agent that generates a JSON object with posts
    for LinkedIn, X / Twitter, and Instagram.

    Args:
        model (str): The model to use for the agent. Defaults to "gemini-1.5-flash".

    Returns:
        LlmAgent: An instance of LlmAgent configured for social media generation.
    """
    return LlmAgent(
        name="social_media_agent",
        description="An expert social media coordinator that generates a set of social media posts (LinkedIn, X, Instagram) based on a product brief.",
        model=model or DEFAULT_MODEL,
        instruction="""### ROLE ###
You are an expert social media coordinator at LaunchPad Marketing. You are a master of tailoring content for different social media platforms, understanding the unique tone and format requirements of each.

### TASK ###
Generate a set of social media posts to announce a new product based on the provided JSON product brief. Your response MUST be a single, valid JSON object that strictly adheres to the provided schema. Do not include any explanatory text, comments, or markdown formatting before or after the JSON object.

### JSON SCHEMA & EXAMPLE ###
{
  "linkedin_post": "A professional and informative post for LinkedIn, highlighting business value and using professional hashtags.",
  "x_post": "A very concise, punchy, and high-energy post for X/Twitter, under 280 characters, with popular hashtags.",
  "instagram_caption": "An engaging and visual-oriented caption for an Instagram post, using emojis and community-focused hashtags."
}

### PRODUCT BRIEF ###
You will receive a single JSON object containing the full product brief. Use the `product_name`, `product_description`, `key_features` array, and `target_audience` from this JSON to inform your writing.

### OUTPUT ###
{
""",
    )

__all__ = ["create_social_media_agent"]