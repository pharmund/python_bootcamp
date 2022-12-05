import json

def application(env, start_response):
    species = {
    "Cyberman": "John Lumic",
    "Dalek": "Davros",
    "Judoon": "Shadow Proclamation Convention 15 Enforcer",
    "Human": "Leonardo da Vinci",
    "Ood": "Klineman Halpen",
    "Silence": "Tasha Lem",
    "Slitheen": "Coca-Cola salesman",
    "Sontaran": "General Staal",
    "Time Lord": "Rassilon",
    "Weeping Angel": "The Division Representative",
    "Zygon": "Broton",
    }

    temp = env['REQUEST_URI'].replace("%20"," ").split("=")

    if species.get(temp[1]):
        new_dict = {"credentials": species.get(temp[1])}
        json_file = bytes(json.dumps(new_dict), 'utf8')
        start_response('200 OK', [('Content-Type','application/json')])
        return [json_file]

    else:
        empty_json_file = bytes(json.dumps({"credentials": "Unknown"}), 'utf8')
        start_response('200 OK', [('Content-Type','application/json')])
        return [empty_json_file]
