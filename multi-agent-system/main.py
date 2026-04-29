from core.orchestrator import Orchestrator

if __name__ == "__main__":
    task = "分析电商转化率下降的原因，并给出优化策略"

    orchestrator = Orchestrator()
    result = orchestrator.run(task)

    print("\n================ FINAL RESULT ================\n")
    print(result)