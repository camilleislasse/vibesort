# Vibesort

AI-powered array sorting using GPT.

## Usage

Install the package:
```bash
pip install vibesort
```

Set your OpenAI API key as an environment variable.
```bash
export OPENAI_API_KEY=your_key_here
```

```python
from vibesort import vibesort

result = vibesort([5, 2, 8, 1, 9])
print(result)  # [1, 2, 5, 8, 9]
```

## Benchmark

Compare AI sorting vs native Python:

```python
from vibesort import benchmark_vibesort

benchmark_vibesort()
```

Example output:
```
Input: [3, 1, 4, 1, 5, 9, 2, 6]

Test 1: vibesort 0.980s $0.000025 104tok ✓  |  sorted() 0.000002s $0.000000 ✓
Test 2: vibesort 0.863s $0.000025 104tok ✓  |  sorted() 0.000004s $0.000000 ✓
Test 3: vibesort 0.832s $0.000025 104tok ✓  |  sorted() 0.000003s $0.000000 ✓
Test 4: vibesort 0.958s $0.000025 104tok ✓  |  sorted() 0.000005s $0.000000 ✓
Test 5: vibesort 0.792s $0.000025 104tok ✓  |  sorted() 0.000003s $0.000000 ✓

Average vibesort: 0.885s  $0.000123  520tok  (5/5 correct)
Average sorted(): 0.000003s  $0.000000      0tok      (5/5 correct)

vibesort is 257765x slower and costs $0.000123!
```

## Test

```bash
pytest tests/
```

## Dependencies

- openai
- pydantic  
- typing-extensions

⚠️ Requires OpenAI API key. Experimental project - not for production use.
