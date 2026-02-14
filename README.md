OpenARC-Reason: A Free-Tier Neurosymbolic Solver
OpenARC-Reason is a neurosymbolic AI system designed to solve the ARC-AGI (Abstraction and Reasoning Corpus) benchmark.

Unlike traditional "black box" solvers that try to guess the output pixels directly, this project uses Program Synthesis. It looks at the input/output examples, determines the underlying logic, and writes a Python program to solve the puzzle.

Crucially, this entire stack is built to run on the FREE TIER. It leverages the massive context window of Google's Gemini 2.0 Flash (via AI Studio) to reason about puzzles without API costs.
