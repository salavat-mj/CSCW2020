import pandas as pd
from pathlib import Path


FILE="Metadata.csv"
PATH='./RecoverTags/Dribbble_test/website/'


def main():
    """ get pwd img """
    path = Path(PATH)
    id = [int(p.stem) for p in path.glob('Images/*')]

    """ load dataset """
    data = pd.read_csv(FILE,encoding='ISO-8859-15', header = None, low_memory = False, index_col=0)
    series = data[5]
    # df = df.dropna(axis=0,how='any')
    # df = df.str.strip().str.split("   ")
    # exceptions = ["ui", "user interface", "user_interface", "userinterface"]
    # df = df.apply(lambda tags: [x for x in tags if x not in exceptions])
    
    """ save data """
    tags = series[id].str.strip().str.replace('   ', ',')
    for number, current_tags in tags.items():
        with open(f'./{path}/Tags/{number}.txt', 'w+') as f:
            f.write(current_tags)
            print(f'./{path}/Tags/{number}.txt')


if __name__ == "__main__":
    main()
