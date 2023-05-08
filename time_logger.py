import datetime
import json
import os


def get_current_log_file():
	log_index = 1
	while True:
		file_name = f"log_{log_index}.json"
		if not os.path.exists(file_name):
			today = datetime.datetime.now().strftime("%Y-%m-%d")
			return f"log_{log_index}_{today}.json"

		with open(file_name, "r") as f:
			logs = json.load(f)

		if len(logs) < 10:
			return file_name

		log_index += 1


def save_log(log_file, current_time, comment):
	logs = []

	if os.path.exists(log_file):
		with open(log_file, "r") as f:
			logs = json.load(f)

	logs.append({"time": current_time, "comment": comment})

	with open(log_file, "w") as f:
		json.dump(logs, f, indent=4)


def log_time_and_comment():
	while True:
		user_input = input(
		 "Press 'Enter' to log the current time or type 'q' to quit: ")

		if user_input.lower() == "q":
			break

		current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print(f"Current time: {current_time}")

		comment = input("Enter a short comment (or leave empty): ")

		log_file = get_current_log_file()
		save_log(log_file, current_time, comment)

		print(f"Log saved to {log_file}")
		print("\n---\n")


if __name__ == "__main__":
	log_time_and_comment()
