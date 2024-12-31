
def extensions():
    file=input("File name: ")
    if ".gif" in file:
        print("image/gif")   
    elif ".jpg" in file:
        print("image/jpg")
    elif "jpeg" in file:
        print("image/jpeg")
    elif ".png" in file:
        print("image/png")
    elif ".pdf" in file:
        print("image/pdf")
    elif ".txt" in file:
        print("image/txt")
    elif ".zip" in file:
        print("image/zip")    
    else:
        print("application/octet-stream")
    
extensions()