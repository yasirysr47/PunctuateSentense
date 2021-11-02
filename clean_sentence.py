import re


input_file = "sentence.txt"
output_file = open("no_punct_sentence.txt", "w+")

def clean(sent):
    sent = sent.lower()
    sent = re.sub(r'[^\w\s]', '', sent)
    return sent

with open(input_file) as fp:
    for sentence in fp:
        new_sent = clean(sentence)
        output_file.write("{}".format(new_sent))
    





