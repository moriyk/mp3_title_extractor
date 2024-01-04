import sys
import eyed3

def get_mp3_title(file_path):
    audiofile = eyed3.load(file_path)
    if audiofile and audiofile.tag and audiofile.tag.title:
        return audiofile.tag.title
    else:
        return "N/A"
    
def main():
    if len(sys.argv) != 2:
        print("Usage: mp3_title_extractor <mp3_file_path>")
        sys.exit(1)

    mp3_file_path = sys.argv[1]
    title = get_mp3_title(mp3_file_path)
    print(f"{title}")

if __name__ == "__main__":
    main()