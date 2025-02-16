#!/usr/bin/env python
import sys
import warnings

from manager import SeoSemCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = inputs = {
        
        'website_name': "",
        'competitors': "", 
        'target_audience': " ",
        'ad_budget': "",
        'primary_goals': "",
        'current_year': "",
        "human_task": "Draft a compelling LinkedIn post for a B2B SaaS company launching a new AI-powered SEO tool. The goal is to educate digital marketers on its benefits and encourage sign-ups for a free trial."

    }
    SeoSemCrew().crew().kickoff(inputs=inputs)

run()