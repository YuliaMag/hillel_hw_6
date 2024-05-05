import os
import shutil

# f = open("combined_files.txt", "x")
# ========================================== #

with open("combined_files.txt", "w") as comb_f:
    for path, dirs, files in os.walk("./momma_dir/"):
        for f in files:
            size = os.path.getsize(os.path.join(path, f))
            cont = shutil.copy(os.path.join(path, f), "combined_files.txt")
            if size <= 120:
                comb_f.write(f"{f}: {cont}\n")
