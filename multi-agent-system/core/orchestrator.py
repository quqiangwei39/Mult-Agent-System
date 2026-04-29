from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.analyst import AnalystAgent
from core.memory import Memory
from core.task import Task
from core.logger import Logger

class Orchestrator:

    def __init__(self):
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.analyst = AnalystAgent()
        self.memory = Memory()

    def run(self, task_description):

        Logger.log("🚀 开始任务")

        task = Task(task_description)

        # 1. 规划
        Logger.log("🧠 规划阶段")
        steps = self.planner.run(task)

        # 2. 执行
        Logger.log("⚙️ 执行阶段")
        executed_steps = []
        for step in steps:
            result = self.executor.run(step)
            self.memory.save_short(result.result)
            executed_steps.append(result)

        # 3. 分析
        Logger.log("📊 分析阶段")
        final_result = self.analyst.run(executed_steps)

        Logger.log("✅ 任务完成")

        return final_result