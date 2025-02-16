from crewai.tools import BaseTool
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class GoogleSearchConsoleInput(BaseModel):
    """Input schema for GoogleSearchConsoleTool."""
    website_name: str = Field(..., description="Website URL to monitor performance.")
    competitors: str = Field(..., description="Comma-separated list of competitor websites.")
    target_audience: str = Field(..., description="Target audience for the website.")
    ad_budget: str = Field(..., description="Monthly advertising budget.")
    primary_goals: str = Field(..., description="Main goals for website optimization.")
    current_year: str = Field(..., description="Current year for tracking performance trends.")

class GoogleSearchConsoleTool(BaseTool):
    name: str = "Google Search Console Monitor"
    description: str = "Monitors website performance, indexing status, and search traffic."
    args_schema: Type[BaseModel] = GoogleSearchConsoleInput

    def _run(self, website_name: str, competitors: str, target_audience: str, ad_budget: str, primary_goals: str, current_year: str) -> str:
        try:
            response = requests.get(website_name)
            if response.status_code != 200:
                return f"Failed to retrieve data from {website_name}. Status Code: {response.status_code}"

            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "No title found"
            meta_desc = "No description found"
            for meta in soup.find_all('meta'):
                if 'name' in meta.attrs and meta.attrs['name'].lower() == 'description':
                    meta_desc = meta.attrs['content']
                    break
            
            return (f"Website Analysis for {website_name} ({current_year}):\n"
                    f"- Title: {title}\n"
                    f"- Meta Description: {meta_desc}\n"
                    f"- Competitors: {competitors}\n"
                    f"- Target Audience: {target_audience}\n"
                    f"- Ad Budget: {ad_budget}\n"
                    f"- Primary Goals: {primary_goals}")
        except Exception as e:
            return f"Error fetching website data: {str(e)}"
        


class GoogleAnalyticsInput(BaseModel):
    """Input schema for GoogleAnalyticsTool."""
    website_name: str = Field(..., description="Website URL to track analytics for.")
    competitors: str = Field(..., description="Comma-separated list of competitor websites.")
    target_audience: str = Field(..., description="Target audience description.")
    ad_budget: str = Field(..., description="Monthly ad budget range.")
    primary_goals: str = Field(..., description="Primary goals of the website.")
    current_year: str = Field(..., description="Current year.")

class GoogleAnalyticsTool(BaseTool):
    name: str = "Google Analytics Tracker"
    description: str = "Tracks website traffic and user behavior to measure the effectiveness of SEO strategies."
    args_schema: Type[BaseModel] = GoogleAnalyticsInput

    def _run(self, website_name: str, competitors: str, target_audience: str, ad_budget: str, primary_goals: str, current_year: str) -> dict:
        """Fetches website analytics data."""
        try:
            response = requests.get(website_name)
            if response.status_code != 200:
                return {"error": "Failed to retrieve website data."}
            
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "No title found"
            meta_description = soup.find("meta", attrs={"name": "description"})
            description = meta_description["content"] if meta_description else "No meta description found"

            return {
                "Website": website_name,
                "Title": title,
                "Meta Description": description,
                "Target Audience": target_audience,
                "Ad Budget": ad_budget,
                "Primary Goals": primary_goals,
                "Current Year": current_year,
                "Competitors": competitors.split(",")
            }
        except Exception as e:
            return {"error": str(e)}
        

class SEMrushToolInput(BaseModel):
    """Input schema for SEMrushTool."""
    website_name: str = Field(..., description="Website URL to analyze.")
    competitors: str = Field(..., description="Comma-separated competitor URLs.")
    target_audience: str = Field(..., description="Description of the target audience.")
    ad_budget: str = Field(..., description="Ad budget information.")
    primary_goals: str = Field(..., description="Primary marketing goals.")
    current_year: str = Field(..., description="Current year.")

class SEMrushTool(BaseTool):
    name: str = "SEMrush Analysis Tool"
    description: str = (
        "Conducts keyword research, backlink analysis, site audit, and competitor analysis "
        "to support SEO and SEM strategies. Provides actionable insights for optimization."
    )
    args_schema: Type[BaseModel] = SEMrushToolInput

    def _run(self, website_name: str, competitors: str, target_audience: str, ad_budget: str, primary_goals: str, current_year: str) -> dict:
        """Executes the SEMrush-based analysis."""
        results = {}
        competitors_list = competitors.split(",")

        # Example: Scraping keyword data (Placeholder function)
        results["keyword_research"] = self.keyword_research(website_name)
        
        # Example: Scraping backlink data (Placeholder function)
        results["backlink_analysis"] = self.backlink_analysis(website_name)
        
        # Example: Competitor Analysis (Placeholder function)
        results["competitor_analysis"] = {
            competitor: self.competitor_seo_analysis(competitor) for competitor in competitors_list
        }
        
        return results
    
    def keyword_research(self, website: str):
        """Simulates keyword research."""
        return ["best budget gadgets", "affordable electronics", "cheap online shopping"]
    
    def backlink_analysis(self, website: str):
        """Simulates backlink analysis."""
        return {"total_backlinks": 1200, "high_quality_links": 340, "spam_score": "Low"}
    
    def competitor_seo_analysis(self, competitor: str):
        """Simulates competitor SEO analysis."""
        return {"ranking_keywords": 3500, "domain_authority": 78, "traffic_estimate": "1.2M monthly"}        
    


class AhrefsToolInput(BaseModel):
    """Input schema for AhrefsTool."""
    website_name: str = Field(..., description="The website to analyze.")
    competitors: str = Field(..., description="Comma-separated list of competitor websites.")
    target_audience: str = Field(..., description="Description of the target audience.")
    ad_budget: str = Field(..., description="The allocated monthly ad budget.")
    primary_goals: str = Field(..., description="The primary objectives of the SEO strategy.")
    current_year: str = Field(..., description="The current year.")

class AhrefsTool(BaseTool):
    name: str = "Ahrefs Competitor & SEO Analysis Tool"
    description: str = (
        "A tool that provides competitor analysis, keyword research, backlink monitoring, "
        "and content strategy suggestions using real data from competitor websites."
    )
    args_schema: Type[BaseModel] = AhrefsToolInput

    def _run(self, website_name: str, competitors: str, target_audience: str, ad_budget: str, primary_goals: str, current_year: str) -> str:
        competitors_list = competitors.split(',')
        
        # Fetch competitor data
        competitor_data = []
        for competitor in competitors_list:
            competitor_info = self.scrape_competitor_data(competitor.strip())
            competitor_data.append(competitor_info)

        return {
            "website_analyzed": website_name,
            "competitor_analysis": competitor_data,
            "target_audience": target_audience,
            "ad_budget": ad_budget,
            "primary_goals": primary_goals,
            "year": current_year
        }

    def scrape_competitor_data(self, competitor_url: str) -> dict:
        """Scrapes basic SEO data from a competitor's website."""
        try:
            response = requests.get(competitor_url, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(response.text, "html.parser")
            
            title = soup.title.string if soup.title else "No title found"
            meta_desc = "No description found"
            meta_tag = soup.find("meta", attrs={"name": "description"})
            if meta_tag and "content" in meta_tag.attrs:
                meta_desc = meta_tag["content"]
            
            return {
                "competitor": competitor_url,
                "title": title,
                "meta_description": meta_desc
            }
        except Exception as e:
            return {"competitor": competitor_url, "error": str(e)}
        
 

class MozProToolInput(BaseModel):
    """Input schema for MozProTool."""
    website_name: str = Field(..., description="Website URL to analyze.")
    competitors: str = Field(..., description="Comma-separated list of competitor URLs.")
    target_audience: str = Field(..., description="Target audience description.")
    ad_budget: str = Field(..., description="Advertising budget details.")
    primary_goals: str = Field(..., description="Primary SEO goals.")
    current_year: str = Field(..., description="Current year for contextual relevance.")

class MozProTool(BaseTool):
    name: str = "Moz Pro SEO Analyzer"
    description: str = "A suite of tools for site auditing, rank tracking, and keyword research."
    args_schema: Type[BaseModel] = MozProToolInput

    def _run(self, website_name: str, competitors: str, target_audience: str, ad_budget: str, primary_goals: str, current_year: str) -> dict:
        """Executes SEO analysis based on Moz Pro functionalities."""
        report = {}
        
        # Perform site audit
        report["site_audit"] = self.perform_site_audit(website_name)
        
        # Analyze backlinks
        report["backlink_analysis"] = self.analyze_backlinks(website_name)
        
        # Generate meta descriptions
        report["meta_descriptions"] = self.generate_meta_descriptions(website_name)
        
        # Suggest internal linking strategy
        report["internal_linking"] = self.suggest_internal_links(website_name)
        
        return report

    def perform_site_audit(self, website_url: str) -> str:
        """Simulates a site audit by fetching and analyzing basic webpage elements."""
        try:
            response = requests.get(website_url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "No title found"
            headers = [h.text for h in soup.find_all(['h1', 'h2', 'h3'])]
            return f"Title: {title}, Headers: {headers[:5]}"
        except Exception as e:
            return f"Error fetching website: {str(e)}"

    def analyze_backlinks(self, website_url: str) -> str:
        """Placeholder for backlink analysis (would normally require API access)."""
        return "Backlink analysis feature requires external API access."

    def generate_meta_descriptions(self, website_url: str) -> str:
        """Generates a simple meta description by analyzing page content."""
        try:
            response = requests.get(website_url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            snippet = ' '.join([p.text for p in paragraphs[:2]])[:160]
            return snippet if snippet else "No suitable content found for meta description."
        except Exception as e:
            return f"Error generating meta description: {str(e)}"

    def suggest_internal_links(self, website_url: str) -> str:
        """Provides basic internal linking suggestions."""
        return "Consider linking key pages with relevant anchor text for better SEO."


class ScreamingFrogToolInput(BaseModel):
    """Input schema for ScreamingFrogTool."""
    website_name: str = Field(..., description="URL of the website to audit.")
    competitors: str = Field(..., description="Comma-separated list of competitor websites.")
    target_audience: str = Field(..., description="Target audience for the website.")
    ad_budget: str = Field(..., description="Monthly advertising budget.")
    primary_goals: str = Field(..., description="Primary marketing goals.")
    current_year: str = Field(..., description="Current year for reference.")

class ScreamingFrogTool(BaseTool):
    name: str = "Screaming Frog SEO Auditor"
    description: str = "Crawls websites to identify technical SEO issues and analyze on-page elements."
    args_schema: Type[BaseModel] = ScreamingFrogToolInput

    def _run(self, website_name: str, competitors: str, target_audience: str, ad_budget: str, primary_goals: str, current_year: str) -> str:
        """Crawls the website and returns an SEO audit report."""
        try:
            response = requests.get(website_name, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code != 200:
                return f"Failed to access {website_name}. HTTP Status Code: {response.status_code}"
            
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "No title found"
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            meta_desc_content = meta_desc['content'] if meta_desc else "No meta description found"
            
            audit_report = f"""
            SEO Audit Report for {website_name} ({current_year})
            ------------------------------------------------------
            Title Tag: {title}
            Meta Description: {meta_desc_content}
            Competitors: {competitors}
            Target Audience: {target_audience}
            Ad Budget: {ad_budget}
            Primary Goals: {primary_goals}
            
            Recommendations:
            - Ensure title tag is optimized for primary keywords.
            - Improve meta description for better click-through rates.
            - Conduct internal linking improvements for better navigation.
            - Optimize images with alt text for accessibility and SEO.
            - Improve page speed and mobile-friendliness.
            
            """
            return audit_report
        except Exception as e:
            return f"An error occurred during the audit: {str(e)}"




class SitebulbAuditInput(BaseModel):
    """Input schema for SitebulbAuditTool."""
    website_name: str = Field(..., description="The URL of the website to audit for SEO improvements.")
    competitors: str = Field(..., description="Comma-separated URLs of competitors.")
    target_audience: str = Field(..., description="Description of the target audience.")
    ad_budget: str = Field(..., description="Monthly advertising budget.")
    primary_goals: str = Field(..., description="Primary SEO goals.")
    current_year: str = Field(default=str(datetime.now().year), description="Current year.")

class SitebulbAuditTool(BaseTool):
    name: str = "Sitebulb SEO Audit Tool"
    description: str = (
        "A tool that audits a website for technical SEO improvements using Sitebulb. "
        "It provides actionable insights for better rankings."
    )
    args_schema: Type[BaseModel] = SitebulbAuditInput

    def _run(self, website_name: str, competitors: str, target_audience: str, ad_budget: str, primary_goals: str, current_year: str) -> str:
        """Performs a basic SEO audit by fetching site data and considering marketing parameters."""
        try:
            response = requests.get(website_name, timeout=10)
            if response.status_code == 200:
                return (
                    f"Website {website_name} is accessible.\n"
                    f"Competitors: {competitors}\n"
                    f"Target Audience: {target_audience}\n"
                    f"Ad Budget: {ad_budget}\n"
                    f"Primary Goals: {primary_goals}\n"
                    f"Year: {current_year}\n"
                    "Perform a deeper audit using Sitebulb for detailed SEO improvements."
                )
            else:
                return f"Failed to access {website_name}. Status Code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"Error accessing {website_name}: {str(e)}"

        



class YoastOptimizationInput(BaseModel):
    """Input schema for YoastOptimizationTool."""
    website_name: str = Field(..., description="The URL of the website to optimize.")
    competitors: str = Field(..., description="Comma-separated URLs of competitors.")
    target_audience: str = Field(..., description="Description of the target audience.")
    ad_budget: str = Field(..., description="Monthly advertising budget.")
    primary_goals: str = Field(..., description="Primary SEO goals.")
    current_year: str = Field(default=str(datetime.now().year), description="Current year.")

class YoastOptimizationTool(BaseTool):
    name: str = "Yoast SEO Optimization Tool"
    description: str = "Analyzes and optimizes website content with meta tags and SEO recommendations."
    args_schema: Type[BaseModel] = YoastOptimizationInput

    def _run(self, website_name: str, competitors: str, target_audience: str, ad_budget: str, primary_goals: str, current_year: str) -> dict:
        try:
            response = requests.get(website_name, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title = soup.title.string if soup.title else "No title found"
            meta_desc_tag = soup.find('meta', attrs={'name': 'description'})
            meta_desc = meta_desc_tag['content'] if meta_desc_tag else "No meta description found"
            
            seo_recommendations = {
                "title": title,
                "meta_description": meta_desc,
                "competitors": competitors,
                "target_audience": target_audience,
                "ad_budget": ad_budget,
                "primary_goals": primary_goals,
                "year": current_year,
                "recommendations": [
                    "Ensure the title is under 60 characters and includes target keywords.",
                    "Meta description should be between 150-160 characters with a strong call-to-action.",
                    "Use structured data markup to improve search visibility.",
                    "Optimize images with alt text for better SEO.",
                    "Ensure mobile-friendliness and fast page loading speed."
                ]
            }
            return seo_recommendations
        
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to fetch page content: {e}"}

# Example Inputs for SEO Optimization
def get_website_seo_details():
    seo_details = {
        "website_name": "https://www.shopclues.com/",
        "competitors": "https://www.amazon.in/, https://www.flipkart.com/, https://www.myntra.com/",
        "target_audience": "Budget-Conscious Shoppers",
        "ad_budget": "Monthly ad budget of $5,000 – $15,000",
        "primary_goals": "Increase High-Intent Conversions from Niche Shoppers",
        "current_year": "2025"
    }
    return seo_details



class KWFinderInput(BaseModel):
    """Input schema for KWFinder tool."""
    website_name: str = Field(..., description="Website URL to analyze for keyword opportunities.")
    competitors: str = Field(..., description="Comma-separated list of competitor websites.")
    target_audience: str = Field(..., description="Target audience description.")
    ad_budget: str = Field(..., description="Monthly advertising budget.")
    primary_goals: str = Field(..., description="Primary marketing goals.")
    current_year: str = Field(..., description="Current year for contextual analysis.")

class KWFinderTool(BaseTool):
    name: str = "KWFinder"
    description: str = "Helps find suitable keywords based on search volume and competition analysis."
    args_schema: Type[BaseModel] = KWFinderInput

    def _run(self, website_name: str, competitors: str, target_audience: str, ad_budget: str, primary_goals: str, current_year: str) -> dict:
        keywords = self._scrape_keywords(website_name)
        blog_topics = self._generate_blog_topics(keywords, target_audience)
        return {
            "keywords": keywords,
            "blog_topics": blog_topics
        }

    def _scrape_keywords(self, website: str) -> list:
        """Scrape relevant keywords from the website."""
        try:
            response = requests.get(website, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            words = [word.text for word in soup.find_all('h1') + soup.find_all('h2') + soup.find_all('h3')]
            return list(set(words[:10]))  # Return top 10 unique keywords
        except Exception as e:
            return ["Error fetching keywords"]

    def _generate_blog_topics(self, keywords: list, target_audience: str) -> list:
        """Generate blog topics based on long-tail keywords and audience insights."""
        return [f"How {kw} Can Help {target_audience} in {datetime.now().year}" for kw in keywords if kw]

        



