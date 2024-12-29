def calculate_checksum(disk: list[int]):
    checksum = 0

    for i, file_id in enumerate(disk):
        if file_id == -1:
            continue

        checksum += file_id * i

    return checksum
