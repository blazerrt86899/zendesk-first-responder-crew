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
    Can you please help us in creating WAF rules or suggesting remediations for the below given alerts ?
    
    Hi Team,

Please find the details of the following security alert that our SOC detected:

This alert was triggered when SIEM detected a potential PHP File Inclusion attack attempt.

Security Alerts Details:

Start Time: March 28, 2025, 11:32 PM (IST)
Source IP Address: 165.22.215.131
Host: 43.205.154.2
URI: /hello.world
HTTP Method: POST
Action: Allow
Source IP Analysis:

165.22.215.131

ISP: DigitalOcean, LLC
Country: India
IP Reputation: Poor
 

SOC Analyst Triage Comments:

SIEM detected a suspicious post request from the source IP address 165.22.215.131, which contains the following arguments:
"allow_url_include=1": Enables remote file inclusion, allowing external scripts to be executed via URL.
"auto_prepend_file=php://input": Forces PHP to execute code from the raw POST body, enabling code injection.
Furthermore, the post request was allowed by the Web Application Firewall "Truthscreen-Prod".
Additionally, the user-agent in the post request was "Custom-AsyncHttpClient", which is not a typical browser and might indicate the use of an automated script or scanning tool.
On analyzing the logs, we have seen multiple Get requests for suspicious URI from the above-mentioned source IP address to the same host in the past 3 hours, and all of those requests were allowed by the web application firewall. For more information, refer to the box link mentioned below:
Box-Link: https://app.box.com/s/bqetmdquwwmtryp14ht0cdcv3qai34ev
 

Verification Required:

Could you please verify this activity and let us know if it is legitimate or not?
If not legitimate, then please follow the below-mentioned recommended next steps:
Recommended Next Steps:

Block or rate-limit the above-mentioned source IP address if it's not a recognized or legitimate user.
Update WAF rules to block suspicious parameters like allow_url_include and php://input.
Disable risky PHP directives (allow_url_include, auto_prepend_file) and apply open_basedir restrictions in production.
    """
    
    inputs = {
        "ticket_id": "11",
        "subject": "Consolidating three redis cache cluster into single redis cache cluster",
        "description": ticket_description
    }
    
    try:
        ZendeskFirstResponderCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")