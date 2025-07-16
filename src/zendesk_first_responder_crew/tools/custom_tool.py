from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
import os
from dotenv import load_env, find_env

class ZendeskKBSearchTool(BaseTool):
    name = "Zendesk KB Search Tool"
    description = "Searches the query in Zendesk KB Articles"
    
    def _run(self, query: str):
        """ Searches the query in Zendesk KB Articles """
        ZENDESK_SUBDOMAIN=os.getenv('ZENDESK_SUBDOMAIN')
        ZENDESK_API_TOKEN=os.getenv('ZENDESK_API_TOKEN')
        ZENDESK_USER_MAIL=os.getenv('ZENDESK_EMAIL')
        
        if not all([ZENDESK_SUBDOMAIN, ZENDESK_API_TOKEN, ZENDESK_USER_MAIL]):
            return "Missing required configuration (domain, user_email, search_url, or auth_token)"
        
        url = f"https://{ZENDESK_SUBDOMAIN}/api/v2/help_center/articles/search.json"
        auth = (f"{ZENDESK_USER_MAIL}/token", ZENDESK_API_TOKEN)
        headers = {
            "Content-Type": "application/json"
        }
        params = { "query": query }
        
        response = requests.get(url, auth=auth, headers=headers, params=params)
        response.raise_for_status()
        
        if response.ok:
            articles = response.json().get("articles", [])
            if not articles:
                return "No articles found for the query"
            summary = []
            for article in articles:
                title = article.get("title", "No Title")
                link = article.get("link", "No Link")
                snippet = article.get("snippet", "No Snippet")
                summary.append(f"- [{title}]({link}: {snippet})")
            
            return "\n".join(summary)
        else:
            return f"Failed to search KB: {response.status_code}, {response.text}"

class AWSDocsSearchTool(BaseTool):
    name = "AWS Docs Search Tool"
    description = "Searches the query in AWS Docs"
    
    def _run(self, query: str):
        """ Searches the query in AWS Docs """
        pass
                
    