import subprocess

scripts = [
    "src/problem2_numpy.py",
    "src/problem3_element.py",
    "src/problem4_function.py",
    "src/problem5_check.py",
    "src/problem6_transpose.py"
]

for i, script in enumerate(scripts, start=2):
    print(f"\n=== Running Problem {i} ===")
    subprocess.run(["python", script])
