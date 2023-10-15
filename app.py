import argparse
import json
from converter import Converter

def convert(config: dict): #work
    markdownConverter = Converter(config)
    markdownConverter.convert()
    markdownConverter.toHtml()

def argument(): #work
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML")
    parser.add_argument("-c", "--config", help="Path to the JSON configuration file", required=True)
    args = parser.parse_args()
    return args

args = argument()

with open(args.config, 'r') as config_file:
    config = json.load(config_file)

print(f"configuration: {config}\n")

print("start conversion...\n")
convert(config)
print("finish...\n")
