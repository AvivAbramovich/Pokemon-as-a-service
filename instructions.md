# PaaS - Pokemon as a Service

## Practical Part
Build an API service (using `python` and `flask`), by the following specifications.

### 1. "Create a new Pokemon" endpoint -  
* Gets a JSON object of a Pokemon
* Validates the input
* Index it in ElasticSearch

Here are 2 examples of Pokemon objects:

```javascript
// Possible pokemon types are : ["ELECTRIC", "GROUND", "FIRE", "WATER", "WIND", "PSYCHIC", "GRASS"]
```
 ```javascript
{
    "pokadex_id": 25,
    "name": "Pikachu",
    "nickname": "Baruh Ha Gever",
    "level": 60,
    "type": "ELECTRIC",
    "skills": [
        "Tail Whip",
        "Thunder Shock",
        "Growl",
        "Play Nice",
        "Quick Attack",
        "Electro Ball",
        "Thunder Wave"
    ]
}
```
```javascript
{
    "pokadex_id": 1,
    "name": "Bulbasaur",
    "nickname": "Gavrial",
    "level": 20,
    "type": "GRASS",
    "skills": [
        "Tackle",
        "Growl",
        "Vine Whip",
        "Poison Powder",
        "Sleep Powder",
        "Take Down",
        "Razor Leaf",
        "Growth"
    ]
}
```


### 2. "Auto-complete" endpoint

- This end point will get a simple query-string argument (like: "gr") 
- Will return the Pokemon objects that one of their TEXT fields contains (as a prefix of a word) our query-string-argument
- Implement some simple caching for those search API
       

**NOTICE** - Pokemon's TEXT fields can change often (tomorrow we will add `evolve_to` field). 
Design your solution, knowing that our autocomplete should support those new fields as well!

Examples (assuming the Pokemon example in the previous section were indexed)

```javascript

// GET /api/autocomplete/pik
[
    {
        "pokadex_id": 25,
        "name": "Pikachu",
        "nickname": "Baruh Ha Gever",
        "level": 60,
        "type": "ELECTRIC",
        "skills": [
            "Tail Whip",
            "Thunder Shock",
            "Growl",
            "Play Nice",
            "Quick Attack",
            "Electro Ball",
            "Thunder Wave"
        ]
    }
]
```

```javascript
// GET /api/autocomplete/grow
[
    {
        "pokadex_id": 25,
        "name": "Pikachu",
        "nickname": "Baruh Ha Gever",
        "level": 60,
        "type": "ELECTRIC",
        "skills": [
            "Tail Whip",
            "Thunder Shock",
            "Growl",
            "Play Nice",
            "Quick Attack",
            "Electro Ball",
            "Thunder Wave"
        ]
    },
    {
        "pokadex_id": 1,
        "name": "Bulbasaur",
        "nickname": "Gavrial",
        "level": 20,
        "type": "GRASS",
        "skills": [
            "Tackle",
            "Growl",
            "Vine Whip",
            "Poison Powder",
            "Sleep Powder",
            "Take Down",
            "Razor Leaf",
            "Growth"
        ]
    }
]
```
```javascript
// GET /api/autocomplete/geve
[
    {
        "pokadex_id": 25,
        "name": "Pikachu",
        "nickname": "Baruh Ha Gever",
        "level": 60,
        "type": "ELECTRIC",
        "skills": [
            "Tail Whip",
            "Thunder Shock",
            "Growl",
            "Play Nice",
            "Quick Attack",
            "Electro Ball",
            "Thunder Wave"
        ]
    }
]
```
 ```javascript
// GET /api/autocomplete/leaf
[
    {
        "pokadex_id": 1,
        "name": "Bulbasaur",
        "nickname": "Gavrial",
        "level": 20,
        "type": "GRASS",
        "skills": [
            "Tackle",
            "Growl",
            "Vine Whip",
            "Poison Powder",
            "Sleep Powder",
            "Take Down",
            "Razor Leaf",
            "Growth"
        ]
    }
]
```

### 3. Theoretical Part (NO CODE)

Now we would like to collect usage-log, of our API (in your service), as used by our users.
- We want to log all requests, even if they had failed
- We want to be able to identify the order of which a specific user, used our API (assume that there is a authentication mechanism) 
- We may have multiple instances of the server you created.
- In the future we would want to run analytics over those logs, so it would be a nice benefit to have easy and simple access to them

#### Questions, answer in your words:
- How would you implement it? where would you store it? 
- What would you do differently in a much larger scale of data and usage