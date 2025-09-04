from roboto import Dataset
from pathlib import Path

input_file = Path("test.ulg")
device_id = "vehicle_001"

ds = Dataset.create(name="my_dataset_123", device_id=device_id, create_device_if_missing=True)

print(f"Created dataset: {ds.dataset_id}")

# Upload the .ulg file, retaining filename as destination
ds.upload_file(input_file, file_destination_path=input_file.name, device_id=device_id)

# Add some metadata
ds.put_metadata({
    "test_type": "night_flight",
    "weather": "rainy",
    "temperature": 20
})

# Add some tags
ds.put_tags(["night", "autonomous", "test", "rainy"])

print(f"Uploaded file '{input_file.name}' to dataset {ds.dataset_id}")
