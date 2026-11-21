# My Coding Bot - inafanya kazi bila API Key
print("Bot imeamka! Niko tayari kufanya kazi...")

# Soma task kutoka task.txt
try:
    with open("task.txt", "r") as f:
        task = f.read()
    print(f"Task yangu leo ni: {task}")
except:
    task = "No task"

# Bot inatengeneza KCSE Calculator
code = """
def kcse_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "A-"
    elif marks >= 60:
        return "B+"
    elif marks >= 50:
        return "B"
    elif marks >= 40:
        return "C+"
    else:
        return "C and below"

print("KCSE Calculator iko tayari!")
print("Marks 85 =", kcse_grade(85))
print("Marks 65 =", kcse_grade(65))
print("Marks 45 =", kcse_grade(45))
"""

with open("output.py", "w") as f:
    f.write(code)

print("Done! Nimetengeneza output.py - nenda uka-check")
