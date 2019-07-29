def sanitize(data):
    if data == None or data == "":
        return False
    # remove the spaces from the data
    data = data.replace(" ", "")
    return data
