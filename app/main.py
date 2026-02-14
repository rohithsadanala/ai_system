import numpy as np
from data import load_task
from agent import generate_solution

def solve_task(task_id):
    print(f" Loading task {task_id}...")
    train_in, train_out, test_in, test_out = load_task(task_id)

    print(f"Asking gemini to write a program...")
    generated_code = generate_solution(train_in, train_out)

    local_scope = {'np' : np}

    try:
        exec(generated_code, globals(), local_scope)
        solve_func = local_scope.get('solve_func')

        if not solve_func:
            print("Error: LLM did not define a 'solve function.")
            return

        print("Validating code on training examples...")

        for i, (inp, target) in enumerate(zip(train_in, train_out)):
            prediction = solve_func(inp)
            if np.array_equal(prediction, target):
                print(f"  Example {i + 1}: PASSED")
            else:
                print(f"  Example {i + 1}: FAILED")
                return

        print("Validation passed! Generating solution for Test Input...")
        final_answer = solve_func(test_in[0])
        print("Final Answer:\n", final_answer)

    except Exception as e:
        print(f"Code execution failed: {e}")

if __name__ == "__main__":
    solve_task("007bbfb7")