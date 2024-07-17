def convert_to_str(data):
    if isinstance(data, (int, float, bool, str, type(None))):
        # Keep primitive types as is
        return data
    elif isinstance(data, dict):
        # Convert dictionary values recursively
        return {key: convert_to_str(value) for key, value in data.items()}
    elif isinstance(data, (list, tuple)):
        # Convert list or tuple elements recursively
        return [convert_to_str(item) for item in data]
    elif isinstance(data, set):
        # Convert set elements recursively
        return {convert_to_str(item) for item in data}
    else:
        # Convert non-primitive types to string representation
        return str(data)

#
# import requests
#
# response = requests.get("https://pbs.twimg.com/media/GOpKhbdbkAASBAU?format=jpg&name=medium")
# # Check if the request was successful
# print(response)
# with open("/tmp/temp_file", 'wb') as file:
#     file.write(response.content)
# print("here")
#
#
