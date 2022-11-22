#path = "my_file.txt"


def write_new_record(path,new_score):
    with open(path,"w") as file:
        file.write(new_score)
    return

def read_new_record(path):
    with open(path,"r") as f:
        score = f.read()
        print(score)
    return score


