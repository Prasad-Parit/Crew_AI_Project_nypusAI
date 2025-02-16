from typing import Type, Dict, Any
from crewai.tools import BaseTool
from pydantic import BaseModel, Field, PrivateAttr
from langchain_community.utilities.dataforseo_api_search import DataForSeoAPIWrapper
from datetime import datetime

class KeywordResearchInput(BaseModel):
    """Input schema for Keyword Research Tool."""
    query: str = Field(..., description="Search query term for keyword research.")
    website_name: str = Field(..., description="Target website for keyword research.")
    competitors: str = Field(..., description="List of competitor websites, comma-separated.")
    target_audience: str = Field(..., description="Primary target audience.")
    ad_budget: str = Field(..., description="Monthly ad budget allocation.")
    primary_goals: str = Field(..., description="Main business objectives.")
    current_year: str = Field(..., description="Current year for context.")

class DataForSEOSerpTool(BaseTool):
    name: str = "DataForSEO SERP Keyword Research Tool"
    description: str = (
        "Fetches search engine results data using DataForSEO SERP API. "
        "Useful for keyword research, uncovering trends, and guiding content strategy."
    )
    args_schema: Type[BaseModel] = KeywordResearchInput
    _wrapper: DataForSeoAPIWrapper = PrivateAttr()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._wrapper = DataForSeoAPIWrapper()

    def _run(self, query: str, website_name: str, competitors: str, target_audience: str,
             ad_budget: str, primary_goals: str, current_year: str) -> Dict[str, Any]:
        """
        Conducts keyword research based on provided parameters and fetches search engine results data.
        """
        try:
            search_query = (
                f"Keyword research for {website_name}, competing with {competitors}, "
                f"targeting {target_audience} with a {ad_budget}. Goal: {primary_goals}. "
                f"Year: {current_year}."
            )
            
            response = self._wrapper.run(search_query)
            return {"query": search_query, "results": response}
        except Exception as e:
            return {"error": str(e)}

# Example Usage
if __name__ == "__main__":
    tool = DataForSEOSerpTool()
    result = tool.run(
        query="keyword research",
        website_name="https://www.shopclues.com/",
        competitors="https://www.amazon.in/,https://www.flipkart.com/,https://www.myntra.com/",
        target_audience="Budget-Conscious Shoppers",
        ad_budget="Monthly ad budget of $5,000 – $15,000",
        primary_goals="Increase High-Intent Conversions from Niche Shoppers",
        current_year=str(datetime.now().year)
    )
    print(result)
