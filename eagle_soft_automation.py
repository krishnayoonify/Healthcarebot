import time
import requests
import os
from eagle_soft_prod_code import open_eaglesoft, process_request
import json

BASE_URL = "http://127.0.0.1:8000/api"  # Replace with your Django app domain
POLL_INTERVAL = 1  # Poll every 60 seconds


def get_pending_tasks():
    response = requests.get(f"{BASE_URL}/tasks/pending/")
    if response.status_code == 200:
        return response.json()
    return []


def update_task_status(task_id, status, result=None):
    data = {"status": status, "result": json.dumps(result)}
    files = {}
    # Add images to the files dictionary
    if result:
        for i, image_path in enumerate([result["image"], result["xray"]]):
            if os.path.exists(image_path):
                files[f"image{i+1}"] = open(image_path, "rb")
    print(f"posting {data}")

    response = requests.post(
        f"{BASE_URL}/tasks/update/{task_id}/", data=data, files=files
    )
    if result:
        for file in files.values():
            file.close()
        for i, image_path in enumerate([result["image"], result["xray"]]):
            if os.path.exists(image_path):
                os.remove(image_path)
    return response.status_code == 200


def execute_gui_task(task):
    # Replace with your actual GUI automation logic
    try:
        name = task.get("parameters").get("name", None)
        if name:
            result = process_request()
        else:
            result = {"error": "No User Name given"}

        return "completed", result
    except Exception as e:
        return "failed", {"error": str(e)}


def main():
    open_eaglesoft()
    while True:
        tasks = get_pending_tasks()
        for task in tasks:
            task_id = task["id"]
            try:
                print(f"Got task {task_id} ")
                # update_task_status(task_id, "in_progress")  # TODO: uncomment this
                status, result = execute_gui_task(task)
                print(f"Finished task {task_id} result {result}")
                update_task_status(task_id, status, result)
            except Exception as e:
                print(e)
                update_task_status(task_id, "pending")
        time.sleep(POLL_INTERVAL)
        print("P O L L I N G")


if __name__ == "__main__":
    main()
