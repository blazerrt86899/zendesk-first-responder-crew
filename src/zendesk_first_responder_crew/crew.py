from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pydantic import BaseModel, Field
from typing import List
from crewai_tools import SerperDevTool, WebsiteSearchTool

class TicketSummary(BaseModel):
    ticketId: str = Field(description="The ID of the Zendesk ticket")
    summarizedDescription: str = Field(description="A concise summary of the customer's technical issue")
    awsServices: List[str] = Field(description="A list of AWS services that are relevant to the customer's issue")

@CrewBase
class ZendeskFirstResponderCrew():
    """ZendeskFirstResponderCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    ## Agents Config
    
    @agent
    def problem_summarizer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['problem_summarizer_agent'], # type: ignore[index]
            verbose=True,
            allow_delegation=False
        )
    
    @agent
    def web_search_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['web_search_analyst'], # type: ignore[index]
            verbose=True,
            allow_delegation=False,
            tools=[SerperDevTool(), WebsiteSearchTool(website_url="https://docs.aws.amazon.com/")]
        )
        
    @agent
    def response_drafter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['response_drafter_agent'], # type: ignore[index]
            verbose=True,
            allow_delegation=False
        )
    
        
    ## Tasks Config
        
    @task
    def summarize_problem_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_problem_task'], # type: ignore[index]
            agent=self.problem_summarizer_agent(),
            verbose=True,
            output_pydantic=TicketSummary
        )
    
    @task
    def web_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['web_search_task'], # type: ignore[index]
            agent=self.web_search_analyst(),
            verbose=True,
            context=[self.summarize_problem_task()]
        )
    
    @task
    def draft_response_task(self) -> Task:
        return Task(
            config=self.tasks_config['draft_response_task'], # type: ignore[index]
            agent=self.response_drafter_agent(),
            verbose=True,
            context=[self.web_search_task()],
            markdown=True,
            output_file="final_response.md"
        )
        
    ## Crew Config

    @crew
    def crew(self) -> Crew:
        """Creates the ZendeskFirstResponderCrew crew"""
       
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            memory=True
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
