from . import ai
import time


def vibesort(arr: list[int]) -> list[int]:
    result, _ = ai.vibesort(arr)
    return result


def benchmark_vibesort(arr: list[int] = None) -> None:
    """Benchmark vibesort vs sorted()"""
    if arr is None:
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
    
    # GPT-4o-mini pricing: $0.00015/1K input tokens, $0.0006/1K output tokens
    input_price_per_1k = 0.00015
    output_price_per_1k = 0.0006
    
    expected = sorted(arr)
    vibesort_times = []
    vibesort_results = []
    sorted_times = []
    total_input_tokens = 0
    total_output_tokens = 0
    
    print(f"Input: {arr}")
    print()
    
    # Run both methods 5 times for statistical comparison
    for i in range(5):
        # Test vibesort
        start = time.time()
        result, usage = ai.vibesort(arr)
        vibesort_time = time.time() - start
        vibesort_times.append(vibesort_time)
        
        # Track actual token usage
        total_input_tokens += usage["prompt_tokens"]
        total_output_tokens += usage["completion_tokens"]
        
        # Calculate real cost for this call
        real_cost = (usage["prompt_tokens"] * input_price_per_1k / 1000 + 
                    usage["completion_tokens"] * output_price_per_1k / 1000)
        
        correct = result == expected
        vibesort_results.append(correct)
        vibesort_status = "✓" if correct else "✗"
        
        # Test sorted() for comparison
        start = time.time()
        sorted(arr)
        sorted_time = time.time() - start
        sorted_times.append(sorted_time)
        
        print(f"Test {i+1}: vibesort {vibesort_time:.3f}s ${real_cost:.6f} {usage['total_tokens']}tok {vibesort_status}  |  sorted() {sorted_time:.6f}s $0.000000 ✓")
    
    # Calculate averages and total cost
    avg_vibesort_time = sum(vibesort_times) / len(vibesort_times)
    avg_sorted_time = sum(sorted_times) / len(sorted_times)
    total_cost = (total_input_tokens * input_price_per_1k / 1000 + 
                 total_output_tokens * output_price_per_1k / 1000)
    
    # Display summary
    print()
    print(f"Average vibesort: {avg_vibesort_time:.3f}s  ${total_cost:.6f}  {total_input_tokens + total_output_tokens}tok  ({sum(vibesort_results)}/5 correct)")
    print(f"Average sorted(): {avg_sorted_time:.6f}s  $0.000000      0tok      (5/5 correct)")
    print()
    print(f"vibesort is {avg_vibesort_time/avg_sorted_time:.0f}x slower and costs ${total_cost:.6f}!")
