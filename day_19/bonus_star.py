from tqdm import tqdm


def import_data(path: str) -> tuple[set[str], set[str]]:
    with open(path, 'r') as file:
        a, b = file.read().strip().split("\n\n")
        avalable_towels = set(a.strip().split(", "))
        required_towels = set(b.strip().split("\n"))
    return avalable_towels, required_towels

def find_matching_patterns(target: str, towel_patterns: set[str]) -> int:
    # Create a memoization dictionary to store results of subproblems
    memo = {}

    def count_ways(remaining: str) -> int:
        if remaining == "":
            return 1
        if remaining in memo:
            return memo[remaining]

        total_ways = 0
        for pattern in towel_patterns:
            if remaining.startswith(pattern):
                suffix = remaining[len(pattern):]
                total_ways += count_ways(suffix)

        memo[remaining] = total_ways
        return total_ways

    return count_ways(target)

def main():
    towel_patterns, needed_patterns = import_data("input.txt")
    total_count = 0
    print(f"Available towels: {towel_patterns}")
    print(f"Necessary towels: {needed_patterns}")
    for patterns in tqdm(needed_patterns):
        count = find_matching_patterns(patterns, towel_patterns)
        total_count += count
        print(f"Found {count} ways to match pattern {patterns}")
    print(f"Total matching patterns: {total_count}")

if __name__ == "__main__":
    main()