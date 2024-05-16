import hashlib

class BasicAntivirus:
    def __init__(self):
        self.virus_db = ['2c1e66cbb82b58c818711649b6e5b2af']  # This is an example of a different file's MD5 Hash, replace with real virus signatures

    def scan_file(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
            md5_hash = hashlib.md5(data).hexdigest()
            if md5_hash in self.virus_db:
                return True
            else:
                return False

if __name__ == "__main__":
    av = BasicAntivirus()
    result = av.scan_file('test.txt')
    if result:
        print("Malware detected!")
    else:
        print("File is clean.")
