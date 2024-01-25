file_name = input("Name for cue sheet: ")
print("\nCreating cue sheet\n")
f = open(file_name + ".cue", "a", encoding="utf-8")

while True:
    smart_capitalizing = input("Enable smart capitalizing for file? (Y/N): ")
    if smart_capitalizing.lower() == "y":
        smart_capitalizing = True

        def smart_title(s):
            return " ".join(w if w.isupper() else w.capitalize() for w in s.split())

        break
    if smart_capitalizing.lower() == "n":
        smart_capitalizing = False

        def smart_title(s):
            return " ".join(w for w in s.split())

        break
    else:
        print("\nPlease enter 'Y' for YES or 'N' for NO\n")
        continue

album_performer = (
    'PERFORMER "' + smart_title(input("\nAlbum PERFORMER: ").strip()) + '"'
)
album_title = 'TITLE "' + smart_title(input("Album TITLE: ").strip()) + '"'
while True:
    try:
        album_file = smart_title(input("Album audio FILE: ").strip())
        if len(album_file.split(".")[1]) != 3 and len(album_file.split(".")[1]) != 4:
            print("\nPlease include audio file extension\n")
            continue
        album_file = 'FILE "' + album_file + '" ' + album_file.split(".")[1].upper()
    except Exception:
        print("\nPlease include audio file extension\n")
        continue
    else:
        break
while True:
    try:
        album_track_total = int(input("Album total tracks: ").strip())
    except ValueError:
        print("\nPlease enter an integer\n")
        continue
    else:
        break
track_number = 0

print("\nStarting cue sheet writing")
f.write(album_performer + "\n")
f.write(album_title + "\n")
f.write(album_file + "\n")

for x in range(album_track_total):
    print("\nType 'EXIT' to stop feed\n")
    track_number += 1
    track_performer = input("Track " + str(track_number) + " PERFORMER: ").strip()
    if track_performer == "EXIT":
        break
    else:
        track_title = input("Track " + str(track_number) + " TITLE: ").strip()
        while True:
            track_index = input("Track " + str(track_number) + " INDEX: ").strip()
            if not ":" in track_index:
                print(
                    "\nPlease enter INDEX in (hours) minutes and seconds seperated by colons [h:mm:ss or mm:ss]\n"
                )
                continue
            else:
                index_error = False
                counter = 0
                for y in range(len(track_index.split(":"))):
                    if len(track_index.split(":")) == 2:
                        if (
                            len(track_index.split(":")[counter]) != 2
                            or int(track_index.split(":")[1]) > 59
                        ):
                            index_error = True
                    if len(track_index.split(":")) == 3:
                        if (
                            len(track_index.split(":")[counter]) > 2
                            or int(track_index.split(":")[2]) > 59
                        ):
                            index_error = True
                    counter += 1
                if not track_index.replace(":", "").isnumeric() or index_error:
                    print(
                        "\nPlease enter INDEX in (hours) minutes and seconds seperated by colons [h:mm:ss or mm:ss]\n"
                    )
                    continue
                else:
                    if len(track_index) > 5:
                        index_hour = int(track_index.split(":")[0]) * 60
                        track_index = track_index.split(":")
                        track_index[1] = int(track_index[1]) + index_hour
                        track_index = str(track_index[1]) + ":" + str(track_index[2])
                    break
        if x < 9:
            f.write("  TRACK 0" + str(track_number) + " AUDIO\n")
        else:
            f.write("  TRACK " + str(track_number) + " AUDIO\n")
        f.write('    PERFORMER "' + smart_title(track_performer) + '"\n')
        f.write('    TITLE "' + smart_title(track_title) + '"\n')
        f.write("    INDEX 01 " + str(track_index) + ":00\n")

print("\nEnding cue sheet writing\n")
f.close()

f = open(file_name + ".cue", "r", encoding="utf-8")
print(f.read())
