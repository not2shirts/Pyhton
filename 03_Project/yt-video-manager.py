import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            data =  json.load(file)
            print(data)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_videos_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


# [{"name": "soemthing", "link": "https//ndjndscn" , "length" : "50min" }]
def list_all_videos(videos):
    print("*"*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index} . {video["name"]}\n\t Link: {video["link"]} \n\t Length: {video["length"]} \n")
    print("*"*70)


def add_video(videos):
    name = input("Enter title of the video : ")
    link = input("Enter link of the video : ")
    length = input("Enter length of the video : ")
    videos.append({"name": name, "link": link, "length": length })
    save_videos_helper(videos)



def update_detail(videos):
    list_all_videos(videos)
    vid= int(input("Enter the video number to update details : "))
    if   0 < vid <= len(videos):
        print("Enter the new details : \n")
        name = input("Enter title of the video : ")
        link = input("Enter link of the video : ")
        length = input("Enter length of the video : ")
        videos[vid -1] = {"name": name, "link": link, "length": length }
        save_videos_helper(videos)
    else:
        print("Video Doesn't exist !! please enter correct video number")


def delete_video(videos):
    list_all_videos(videos)
    vid= int(input("Enter the video number to delete : "))
    if   0 < vid <= len(videos):
        del videos[vid -1]
        save_videos_helper(videos)
    else:
        print("Video Doesn't exist !! please enter correct video number")



def main():
    videos  = load_data()
    while True:
        print("1. List all Youtube Videos\n")
        print("2. Add a Youtube Video\n")
        print("3. Update a youtube video details\n")
        print("4. Delete a Youtube video\n")
        print("5. Exit\n")
        choice =  input("\n Enter your choice\t")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_detail(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Enter a valid choice !!")


if __name__ == "__main__":
 main()
