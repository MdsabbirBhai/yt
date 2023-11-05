
def clear():
    os.system("clear")
    clear()

def show_progress_bar(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    sys.stdout.write(f"\rDownloading: {percent:.1f}% |{'=' * int(percent / 5)}{' ' * (20 - int(percent / 5))}|")
    sys.stdout.flush()

def download_youtube_video(url, save_folder):
    try:
        yt = YouTube(url, on_progress_callback=show_progress_bar)
        video = yt.streams.filter(file_extension='mp4', progressive=True).first()
        if video:
            video.download(save_folder)
            sys.stdout.write("\rVideo downloaded successfully.\n")
        else:
            print("\nCouldn't find a suitable YouTube video stream.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        

def download_facebook_video(url, save_folder):
    try:
        os.system(f"youtube-dl -f best -o '{save_folder}/%(title)s.%(ext)s' {url}")
        sys.stdout.write("\rVideo downloaded successfully.\n")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        

def download_instagram_video(url, save_folder):
    try:
        os.system(f"youtube-dl -f best -o '{save_folder}/%(title)s.%(ext)s' {url}")
        sys.stdout.write("\rVideo downloaded successfully.\n")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        

def download_tiktok_video(url, save_folder):
    try:
        os.system(f"youtube-dl -f best -o '{save_folder}/%(title)s.%(ext)s' {url}")
        sys.stdout.write("\rVideo downloaded successfully.\n")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        

def main():
    logo = r"""
┏━━━┳━━━┳━━┓┏━━┓┏━━┳━━━┓
┃┏━┓┃┏━┓┃┏┓┃┃┏┓┃┗┫┣┫┏━┓┃
┃┗━━┫┃╋┃┃┗┛┗┫┗┛┗┓┃┃┃┗━┛┃
┗━━┓┃┗━┛┃┏━┓┃┏━┓┃┃┃┃┏┓┏┛
┃┗━┛┃┏━┓┃┗━┛┃┗━┛┣┫┣┫┃┃┗┓
┗━━━┻┛╋┗┻━━━┻━━━┻━━┻┛┗━┛  
 \033[1;91m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 \033[1;34m┃ [✓] AUTHOR    \033[1;91m: \033[1;92mSABBIR             ┃
 \033[1;34m┃ [✓] TOOL      \033[1;91m: \033[1;92mRANDOM CLONE               ┃
 \033[1;34m┃ [✓] STATUS    \033[1;91m: \033[1;92mFREE                       ┃
 \033[1;34m┃ [✓] SYSTEM    \033[1;91m: \033[1;92mDATA & WIFI                ┃
 \033[1;34m┃ [✓] GITHUB    \033[1;91m: \033[1;92mMDSABBIRBHAI            ┃
 \033[1;34m┃ [✓] FACEBOOK  \033[1;91m: \033[1;92m —SABBIR SR      ┃
 \033[1;34m┃ [✓] WHATSAPP  \033[1;91m: \033[1;92m+ADCF              ┃
 \033[1;34m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
\x1b[38;5;50m⋆\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m⋆ """
    print(logo)

    try:
        num_videos = int(input("How many videos do you want to download? "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        sys.exit(1)

    save_folder = "/sdcard/mueor"  # Change this to your desired folder path in the internal storage

    for i in range(num_videos):
        print("Which One you want download Video:")
        print("1. Facebook")
        print("2. YouTube")
        print("3. Instagram")
        print("4. TikTok")
        option = int(input("Enter the option number: "))
        if option == 1:
            video_url = input(f"Enter Facebook video URL {i + 1}: ")
            print("\033[0;32m  You're video downloading... Please wait.\033[1;97m")
            time.sleep(10)  # Add a delay to make the animation visible
            download_facebook_video(video_url, save_folder)
        elif option == 2:
            video_url = input(f"Enter YouTube video URL {i + 1}: ")
            print("\033[0;32m  You're video downloading... Please wait.\033[1;97m")
            time.sleep(10)  # Add a delay to make the animation visible
            download_youtube_video(video_url, save_folder)
        elif option == 3:
            video_url = input(f"Enter Instagram video URL {i + 1}: ")
            print("\033[0;32m  You're video downloading... Please wait.\033[1;97m")
            time.sleep(10)  # Add a delay to make the animation visible
            download_instagram_video(video_url, save_folder)
        elif option == 4:
            video_url = input(f"Enter TikTok video URL {i + 1}: ")
            print("\033[0;32m  You're video downloading... Please wait.\033[1;97m")
            time.sleep(10)  # Add a delay to make the animation visible
            download_tiktok_video(video_url, save_folder)
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
