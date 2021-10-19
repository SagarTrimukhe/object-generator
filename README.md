# object-generator
Want to quickly generate an array of objects of required structure?
Here is a Python script!!

### How to use it?

Step 1:  Put the JSON object in the input.json file

Step 2: Check the config.ini file. It you want to modify the length of strings and numbers, do so and Save it.

Step 3: Run the object_generator.py file. 

Note: Remember to pass the number of objects as arguments. 

Check the output.json file. You will have the required array.


### Examples 
1. Simple object

input.json file
```
{
    "name":"test",
    "age":12
}
```

config.ini file
```
[LENGTH]
String=10
Integer=2
```

output.json file WILL CONTAIN following result after running
###### python objects_generator.py 3
```
[
	{
		"name": "xzQvqgBEDm",
		"age": 71
	},
	{
		"name": "nYNpySXrMA",
		"age": 17
	},
	{
		"name": "OepitXWBRo",
		"age": 55
	}
]
```

2. Object with arrays
input.json file
```
{
    "name":"Amar",
    "friends":["John","sagar","Malik"],
    "major": true
}
```

config.ini file
```
[LENGTH]
String=10
Integer=2
```

output.json file WILL CONTAIN following result after running
###### python objects_generator.py 2
```
[
	{
		"name": "ppZIRHXiVm",
		"friends": [
			"ybvtUFInkZ",
			"Yfpebjmmlf",
			"TuCynvQrnl"
		],
		"major": true
	},
	{
		"name": "KtBulTOOXC",
		"friends": [
			"vbCrPnpXSP",
			"peUbcojuqs",
			"KQcjRlEbgc"
		],
		"major": false
	}
]
```

3. Nested Object
input.json file
```
{
    "name":"Amar",
    "age": 12,
    "id": "abcd",
    "address": {
      "house_no": 12,
      "street": "abcd",
      "state": "xyz",
      "pincode": 50
    }
}
```

config.ini file
```
[LENGTH]
String=10
Integer=2
```

output.json file WILL CONTAIN following result after running
###### python objects_generator.py 2
```
[
	{
		"name": "digMPayNaG",
		"age": 94,
		"id": "ryExYQXmVj",
		"address": {
			"house_no": 80,
			"street": "EXaGZEYFdb",
			"state": "rWSaHSRPXQ",
			"pincode": 68
		}
	},
	{
		"name": "ZkvKysKRqs",
		"age": 54,
		"id": "zqZUJgVQNG",
		"address": {
			"house_no": 38,
			"street": "qwRZHJWKNz",
			"state": "vuxJfwqfvX",
			"pincode": 94
		}
	}
	
]
```


