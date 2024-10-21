import csv
from playsound import playsound



def main():
    with open('./con.csv', 'a', newline='') as f:  # Use newline='' to avoid blank lines in the CSV
            writer = csv.writer(f, delimiter=",")
            while True:
                q = input("scan tag: ")
                if not q.startswith("wattro.io"):
                    print("Scan the tag with the barcode scanner first!")
                    playsound("./fail.mp3")
                    continue
                tag = q.strip("wattro.io/")
                print(tag)
                playsound("./success.mp3")
                nfc = input("hold nfc: ")
                if  nfc.startswith("wattr.io"):  # You should check nfc here, not q again
                    print("Hold the tag to the NFC reader!")
                    playsound("./fail.mp3")
                    continue
                print(nfc)
                print(tag)
                writer.writerow([tag, nfc])  # Use writerow instead of writerows for a single row
                f.flush()
                print("Data written successfully.")
                playsound("./done.mp3")


main()