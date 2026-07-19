import importlib.metadata as metadata

for dist in metadata.distributions():

    try:
        files = dist.files

    except Exception as error:
        print("\nCORRUPT PACKAGE FOUND:")
        print("Package:", dist.metadata.get("Name"))
        print("Location:", dist._path)
        print("Error:", repr(error))