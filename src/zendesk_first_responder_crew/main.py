#!/usr/bin/env python
import sys
import warnings

from .crew import ZendeskFirstResponderCrew
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    
    ticket_description = """
    Hi Team ,

    We are currently working on a DB  Disk space reclaim activity as part of our effort to optimize storage usage and reduce ongoing costs. We ran the Sync process and we found the sync job failed due to some issues. To proceed effectively, we require assistance from your technical team.

    """
    
    inputs = {
        "ticket_id": "11",
        "subject": "Request for Assistance with DB Disk Space Reclaim Activity ( DB: Mongo DB)",
        "description": ticket_description
    }
    
    try:
        ZendeskFirstResponderCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    
    ticket_description = """
    Hi @Lokhande, Abhijeet 

Hope you're doing well.

We had earlier installed both network plugins (VPC-CNI and Calico) in your EKS clusters. However, we’ve observed that VPC-CNI is currently not being utilized. We would appreciate your support in migrating the cluster to use VPC-CNI as the primary CNI.

Looking forward to your guidance.

 

Thanks

Chirrag Sapra

Senior DevOps Engineer
    """
    
    
    inputs = {
        "ticket_id": "11",
        "subject": "[EXTERNAL] Support Required for Migrating to VPC-CNI on EKS",
        "description": ticket_description
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
    ticket_description = """
    Hi @Lokhande, Abhijeet 

Hope you're doing well.

We had earlier installed both network plugins (VPC-CNI and Calico) in your EKS clusters. However, we’ve observed that VPC-CNI is currently not being utilized. We would appreciate your support in migrating the cluster to use VPC-CNI as the primary CNI.

Looking forward to your guidance.
    """
    
    inputs = {
        "ticket_id": "11",
        "subject": "[EXTERNAL] Support Required for Migrating to VPC-CNI on EKS",
        "description": ticket_description
    }
    
    try:
        ZendeskFirstResponderCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")