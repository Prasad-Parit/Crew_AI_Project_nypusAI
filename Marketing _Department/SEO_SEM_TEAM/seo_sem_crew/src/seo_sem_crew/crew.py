from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
    

from tools.lang_tools import DataForSEOSerpTool
from tools.custom_tool import(
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
from dotenv import load_dotenv

load_dotenv()


@CrewBase
class SeoSemCrew():
	"""SeoSemCrew crew"""

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
			tools=[SerperDevTool(),
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
			tools=[
				YoastOptimizationTool(),
				MozProTool(),
				GoogleSearchConsoleTool(),
				TaskStatusUpdate()
				
			],
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
			output_file='keyword_research_task_report.md'
		)

	@task
	def competitor_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['competitor_analysis_task'],
			output_file='competitor_analysis_task_report.md'
		)
	
	@task
	def content_optimization_task(self) -> Task:
		return Task(
			config=self.tasks_config['content_optimization_task'],
			output_file='content_optimization_task_report.md'
		)
	
	@task
	def backlink_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['backlink_analysis_task'],
			output_file='backlink_analysis_task_report.md'
		)
	
	@task
	def analytics_monitoring_task(self) -> Task:
		return Task(
			config=self.tasks_config['analytics_monitoring_task'],
			output_file='analytics_monitoring_task_report.md'
		)
	
	@task
	def seo_reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['seo_reporting_task'],
			output_file='seo_reporting_task_report.md'
		)
	
	@task
	def meta_description_task(self) -> Task:
		return Task(
			config=self.tasks_config['meta_description_task'],
			output_file='meta_description_task_report.md'
		)
	
	@task
	def ad_copy_task(self) -> Task:
		return Task(
			config=self.tasks_config['ad_copy_task'],
			output_file='ad_copy_task_report.md'
		)
	
	@task
	def sem_campaign_management_task(self) -> Task:
		return Task(
			config=self.tasks_config['sem_campaign_management_task'],
			output_file='sem_campaign_management_task_report.md'
		)
	
	@task
	def seo_audit_task(self) -> Task:
		return Task(
			config=self.tasks_config['seo_audit_task'],
			output_file='seo_audit_task_report.md'
		)
	
	@task
	def internal_linking_task(self) -> Task:
		return Task(
			config=self.tasks_config['internal_linking_task'],
			output_file='internal_linking_task_report.md'
		)
	
	@task
	def content_strategy_task(self) -> Task:
		return Task(
			config=self.tasks_config['content_strategy_task'],
			output_file='content_strategy_task_report.md'
		)
	

	@crew
	def crew(self) -> Crew:
		"""Creates the SeoSemCrew crew"""
		

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
