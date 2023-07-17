def log(tag="", message=""):
    with open("log.txt", mode="w+") as log:
        log.write(f"{tag}: {message}\n")