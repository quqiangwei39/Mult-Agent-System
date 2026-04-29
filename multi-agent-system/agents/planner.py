from agents.base_agent import BaseAgent
from core.task import Step

class PlannerAgent(BaseAgent):

    def __init__(self):
        super().__init__("Planner")

    def run(self, task):
        steps = [
            Step("收集业务数据"),
            Step("分析用户行为"),
            Step("定位问题"),
            Step("生成优化方案")
        ]
        return steps