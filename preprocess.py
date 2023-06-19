csv_file = [("Sarah", 28, "A"), 
        ("Sam", 32, "B"), 
        ("Jean", 21, "C"),
        ]

for row in csv_file:
    for text in row:
        text.lower()
        if text == "ok" or text == "hi" or text == "yes":
            del text
        if text.isnumeric():
            del text

        for char in text:
            if char == "." or char == "!" or char == ",":
                del text