from agents.base_agent import BaseAgent

class AnalystAgent(BaseAgent):

    def __init__(self):
        super().__init__("Analyst")

    def run(self, steps):
        summary = []

        for step in steps:
            summary.append(f"{step.description} -> {step.result}")

        return "\n".join(summary)