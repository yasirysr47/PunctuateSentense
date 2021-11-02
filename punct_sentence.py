from FastPunct import FastPunct
# The default language is 'english'
fastpunct = FastPunct()


def demo():
    print("SENTENCES WE ARE GOING TO TEST : ")
    print("john smiths dog is creating a ruccus\n",
                    "ys jagan is the chief minister of andhra pradesh\n",
                    "we visted new york last year in may\n",
                    'johns son peter is marring estella in jun\n',
                    'kamal hassan is a gud actr\n',
                    "this will cost 30\n"
                    )

    ans = fastpunct.punct([
                    "john smiths dog is creating a ruccus",
                    "ys jagan is the chief minister of andhra pradesh",
                    "we visted new york last year in may"
                    ])

    print(ans)
                    
    # ["John Smith's dog is creating a ruccus.",
    # 'Ys Jagan is the chief minister of Andhra Pradesh.',
    # 'We visted New York last year in May.']

    # punctuation correction with optional spell correction (experimental)

    ans = fastpunct.punct([
                    'johns son peter is marring estella in jun',
                    'kamal hassan is a gud actr',
                    "this will cost 30"], correct=True)

    print(ans)

    ans = fastpunct.punct('johns son peter is marring estella in jun', correct=True)
    print(ans)


demo()