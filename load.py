from datasets import load_dataset
from datasets.download.download_config import DownloadConfig
config = DownloadConfig(max_retries=3)
dataset = load_dataset("gsm8k", "main", download_config=config)

# save to json file
for split in dataset.keys():
    dataset[split].to_json(split + '.json', orient='records', lines=True)
