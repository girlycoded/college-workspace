def convert_seconds(total_seconds: float):
    minutes, seconds = total_seconds // 60, total_seconds % 60
    return minutes, seconds

minutes, seconds = convert_seconds(125)
print(f"Minutes: {minutes}\tSeconds: {seconds}")
print(f"{minutes}:{seconds:02d}")