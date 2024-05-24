import requests
import json

# response = requests.get('https://cat-fact.herokuapp.com/facts')
# data = response.json()

# #1. ziskavani faktu
# print(data)

# #2. filtrovani faktu
# for facts in data:
#     print(facts['text'])

# #3. vytvoreni zaznamu faktu
# facts = [fact['text'] for fact in data]
# print(facts)

# #4. ocislovani faktu
# numbered_facts = [{i + 1: fact} for i, fact in enumerate(facts)]
# print(numbered_facts)

# #5. vytvoreni souboru
# with open('kocici_fakta.json', mode='w', encoding='utf-8') as file:
#     json.dump(numbered_facts, file, indent=4)

try:
    response = requests.get('https://cat-fact.herokuapp.com/facts')
    response.raise_for_status()
    data = response.json()

    facts = [fact['text'] for fact in data]
    print(facts)

    numbered_facts = [{i+1: fact} for i, fact in enumerate(facts)]
    print(numbered_facts)

    try:
        with open("kocici_fakta.json", mode="w", encoding="utf-8") as file:
            json.dump(numbered_facts, file, indent=2)
    except IOError as e:
        print(f"Chyba pri ukladani do souboru: {e}")

except requests.exceptions.RequestException as e:
    print(f"Chyba pri ziskavani dat z API: {e}")