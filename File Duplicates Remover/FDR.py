import os
import hashlib
import logging

logging.basicConfig(level=logging.INFO)


def calculate_file_hash(file_path):

    """Calculate the SHA256 hash of a file."""

    hash_func = hashlib.sha256()

    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)

    return hash_func.hexdigest()


def get_album_hashes(main_directory):

    """Get all file hashes for files in subfolders (albums) within the main directory."""

    album_hashes = set()

    for root, dirs, files in os.walk(main_directory):
        for dir in dirs:
            album_path = os.path.join(root, dir)
            for album_root, _, album_files in os.walk(album_path):
                for album_file in album_files:
                    album_file_path = os.path.join(album_root, album_file)
                    file_hash = calculate_file_hash(album_file_path)
                    album_hashes.add(file_hash)

    return album_hashes


def remove_duplicates(main_directory, album_hashes):

    """Remove files in the main directory that are duplicates of files in albums."""

    deletions_count = 0

    for item in os.listdir(main_directory):

        item_path = os.path.join(main_directory, item)

        if os.path.isfile(item_path):

            file_hash = calculate_file_hash(item_path)

            if file_hash in album_hashes:
                try:
                    os.remove(item_path)
                    deletions_count += 1
                    logging.info(f"Deleted duplicate: {item_path}")

                except PermissionError:
                    logging.warning(f"Permission denied for {item_path}. Check permissions.")

                except FileNotFoundError:
                    logging.warning(f"{item_path} not found. It may have been moved or deleted.")

                except Exception as e:
                    logging.error(f"Failed to delete {item_path}: {e}")

    logging.info(f"Total duplicates deleted: {deletions_count}")


if __name__ == "__main__":

    # Replace with your main directory path
    main_dir = r'C:\Users\USUARIO\GR\Gallery\2024'
    
    # Step 1: Generate hashes for all files in subfolders (albums)
    logging.info("Calculating hashes for album files...")
    album_file_hashes = get_album_hashes(main_dir)
    
    # Step 2: Remove duplicates from the root directory
    logging.info("Removing duplicates from the root directory...")
    remove_duplicates(main_dir, album_file_hashes)