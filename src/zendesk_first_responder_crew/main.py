#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from .crew import ZendeskFirstResponderCrew
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        "ticket_id": 10,
        "subject": "EKS Cluster using deprecated authentication method",
        "description": "Hello Team, \n\nWe have received High Vulnerability on our AWS EKS cluster from our security tool Crowdstrike. \nPlease help us to understand the severity of the issue and how we can migrate without any downtime. And what will be the impact if anything goes wrong.\n\n\n\nThis policy identifies EKS clusters that are configured to use the deprecated authentication method based on AWS IAM authenticator. Starting with Kubernetes 1.27, Amazon EKS now supports native IAM authentication, replacing the AWS IAM Authenticator. Using deprecated authentication methods may lead to operational issues and potential security vulnerabilities as updates and patches may no longer be available. It is recommended to migrate to the EKS native IAM authentication for better security and future compatibility.\n\n--\nRegards\nAnkita Singh"
    }
    
    try:
        ZendeskFirstResponderCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        ZendeskFirstResponderCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ZendeskFirstResponderCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        ZendeskFirstResponderCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")