from tools.base_tool import BaseTool

class SearchTool(BaseTool):

    def run(self, query):
        # 模拟搜索（可接入真实API）
        return f"[搜索结果] {query} -> 模拟数据分析结果"