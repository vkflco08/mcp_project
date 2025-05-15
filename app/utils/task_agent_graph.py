from langgraph.graph import END, StateGraph
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda  # 최신 기준
from typing import TypedDict, Literal

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

def analyze_task(state):
    task = state["task"]
    analysis = llm.invoke(f"이 태스크의 목적과 요약을 작성해줘: {task['description']}")
    return {"analysis": analysis.content}

def generate_steps(state):
    summary = state["analysis"]
    steps = llm.invoke(f"다음 설명을 기반으로 해야 할 작업 단계를 알려줘: {summary}")
    return {"steps": steps.content}

def store_result(state):
    # 향후 ChromaDB 저장 처리 예정 (지금은 그냥 print)
    print("✅ 최종 결과 저장:", state["steps"])
    return {}

# LangGraph 구성
def get_task_agent_graph():
    builder = StateGraph()
    
    builder.add_node("분석", RunnableLambda(analyze_task))
    builder.add_node("단계생성", RunnableLambda(generate_steps))
    builder.add_node("저장", RunnableLambda(store_result))

    builder.set_entry_point("분석")
    builder.add_edge("분석", "단계생성")
    builder.add_edge("단계생성", "저장")
    builder.add_edge("저장", END)

    return builder.compile()
