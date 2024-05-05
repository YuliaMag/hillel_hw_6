import os

# f = open("combined_files.txt", "x")
# ========================================== #

with open("combined_files.txt", "w") as comb_f:
    for path, dirs, files in os.walk("./momma_dir/"):
        for f in files:
            with open(os.path.join(path, f)) as file:
                data = file.read()
            size = os.path.getsize(os.path.join(path, f))
            if size <= 120 and f.endswith(".txt"):
                comb_f.write(f"{f}: {data} \n")



