from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Coder():
    """Coder crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def coder_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['coder'], # type: ignore[index]
            verbose=True,
            allow_code_execution=False, # This allows the agent to execute code in a safe environment. Use with caution!
            code_execution_config="safe",
            max_execution_time=30, # Maximum time (in seconds) allowed for code execution. Adjust as needed.
            max_retry_limit = 5,
        )  
         
    @task
    def coding_task(self) -> Task:
        return Task(
            config=self.tasks_config['coding_task'], # type: ignore[index]
        )
        
    @crew
    def crew(self) -> Crew:
        
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = True,
        )
    
