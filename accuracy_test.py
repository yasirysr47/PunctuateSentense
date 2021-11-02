from FastPunct import FastPunct
fastpunct = FastPunct()

original_file = "sentence.txt"
input_file_with_no_punct = "no_punct_sentence.txt"
predicted_file = "prediction.txt"


status_report = {"PASS": 0, "FAIL":0, "ACCURACY":0}

def check_accuracy_sentence():
    i = 0
    orig_file = open(original_file, 'r')
    pred_file = open(predicted_file, 'w+')
    with open(input_file_with_no_punct, "r") as fp:
        for sent in fp:
            original_line = orig_file.readline().strip()
            prediction_sent = fastpunct.punct(sent, correct=True)
            pred_file.write(prediction_sent)

            if original_line==prediction_sent:
                status_report["PASS"] += 1
            else:
                status_report["FAIL"] += 1
            i+=1
            if i == 100:
                break

    orig_file.close()
    pred_file.close()         
    accuracy = status_report["PASS"]/(status_report["PASS"]+status_report["FAIL"])
    status_report["ACCURACY"] = "{}%".format(accuracy*100)


check_accuracy_sentence()
print(status_report)