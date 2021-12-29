import xml.etree.ElementTree as ET

def main():
    root = ET.parse('kotus-sanalista_v1.xml').getroot()
    file = open("test.txt", "w", encoding="utf-8")
    for i in range(len(root)):
        s = root[i][0].text
        file.write(s+"\n")
        print(s)
    file.close()

if __name__ == "__main__":
    main()