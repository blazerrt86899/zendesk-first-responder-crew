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
        "ticket_id": "11",
        "subject": "Consolidating three redis cache cluster into single redis cache cluster",
        "description": "Hi Team, I have three redis cache cluster where i want to merge all together into one new redis cache cluster, can you please help out recommended best approach to do this"
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
        "ticket_id": "11",
        "subject": "Consolidating three redis cache cluster into single redis cache cluster",
        "description": "Hi Team, I have three redis cache cluster where i want to merge all together into one new redis cache cluster, can you please help out recommended best approach to do this"
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
        "ticket_id": "11",
        "subject": "Consolidating three redis cache cluster into single redis cache cluster",
        "description": "Hi Team, I have three redis cache cluster where i want to merge all together into one new redis cache cluster, can you please help out recommended best approach to do this"
    }
    
    try:
        ZendeskFirstResponderCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")