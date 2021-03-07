import os
import hashlib
from typing import List, Tuple


def find_duplicate_files(starting_directory: str) -> List[Tuple[str]]:

    files_seen_already = {}
    stack = [starting_directory]
    duplicates: List[Tuple[str]] = []
    while stack:
        current_path = stack.pop()
        # If its a directory, go through the files and add them
        # to the stack
        if os.path.isdir(current_path):
            for path in os.path.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)
        else:
            file_contents_hash = sample_hash_file(current_path)
            # get time it was last edited
            last_time_edited = os.path.getmtime(current_path)
            if file_contents_hash in files_seen_already:
                existing_last_edited_time, existing_path = files_seen_already[file_contents_hash]
                if last_time_edited > existing_last_edited_time:
                    duplicates.append((current_path, existing_path))
                else:
                    duplicates.append((existing_path, current_path))
                    files_seen_already[file_contents_hash] = (last_time_edited, current_path)
            else:
                files_seen_already[file_contents_hash] = (last_time_edited, current_path)
    return duplicates


def sample_hash_file(path: str) -> str:
    sample_byte_size = 4000
    total_size = os.path.getsize(path)
    hasher = hashlib.sha512()
    with open(path, 'rb') as current_file:
        if total_size < sample_byte_size * 3:
            hasher.update(current_file.read())
        else:
            num_bytes_between_samples = ((total_size - sample_byte_size * 3)/2)
            for offset in range(3):
                start_of_sample = (offset*(sample_byte_size + num_bytes_between_samples))
                current_file.seek(start_of_sample)
                sample = current_file.read(sample_byte_size)
                hasher.update(sample)
    return hasher.hexdigest()
