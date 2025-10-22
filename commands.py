STRING = 3
BOOLEAN = 5
USER = 6

dev_huddle = {
    "name": "register_devhud",
    "type": 1,
    "description": "Register a dev huddle",
    "options": [
        {
            "name": "name",
            "description": "Name of the person giving the dev huddle",
            "type": USER,
            "required": True,
        },
        {
            "name": "date",
            "description": "Provide date of the dev huddle in dd-mm-yy format please",
            "type": STRING,
            "required": True,
        },
        {
            "name": "topic",
            "description": "The topic of the dev huddle",
            "type": STRING,
            "required": True,
        },
        {
            "name": "description",
            "description": "A short description of the dev huddle",
            "type": STRING,
            "required": True,
        }
    ]
}

sample_command = {
    "name": "blep",
    "type": 1,
    "description": "Send a random adorable animal photo",
    "options": [
        {
            "name": "animal",
            "description": "The type of animal",
            "type": STRING,
            "required": True,
            "choices": [
                {
                    "name": "Dog",
                    "value": "animal_dog"
                },
                {
                    "name": "Cat",
                    "value": "animal_cat"
                },
                {
                    "name": "Penguin",
                    "value": "animal_penguin"
                }
            ]
        },
        {
            "name": "only_smol",
            "description": "Whether to show only baby animals",
            "type": BOOLEAN,
            "required": False
        }
    ]
}
