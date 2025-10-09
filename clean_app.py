import os
import sys
import shutil
import tempfile
import logging

logging.basicConfig(
    filename="clean_app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def main():
    if len(sys.argv) != 2:
        print("Usage: python clean_app.py <zip-file name>")
        sys.exit(1)

    zf = sys.argv[1]
    deleted_dirs = []

    with tempfile.TemporaryDirectory() as tmpdir:
        logging.info(f"Unzip the archive to a temp directory: {tmpdir}")
        shutil.unpack_archive(zf, tmpdir)

        for dirpath, dirnames, filenames in os.walk(tmpdir, topdown=False):
            if dirpath == tmpdir:
                continue
            if "__init__.py" not in filenames:
                shutil.rmtree(dirpath)
                rel_path = os.path.relpath(dirpath, tmpdir)
                deleted_dirs.append(rel_path)
                logging.info(f"Remove folder: {rel_path}")

        cleaned_path = os.path.join(tmpdir, "cleaned.txt")
        with open(cleaned_path, "w") as f:
            for d in sorted(deleted_dirs):
                f.write(d + "\n")
        logging.info(f"File cleaned.txt created ({len(deleted_dirs)} deleted folders).")

        base_name = os.path.splitext(zf)[0] + "_new"
        shutil.make_archive(base_name, "zip", tmpdir)
        logging.info(f"New archive created: {base_name}.zip")

if __name__ == "__main__":
    main()



