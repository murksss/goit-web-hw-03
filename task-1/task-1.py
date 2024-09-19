import shutil
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


def copy_img_to_dist(file_path: Path, dist_path: Path) -> None:
    target_dir = file_path.suffix.split('.')[1]
    file_name = file_path.name

    dist_path = dist_path.joinpath(target_dir)
    dist_path.mkdir(parents=True, exist_ok=True)
    dist_path = dist_path.joinpath(file_name)

    print(f'Copying {file_path} to {dist_path}')

    shutil.copy(file_path, dist_path)


def process_directory_with_pathlib(source_dir: Path, target_dir: Path) -> None:

    with ThreadPoolExecutor(max_workers=3) as executor:
        futurres = []
        for file_path in source_dir.rglob('*'):
            if file_path.is_file():
                # futurres.append(executor.submit(copy_img_to_dist, file_path, target_dir))
                executor.submit(copy_img_to_dist, file_path, target_dir)


def main():
    args = sys.argv[1:]

    if not args:
        print('Enter directory path')
        return 0

    if len(args) == 1:
        target_dir = Path('dist')
        target_dir.mkdir(parents=True, exist_ok=True)

    else:
        target_dir = Path(args[1])
        target_dir.mkdir(parents=True, exist_ok=True)

    source_dir = Path(args[0])
    process_directory_with_pathlib(source_dir, target_dir)


if __name__ == '__main__':
    main()
