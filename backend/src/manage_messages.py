import json
new_item = "I want to learn a new hobby that is not too hard but is fun. I am working full time and have a family so I also do not have a whole lot of free time. I should be something that I do not need much equipment for and can be done by myself"

def add_to_messages(new_item : str):
    with open('./backend/messages.json', 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    if not isinstance(data, list):
        raise ValueError("Expected JSON file to contain a list, but got " + type(data).__name__)

    data.append({"role": "user", "content": f"{new_item}"})

    with open('./backend/messages.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)

def reset_messages():
    messages = [
        {
            "role": "user",
            "content": "You are a Search-Parameter Generator for the YouTube Data API’s search.list() method. When given a broad topic, do the following:\n\n1. Break the topic into 10-12 meaningful subtopics.\n2. For each subtopic, emit a JSON object whose keys are valid parameters for youtube.search().list(), plus a \"subtopic\" label. At minimum include:\n   - \"part\": \"snippet\"\n   - \"q\": the query string\n   - \"type\": \"video\"\n   - \"maxResults\": number of items to fetch (always 5)\n   - \"order\"\n   - \"videoDuration\"\n   - \"videoDefinition\"\n   - \"safeSearch\"\n   - \"relevanceLanguage\"\n3. Tailor each parameter value to suit the subtopic (e.g. longer durations for documentary subjects).\n4. Output a pure JSON array of these objects—no extra text.\nOne more thing to note is that I would like you to try to make the q prompts all be worded uniquely and have few similar words so that I get the largest variety."
        },
        {
            "role": "assistant",
            "content": "Sure— I can do that. What broad topic would you like me to generate YouTube search parameters for?"
        }
    ]
    with open('./backend/messages.json', 'w', encoding='utf-8') as outfile:
        json.dump(messages, outfile, indent=4, ensure_ascii=False)