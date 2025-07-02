import json
import time
import os
import glob

CAMERA_LOG_DIRS = {
    1: "/home/muzzammil/camera1_logs/output_camera1.json",
    2: "/home/muzzammil/camera2_logs/output_camera2.json",
    3: "/home/muzzammil/camera3_logs/output_camera3.json",
    4: "/home/muzzammil/camera4_logs/output_camera4.json",
    5: "/home/muzzammil/camera5_logs/output_camera5.json",
}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_level_bar(count, max_count=20, length=30):
    filled_length = int(min(count, max_count) / max_count * length)
    bar = '█' * filled_length + '-' * (length - filled_length)
    print(f"People Count: |{bar}| {count}")

def read_json_file(file_path):
    people_count = 0
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                try:
                    frame = json.loads(line)
                except json.JSONDecodeError:
                    continue
                # Count people in this frame
                people = sum(
                    1 for obj in frame.get("objects", [])
                    if obj.get("detection", {}).get("label") == "person"
                )
                if people > people_count:
                    people_count = people
    except FileNotFoundError:
        # File may not exist yet if camera not started
        pass
    return people_count

def main():
    print("📊 LIVE MULTI-CAMERA PEOPLE COUNT DASHBOARD (Press Ctrl+C to quit)")

    try:
        while True:
            clear_console()
            total_people = 0
            for cam_id, path in CAMERA_LOG_DIRS.items():
                count = read_json_file(path)
                print(f"Camera {cam_id}:")
                print_level_bar(count)
                total_people += count
                print()

            print("="*40)
            print(f"TOTAL PEOPLE ACROSS ALL CAMERAS: {total_people}")
            print("="*40)

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nExiting dashboard...")

if __name__ == "__main__":
    main()

