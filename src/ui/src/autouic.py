import os

for file in os.listdir("."):
    if os.path.splitext(file)[-1] == '.ui':
        baseName = os.path.splitext(file)[0]
        outName = f"Ui_{baseName}.py"
        if not os.path.exists(outName) or os.path.getmtime(file) > os.path.getmtime(outName):
            # print(os.path.getmtime(file) , os.path.getmtime(outName))
            print(f"Gen/Updated {outName}")
            if os.path.exists(outName):
                os.system(f"cp {outName} .{outName}")
            os.system(f"pyuic5 {file} -o {outName}")

os.chdir("../../sources")
for file in os.listdir("."):
    if os.path.splitext(file)[-1] == '.qrc':
        baseName = os.path.splitext(file)[0]
        outName = f"{baseName}_rc.py"
        if not os.path.exists(outName) or os.path.getmtime(file) > os.path.getmtime(outName):
            # print(os.path.getmtime(file) , os.path.getmtime(outName))
            print(f"Gen/Updated {outName}")
            if os.path.exists(outName):
                os.system(f"cp {outName} .{outName}")
            os.system(f"pyrcc5 {file} -o {outName}")