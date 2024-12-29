from time import perf_counter

from helpers import calculate_checksum


def read_input(filename: str):
    disk: list[int] = []

    with open(filename, 'r') as f:
        file_id = -1
        free_space = True
        while char := f.read(1).strip():
            # Invert free_space on each character
            free_space = not free_space

            # If it's not free space, increment the file_id
            if not free_space:
                file_id += 1

            # Convert to int
            char = int(char)

            # Create entries for that id or free space
            for _ in range(char):
                if free_space:
                    disk.append(-1)
                else:
                    disk.append(file_id)

    return disk


def part1(disk: list[int]):
    free_space_ptr = 0
    file_block_ptr = len(disk) - 1

    # Continually move blocks until pointers pass each other
    while True:
        # Iterate free_space_ptr until first free space
        while disk[free_space_ptr] != -1:
            free_space_ptr += 1

        # Iterate file_block_ptr until first file block
        while disk[file_block_ptr] == -1:
            file_block_ptr -= 1

        # Break out if pointers have passed
        if not free_space_ptr < file_block_ptr:
            break

        # Swap data and free space
        disk[free_space_ptr] = disk[file_block_ptr]
        disk[file_block_ptr] = -1

    checksum = calculate_checksum(disk)

    print("part 1:", checksum)


def part2(disk: list[int]):
    free_space_blocks: list[tuple[int, int]] = []

    # Identify the blocks of free space
    free_space_ptr = 0
    while True:
        # Find beginning of free space
        while free_space_ptr < len(disk) and disk[free_space_ptr] != -1:
            free_space_ptr += 1

        # Break out once no more free space
        if free_space_ptr >= len(disk):
            break

        # Find end of free space
        end_free_space_ptr = free_space_ptr + 1
        while end_free_space_ptr < len(disk) and disk[end_free_space_ptr] == -1:
            end_free_space_ptr += 1

        # Add this free space
        free_space_blocks.append((free_space_ptr, end_free_space_ptr))

        # Set ptr to the end to start again
        free_space_ptr = end_free_space_ptr

    # Identify file blocks and try to move them
    end_file_block_ptr = len(disk) - 1
    while True:
        # Find end of file
        while end_file_block_ptr >= 0 and disk[end_file_block_ptr] == -1:
            end_file_block_ptr -= 1

        # Break out once no more files
        if end_file_block_ptr < 0:
            break

        file_id = disk[end_file_block_ptr]

        # Find beginning of file
        beg_file_block_ptr = end_file_block_ptr - 1
        while beg_file_block_ptr >= 0 and disk[beg_file_block_ptr] == file_id:
            beg_file_block_ptr -= 1

        # File exists from beg + 1:end + 1
        file_size = end_file_block_ptr - beg_file_block_ptr

        # Find free space block that could fit the file
        for i, block in enumerate(free_space_blocks):
            # Stop once considering blocks that are right of the file
            if block[0] > end_file_block_ptr:
                break

            block_size = block[1] - block[0]

            # Ignore blocks that are too small
            if block_size < file_size:
                continue

            # Place file into spot
            for j in range(file_size):
                disk[block[0] + j] = file_id

            # Update where file used to be to free space
            for j in range(end_file_block_ptr, beg_file_block_ptr, -1):
                disk[j] = -1

            # Delete free space block if all space used
            if block_size == file_size:
                del free_space_blocks[i]
            else:
                free_space_blocks[i] = (block[0] + file_size, block[1])

            # File is swapped, move on
            break

        # Set ptr to the beg to start again
        end_file_block_ptr = beg_file_block_ptr

    checksum = calculate_checksum(disk)

    print("part 2:", checksum)


def main():
    filename = "day9/sample_input4.txt"

    start = perf_counter()
    disk = read_input(filename)
    end = perf_counter()
    print(f"read input: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part1(disk.copy())
    end = perf_counter()
    print(f"part 1: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part2(disk.copy())
    end = perf_counter()
    print(f"part 2: {round((end-start) * 1000)}ms")


if __name__ == "__main__":
    main()
