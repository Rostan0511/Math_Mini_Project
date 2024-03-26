import random
import matplotlib.pyplot as plt
import pandas as pd


def throw_dice(n):
    return [(random.randint(1, 6), random.randint(1, 6)) for _ in range(n)]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_prime_numbers(numbers):
    prime_count = 0
    for number in numbers:
        if is_prime(sum(number)):
            prime_count += 1
    return prime_count


def perform_trials(num_trials, num_throws):
    prime_counts = []
    all_sums = []
    all_rolls = []
    sum_counts = {}  # Dictionary to store sum and its frequency

    for i in range(num_trials):
        rolls = throw_dice(num_throws)
        sums = [sum(roll) for roll in rolls]
        all_rolls.extend(rolls)
        all_sums.extend(sums)
        prime_count = count_prime_numbers(rolls)
        prime_counts.append(prime_count)

        # Update sum counts
        for sum_value in sums:
            sum_counts[sum_value] = sum_counts.get(sum_value, 0) + 1

        print(f'Trial {i + 1}: {rolls}')
        print(f'Sums in trial {i + 1}: {sums}')
        print(f'Number of prime sums in trial {i + 1}: {prime_count}')

    return prime_counts, all_sums, all_rolls, sum_counts


def draw_graph(data, title, filename):
    plt.hist(data, bins=max(data) - min(data) + 1, edgecolor='black')
    plt.title(title)
    plt.xlabel('Sum')
    plt.ylabel('Frequency')
    plt.savefig(filename)
    plt.show()


def print_table(sum_counts):
    print("\nSum\tFrequency")
    print("----\t--------")
    for sum_value, count in sum_counts.items():
        print(f"{sum_value}\t{count}")


# Perform the experiment with increasing number of trials
# Desired trial numbers
trial_numbers = [10,30,50,100,200,400,500,800,1000]

# Aggregate data for all trials
all_prime_counts = []
all_sum_counts = {}

for num_trials in trial_numbers:
    print(f'\nPerforming {num_trials} trials...')
    prime_counts, all_sums, all_rolls, sum_counts = perform_trials(num_trials, 10)

    # Print table after each trial set
    print_table(sum_counts)
    draw_graph(prime_counts, f'Count of Prime Sums vs Frequency for {num_trials} Trials', f'graph_{num_trials}.png')

    # Update aggregate data
    all_prime_counts.extend(prime_counts)
    for sum_value, count in sum_counts.items():
        all_sum_counts[sum_value] = all_sum_counts.get(sum_value, 0) + count

    # Print table of sum and frequency
    print_table(sum_counts)

    # Save the data to a CSV file
    df = pd.DataFrame({
        'Trial': list(range(1, num_trials + 1)),
        'Prime_Count': prime_counts,
    })
    df.to_csv(f'data_{num_trials}.csv', index=False)

# Display aggregate statistics for all trials
print('\nAggregate Statistics for All Trials:')
print(f'Total Trials: {sum(trial_numbers)}')
print(f'Total Prime Counts: {len(all_prime_counts)}')
print(f'Total Sum Counts:')
print_table(all_sum_counts)

# Draw aggregate graph
draw_graph(all_prime_counts, 'Aggregate Count of Prime Sums vs Frequency', 'aggregate_graph.png')
