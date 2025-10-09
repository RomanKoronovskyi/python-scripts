## Clean-archive task

Create script clean_app.py that::

- Take a zip archive name as an argument
- Unzip the archive to a temp directory
- Remove folders that don't contain __init__.py. Only the root folder can be without __init__.py
- Add cleaned.txt with a sorted list of the removed folders
- Create new archive with _new prefix (<old_name>_new.zip)
- Add logging to the script

---

## Requirements

- Python 3.10+
- Python modules:
  - `os`
  - `sys`
  - `shutil`
  - `tempfile`
  - `logging`

## Usage

To run the snapshot monitor script, use the following command:

```bash
python clean_app.py [zip-file name] 
```
