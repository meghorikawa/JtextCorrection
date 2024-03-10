# load data
f = open(
    'ja_sent_pairs.txt',
    'r')
# load txt file of sentence and correction pairs
data = f.read()
# split by line
sent_pairs = data.split('\n')

errors = []
corrections = []
for pair in sent_pairs:
    try:
        new_pair = pair.split('\t')
        print(new_pair)
        correction = new_pair[1]
        error = new_pair[0]
        errors.append(error)
        corrections.append(correction)
    except Exception as e:
        print('previous value could not be added')

import pandas as pd

df = pd.DataFrame(list(zip(errors, corrections)), columns=['error', 'correction'])

print(len(df))

no_duplicates = df.drop_duplicates()
print(len(no_duplicates))

# need grammar label for T5 training
no_duplicates['error'] = 'grammar:' + no_duplicates['error']


no_duplicates.to_csv('dataset.csv', index=False)