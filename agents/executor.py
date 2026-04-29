from agents.base_agent import BaseAgent
from tools.search_tool import SearchTool

class ExecutorAgent(BaseAgent):

    def __init__(self):
        super().__init__("Executor")
        self.tools = {
            "search": SearchTool()
        }

    def run(self, step):
        # 模拟调用工具
        if "数据" in step.description:
            result = self.tools["search"].run("电商数据趋势")
        else:
            result = f"执行：{step.description}"

        step.result = result
        return step