class MemoryPartition:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.occupied = False
        self.process_name = None
        self.process_size = 0


class Job:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def allocate_memory(partitions, jobs):
    waiting_jobs = []
    for job in jobs:
        allocated = False
        for partition in partitions:
            if not partition.occupied and partition.size >= job.size:
                partition.occupied = True
                partition.process_name = job.name
                partition.process_size = job.size
                allocated = True
                break
        if not allocated:
            waiting_jobs.append(job)
    return waiting_jobs


def print_memory_status(partitions, waiting_jobs):
    print("Memory Status:")
    for partition in partitions:
        if partition.occupied:
            print(f"{partition.name} ({partition.size}) | {partition.process_name} {partition.process_size}({partition.size - partition.process_size})")
        else:
            print(f"{partition.name} ({partition.size})")
    print("Waiting Jobs:", ", ".join(job.name for job in waiting_jobs))


def main():
    num_partitions = int(input("Enter number of partitions: "))
    partitions = []
    for i in range(num_partitions):
        name = input(f"Enter Partition Name for partition {i+1}: ")
        size = int(input(f"Enter Partition Size for partition {i+1}: "))
        partitions.append(MemoryPartition(name, size))

    num_jobs = int(input("Enter number of Jobs: "))
    jobs = []
    for i in range(num_jobs):
        name = input(f"Enter Job Name: ")
        size = int(input(f"Enter Job Size: "))
        jobs.append(Job(name, size))

    waiting_jobs = allocate_memory(partitions, jobs)
    print_memory_status(partitions, waiting_jobs)


if __name__ == "__main__":
    main()
