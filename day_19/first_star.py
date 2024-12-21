from tqdm import tqdm


def import_data(path: str) -> tuple[set[str], set[str]]:
    with open(path, 'r') as file:
        a, b = file.read().strip().split("\n\n")
        avalable_towels = set(a.strip().split(", "))
        required_towels = set(b.strip().split("\n"))
    return avalable_towels, required_towels

def find_matching_patterns(target: str, towel_patterns: set[str]) -> bool:
    # Create a memoization dictionary to store results of subproblems
    memo = {}

    def can_construct(remaining: str) -> bool:
        if remaining == "":
            return True
        if remaining in memo:
            return memo[remaining]

        for pattern in towel_patterns:
            if remaining.startswith(pattern):
                suffix = remaining[len(pattern):]
                if can_construct(suffix):
                    memo[remaining] = True
                    return True

        memo[remaining] = False
        return False

    return can_construct(target)

def main():
    towel_patterns, needed_patterns = import_data("input.txt")
    result = 0
    print(f"Available towels: {towel_patterns}")
    print(f"Necessary towels: {needed_patterns}")
    for patterns in tqdm(needed_patterns):
        if find_matching_patterns(patterns, towel_patterns):
            result += 1
            print(f"Found matching pattern for {patterns}")
    print(f"Total matching patterns: {result}")

if __name__ == "__main__":
    main()