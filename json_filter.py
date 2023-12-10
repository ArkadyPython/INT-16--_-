import json
def create_json(file_path, new_file):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = json.load(f)
        attack1_name = text['site'][0]['alerts'][0]['name']
        attack1_count = text['site'][0]['alerts'][0]['count']
        attack2_name = text['site'][0]['alerts'][1]['name']
        attack2_count = text['site'][0]['alerts'][1]['count']
        attack3_name = text['site'][0]['alerts'][2]['name']
        attack3_count = text['site'][0]['alerts'][2]['count']
        attack4_name = text['site'][0]['alerts'][3]['name']
        attack4_count = text['site'][0]['alerts'][3]['count']
        attack5_name = text['site'][0]['alerts'][4]['name']
        attack5_count = text['site'][0]['alerts'][4]['count']
        attack6_name = text['site'][0]['alerts'][5]['name']
        attack6_count = text['site'][0]['alerts'][5]['count']
        attack7_name = text['site'][0]['alerts'][6]['name']
        attack7_count = text['site'][0]['alerts'][6]['count']
        attack8_name = text['site'][0]['alerts'][7]['name']
        attack8_count = text['site'][0]['alerts'][7]['count']
        all_attacks = {
            "vulnerabilities": [
                {
                    "name": attack1_name,
                    "count": attack1_count
                },
                {
                    "name": attack2_name,
                    "count": attack2_count
                },
                {
                    "name": attack3_name,
                    "count": attack3_count
                },
                {
                    "name": attack4_name,
                    "count": attack4_count
                },
                {
                    "name": attack5_name,
                    "count": attack5_count
                },
                {
                    "name": attack6_name,
                    "count": attack6_count
                },
                {
                    "name": attack7_name,
                    "count": attack7_count
                },
                {
                    "name": attack8_name,
                    "count": attack8_count
                }
            ]
        }
    with open(new_file, 'w') as file:
        json.dump(all_attacks, file, indent=4)
new_file = "report.json"
file_path = "C:\\Users\\xxx\\Desktop\\json_all.json"
create_json(file_path, new_file)