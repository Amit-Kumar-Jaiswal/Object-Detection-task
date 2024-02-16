import os
import numpy as np
import glob
import shutil

mydir = "/home/amit/Downloads/task1/3_classes/Tigers"
file_list = glob.glob(mydir + "/*.jpg")

def split_list_randselect(lst, train_size_percent, valid_size_percent):
    train_list = np.random.choice(lst, size=int(train_size_percent * len(lst)/100.0), replace=False)
    valid_list = np.random.choice(train_list, size=int(valid_size_percent * len(train_list)/100.0), replace=False)

    test_list = [i for i in (set(lst) - set(train_list))]
    train_list = [i for i in (set(train_list) - set(valid_list))]

    return train_list, valid_list, test_list

train_list, valid_list, test_list = split_list_randselect(file_list, train_size_percent=90, valid_size_percent=30)

print(len(train_list))
print(len(valid_list))
print(len(test_list))
folder_list = ["train", "valid", "test"]
for folder in folder_list:
    if os.listdir(mydir+f"/{folder}"):
        shutil.rmtree(mydir+f"/{folder}")
    os.makedirs(mydir+f"/{folder}", exist_ok=True)

mapper = {
    "train": train_list,
    "valid": valid_list,
    "test": test_list
}

for folder in folder_list:
    for file_name in mapper[folder]:
        image_name = file_name.split('/')[-1]
        print(file_name)
        print(image_name)
        name = image_name.split('.')[0]
        if os.path.exists(os.path.join(mydir+"/"+ name + ".jpg")) and os.path.exists(os.path.join(mydir+"/"+ name + ".txt")):
            txt_file = os.path.join(mydir+"/"+ name + ".txt")
            if os.path.exists(txt_file):
                shutil.copy(mydir+"/"+name+".jpg", mydir+f"/{folder}/"+name+".jpg")
                shutil.copy(mydir+"/"+name+".txt", mydir+f"/{folder}/"+name+".txt")

            else :
                print('File does not exist')

        