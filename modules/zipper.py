import zlib

def zipper(data, action):
    if action == "zip":
        return zlib.compress(data) #Returning a bytes object containing compressed data
    elif action == "unzip":
        return zlib.decompress(data) #Returns a bytes object containing the uncompressed data
    else:
        print('whats gouing on?')