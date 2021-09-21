from pathlib import Path

path = Path("package")
print(f"is Directory Exists: {path.exists()}")
# path = Path("temp_dir")
# print(path.rmdir())

dir = Path()
for file in dir.glob("package/*.py"):
    print(file)