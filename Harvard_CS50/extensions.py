# cut out input spaces and convert all capitals to lower letters - PDF to pdf
file_name = input("File name: ").strip().lower()

# Splitting name of file into a name and suffix
parts = file_name.rsplit('.', 1)

# EXTENSION: checking more suffixes
#image_suffixes = [".gif", ".jpeg", ".png"]

#if any(file_name.endswith(suffix) for suffix in image_suffixes):
#    print(f"image/{parts[1]}")

if file_name.endswith(".gif") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
    print(f"image/{parts[1]}")
elif file_name.endswith(".jpg"):
    print("image/jpeg")
elif file_name.endswith(".txt"):
    print("text/plain")
elif file_name.endswith(".pdf"):
    print("application/pdf")
elif file_name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
