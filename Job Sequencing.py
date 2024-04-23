def job_sequencing(jobs):
    """Greedy algorithm for Job Sequencing Problem."""
    jobs.sort(key=lambda x: x[2])  # Sort jobs based on finish time
    result = []
    prev_finish_time = 0

    for job in jobs:
        if job[1] >= prev_finish_time:
            result.append(job)
            prev_finish_time = job[2]

    return result


# Taking user input for jobs
num_jobs = int(input("Enter the number of jobs: "))
jobs = []

for i in range(num_jobs):
    job_id = input(f"Enter job ID for job {i + 1}: ")
    start_time = int(input(f"Enter start time for job {job_id}: "))
    finish_time = int(input(f"Enter finish time for job {job_id}: "))
    jobs.append((job_id, start_time, finish_time))

# Finding optimized job sequence
optimal_sequence = job_sequencing(jobs)

# Displaying the result
print("Optimized Job Sequence:")
for job in optimal_sequence:
    print(f"Job ID: {job[0]}, Start Time: {job[1]}, Finish Time: {job[2]}")
"""
Enter the number of jobs: 5
Enter job ID for job 1: A
Enter start time for job A: 1
Enter finish time for job A: 4
Enter job ID for job 2: B
Enter start time for job B: 2
Enter finish time for job B: 5
Enter job ID for job 3: C
Enter start time for job C: 5
Enter finish time for job C: 7
Enter job ID for job 4: D
Enter start time for job D: 6
Enter finish time for job D: 9
Enter job ID for job 5: E
Enter start time for job E: 8
Enter finish time for job E: 10
Optimized Job Sequence:
Job ID: A, Start Time: 1, Finish Time: 4
Job ID: C, Start Time: 5, Finish Time: 7
Job ID: E, Start Time: 8, Finish Time: 10
"""
