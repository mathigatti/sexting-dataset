import os
import sys

def join_txts(txts_folder):
	txts = os.listdir(txts_folder)

	final_text = ""

	for file_name in txts:

	 file_path = os.path.join(txts_folder, file_name) 

	 with open(file_path,'r') as f:
	  next_txt_content = f.read()
	  txts_folder = txts_folder + next_txt_content.strip() + "\n"

	with open("merged.txt",'w') as f:
	 f.write(txts_folder.strip())


if __name__ == '__main__':
	txts_folder = sys.argv[1]
	unir_txts(txts_folder)