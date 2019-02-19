def prettify_string(string):
    for i in range(int(len(string) / 60)):
        char = string[(i+1)*60] # Awkward way of indexing from 1 (instead of 0)
        counter = 0
        while char != ' ':
            counter += 1
            char = string[(i+1)*60 + counter]

        string = string[:((i+1)*60) + counter] + "\n" + string[((i+1)*60) + counter:]

    return string




string = "hejsan jag heter det här för att jag gillar det, men eventuellt blir det svårt kan jag veta hej hej hejsan jag heter det här för att jag gillar det, men eventuellt blir det svårt kan jag veta hej hej hejsan jag heter det här för att jag gillar det, men eventuellt blir det svårt kan jag veta hej hej"

print(prettify_string(string))
