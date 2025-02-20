from langgraph.func import entrypoint, task

@task
def task1() -> str:
    print("Task 1")
    return "Task 1 Executed"

@task
def task2() -> str:
    print("Task 2")
    return "Task 2 Executed"

# Runnable Using Pregal
@entrypoint()
def run_flow(input: str):
    print("Running Simple Flow", input)
    task1_output = task1().result()
    task2_output = task2().result()
    return f"Workflow Executed Successfully With Outputs: {task1_output} and {task2_output}"

# Run The Workflow
def run_chain():
    run_flow.invoke(input="Simple Input")
    for event in run_flow.stream(input="Simple Input"):
        print(event)