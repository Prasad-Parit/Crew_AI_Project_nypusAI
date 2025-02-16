#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import SeoSemCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'website_name': "https://www.shopclues.com/",
        'competitors': "https://www.amazon.in/,https://www.flipkart.com/,https://www.myntra.com/", 
        'target_audience': " Budget-Conscious Shoppers ",
        'ad_budget': "Monthly ad budget of $5,000 – $15,000",
        'primary_goals': "Increase High-Intent Conversions from Niche Shoppers",
        'current_year': str(datetime.now().year)
    }
    
    try:
        SeoSemCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run()