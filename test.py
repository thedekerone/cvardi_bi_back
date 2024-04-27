import csv

# WE DON'T NEED THIS - User data could be stored to csv file 
user_data = {
    "id": data["id"],
    "username": data["username"],
    "imagename": f"{data['id']}.png"
}
success, error = append_user_to_csv(user_data)
if not success:
  return jsonify({"error": error}), 500
# users.csv file handlers - not needed.
def append_user_to_csv(user_data):
    try:
        with open('users.csv', mode='a', newline='') as file:
            fieldnames = ['id', 'username', 'imagename']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # Check if file is empty to write header
            file.seek(0, 2)  # Move the cursor to the end of the file
            if file.tell() == 0:  # If file is empty, write the header
                writer.writeheader()
            writer.writerow({'id': user_data['id'], 'username': user_data['username'], 'imagename': user_data['imagename']})
    except Exception as e:
        return False, str(e)
    return True, None
