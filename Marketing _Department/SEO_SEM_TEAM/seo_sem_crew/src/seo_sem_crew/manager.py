from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from tools.lang_tools import DataForSEOSerpTool
from tools.custom_tool import (
    GoogleAnalyticsTool,
    GoogleSearchConsoleTool,
    SEMrushTool,
    AhrefsTool,
    MozProTool,
    ScreamingFrogTool,
    SitebulbAuditTool,
    YoastOptimizationTool,
    KWFinderTool
)
from tools.tasksupdate import TaskStatusUpdate

load_dotenv()


@CrewBase
class SeoSemCrew:
    """Seo Sem Manager crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def keyword_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['keyword_researcher'],
            tools=[
                DataForSEOSerpTool(),
		  		   SEMrushTool(),
				   AhrefsTool(),
				   KWFinderTool(),
				   TaskStatusUpdate()
            ],
            verbose=True
        )

    @agent
    def competitor_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['competitor_analyst'],
            tools=[
                SerperDevTool(),
				   SEMrushTool(),
				   AhrefsTool(),
				   TaskStatusUpdate()
            ],
            verbose=True
        )

    @agent
    def content_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_optimizer'],
            tools=[YoastOptimizationTool(),
				MozProTool(),
				GoogleSearchConsoleTool(),
				TaskStatusUpdate()],
            verbose=True
        )

    @agent
    def backlink_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['backlink_analyst'],
            tools=[
                AhrefsTool(),
				SEMrushTool(),
				MozProTool(),
				TaskStatusUpdate()
            ],
            verbose=True
        )

    @agent
    def analytics_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['analytics_specialist'],
            tools=[
                GoogleAnalyticsTool(),
				GoogleSearchConsoleTool(),
				TaskStatusUpdate()
            ],
            verbose=True
        )

    @agent
    def seo_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_reporter'],
            tools=[
                SerperDevTool(),
				GoogleAnalyticsTool(),
				SEMrushTool(),
				TaskStatusUpdate()
            ],
            verbose=True
        )

    @agent
    def meta_description_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['meta_description_creator'],
            tools=[
                YoastOptimizationTool(),
				MozProTool(),
				TaskStatusUpdate()
            ],
            verbose=True
        )

    @agent
    def ad_copywriter(self) -> Agent:
        return Agent(
            config=self.agents_config['ad_copywriter'],
            tools=[
                SEMrushTool(),
				TaskStatusUpdate()
            ],
            verbose=True
        )

    @agent
    def sem_campaign_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['sem_campaign_manager'],
            tools=[
                GoogleAnalyticsTool(),
				SEMrushTool(),
				TaskStatusUpdate()
            ],
            verbose=True
        )

    @agent
    def seo_auditor(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_auditor'],
            tools=[
                ScreamingFrogTool(),
				SitebulbAuditTool(),
				GoogleSearchConsoleTool(),
				TaskStatusUpdate()
            ],
            verbose=True
        )

    @agent
    def internal_link_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['internal_link_strategist'],
            tools=[
                ScreamingFrogTool(),
				MozProTool(),
				GoogleSearchConsoleTool(),
				TaskStatusUpdate()
            ],
            verbose=True
        )
    
    @agent
    def content_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['content_strategist'],
            tools=[
                SEMrushTool(),
				AhrefsTool(),
				KWFinderTool(),
				TaskStatusUpdate()
            ],
            verbose=True
        )


    @task
    def keyword_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['keyword_research_task'],
            output_file='keyword_research_task.md'
        )

    @task
    def competitor_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['competitor_analysis_task'],
            output_file='competitor_analysis_task.md'
        )

    @task
    def content_optimization_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_optimization_task'],
            output_file='content_optimization_task.md'
        )

    @task
    def backlink_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['backlink_analysis_task'],
            output_file='backlink_analysis_task.md'
        )

    @task
    def analytics_monitoring_task(self) -> Task:
        return Task(
            config=self.tasks_config['analytics_monitoring_task'],
            output_file='analytics_monitoring_task.md'
        )

    @task
    def seo_reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['seo_reporting_task'],
            output_file='seo_reporting_task.md'
        )

    @task
    def meta_description_task(self) -> Task:
        return Task(
            config=self.tasks_config['meta_description_task'],
            output_file='meta_description_task.md'
        )

    @task
    def ad_copy_task(self) -> Task:
        return Task(
            config=self.tasks_config['ad_copy_task'],
            output_file='ad_copy_task.md'
        )

    @task
    def sem_campaign_management_task(self) -> Task:
        return Task(
            config=self.tasks_config['sem_campaign_management_task'],
            output_file='sem_campaign_management_task.md'
        )

    @task
    def seo_audit_task(self) -> Task:
        return Task(
            config=self.tasks_config['seo_audit_task'],
            output_file='seo_audit_task.md'
        )
    
    @task
    def internal_linking_task(self) -> Task:
        return Task(
            config=self.tasks_config['internal_linking_task'],
            output_file='internal_linking_task.md'
        )
    
    @task
    def content_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_strategy_task'],
            output_file='content_strategy_task.md'
        )

    @agent
    def manager(self) -> Agent:
        return Agent(
            role="Task Manager",
            goal="Efficiently identify, delegate, and oversee the execution of tasks based on user input, ensuring timely and accurate completion while maintaining clear communication with the user.",
            verbose=True,
            tools=[],
            backstory=(
                """
                You are a highly organized and detail-oriented professional with extensive experience in task management and delegation. 
                Your expertise lies in understanding complex requirements, matching tasks to the right resources, and ensuring seamless execution.
                With a strong focus on efficiency and accountability, you thrive in dynamic environments where multiple tasks need to be managed simultaneously.
                Your ability to communicate clearly and monitor progress ensures that tasks are completed on time and meet the highest standards of quality.
                """
            ),
            allow_delegation=True,
            memory=True
        )

    @task
    def process_pending_tasks_task(self) -> Task:
        return Task(
            description=(
                """
                Take the task provided by the user (`{human_task}`) and determine which agent is best suited to execute it based on the agent's role and capabilities.
                
                Steps to follow:
                1. **Analyze the Task**: Carefully read and understand the task provided by the user. Identify the key requirements and objectives of the task.
                2. **Match Task to Agent**: Review the roles and capabilities of all available agents. Match the task to the most appropriate agent based on their expertise and tools.
                3. **Delegate the Task**: If a suitable agent is found, delegate the task to that agent and ensure they execute it properly. Provide the agent with all necessary information and context.
                4. **Handle Unmatched Tasks**: If no suitable agent is available to handle the task, inform the user that the task cannot be executed and provide a reason why.
                5. **Monitor Progress**: Continuously monitor the progress of the task. If the task fails or encounters issues, update the task status accordingly and inform the user.
                6. **Ensure Completion**: Once the task is completed, verify that the output meets the user's expectations and update the task status to "COMPLETED".
                """
            ),
            expected_output="""
            The task provided by the user should be executed by the appropriate agent, and the results obtained by the agent should be shown to the user.
            If the task cannot be executed, the user should be informed with a clear explanation.
            """,
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.keyword_researcher(),
                self.competitor_analyst(),
                self.content_optimizer(),
                self.backlink_analyst(),
                self.analytics_specialist(),
                self.seo_reporter(),
                self.meta_description_creator(),
                self.ad_copywriter(),
                self.sem_campaign_manager(),
                self.seo_auditor(),
                self.internal_link_strategist(),
                self.content_strategist()
            ],
            tasks=[self.process_pending_tasks_task()],
            process=Process.hierarchical,
            verbose=True,
            manager_agent=self.manager()
        )
