import langdetect

from langdetect import detect

# load data
f = open(
    'japaneseSents.txt',
    'r')
# load txt file of sentence and correction pairs
data = f.read()
# split by line
sent_pairs = data.split('\n')


# check each sentence is Japanese, if not remove it.

def langDet(InputString):
    try:
        lang = detect(InputString)
    except:
        lang = 'other'
    return lang


ja_pairs = []
# iterate and remove non-japanese items
for thing in sent_pairs:
    language = langDet(thing)
    if language == 'ja':
        ja_pairs.append(thing)
        print(f'added {sent_pairs.index(thing)} of {len(sent_pairs)}')
    else:
        continue

print(f'Number of Sentence Pairs {len(ja_pairs)}')

f.close()

# write to file
new_file_name = 'ja_sent_pairs.txt'
file_to_write = open(new_file_name, 'w')

for item in ja_pairs:
    file_to_write.write(item+'\n')

file_to_write.close()
print('complete!')
