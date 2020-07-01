# Airbnb Clone: The Console

Airbnb Clone: The Console is a command interpreter to manage our Airbnb objects. This is the first step towards building our first full web application: the Airbnb clone.

* We put in place a parent class (BaseModel) that takes care of initialization, serialization, and deserialization of our future instances.
* We create a simple flow of serialization and deserialization:<br>
Instance <-> Dictionary <-> JSON string <-> File
* We create all classes used for Airbnb: User, State, City, Place, Amenity, and Review.
* We create the first storage engine of the project: file storage.
* We create all the unittests to validate all our classes and storage engine.

## Usage

	The shell should work like this in interactive mode:

	```bash
	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit  

	(hbnb)
	(hbnb)
	(hbnb) quit
	$
	```

	The shell should work like this in non-interactive mode:

	```bash
	$ echo "help" | ./console.py
	(hbnb)
	
	Documented commands (type help <topic>):
	========================================
	help  quit
	(hbnb)
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF help quit
	(hbnb)
	$
	```

## Supported Commands
	* create: Create a new instance of specified class, save it to the JSON file, and print the id
	* show: Print the string representation of an instance based on the class name and id
	* destroy: Delete an instance based on the class name and id
	* all: Print the string representations of all instances based on the class name (or all classes if no class is specified)
	* update: Update an instance based on the class name and id by adding or updating an attribute

## Examples

	These examples show the commands with regular syntax.<br>

	```bash
	$ ./console.py
	(hbnb) create BaseModel
	249391b4-6348-4347-85d2-b01392975f37
	(hbnb) show BaseModel 249391b4-6348-4347-85d2-b01392975f37
	[BaseModel] (249391b4-6348-4347-85d2-b01392975f37) {'id': '249391b4-6348-4347-85d2-b01392975f37', 'created_at': datetime.datetime(2019, 11, 13, 22, 5, 42, 377621), 'updated_at': datetime.datetime(2019, 11, 13, 22, 5, 42, 378124)}
	(hbnb) destroy BaseModel 249391b4-6348-4347-85d2-b01392975f37
	(hbnb) show BaseModel 249391b4-6348-4347-85d2-b01392975f37
	** no instance found **
	(hbnb)
	```

	```bash
	$ ./console.py
	(hbnb) create User
	45b62ec2-acb8-47dd-82c0-11012d9a343f
	(hbnb) update User 45b62ec2-acb8-47dd-82c0-11012d9a343f name Banu
	(hbnb) show User 45b62ec2-acb8-47dd-82c0-11012d9a343f
	[User] (45b62ec2-acb8-47dd-82c0-11012d9a343f) {'id': '45b62ec2-acb8-47dd-82c0-11012d9a343f', 'name': 'Banu', 'created_at': datetime.datetime(2019, 11, 13, 22, 7, 49, 460358), 'updated_at': datetime.datetime(2019, 11, 13, 22, 7, 49, 460394)}
	(hbnb)
	```

	These examples show the commands with "<class name>.<command>()" syntax.<br>

	```bash
	$ ./console.py
	(hbnb) State.create()
	88080931-ffc2-4352-b1c8-1d1bf8edcafd
	(hbnb) State.update(88080931-ffc2-4352-b1c8-1d1bf8edcafd, name, California)
	(hbnb) State.show(88080931-ffc2-4352-b1c8-1d1bf8edcafd)
	[State] (88080931-ffc2-4352-b1c8-1d1bf8edcafd) {'updated_at': datetime.datetime(2019, 11, 13, 22, 26, 0, 582661), 'name': 'California', 'created_at': datetime.datetime(2019, 11, 13, 22, 26, 0, 582038), 'id': '88080931-ffc2-4352-b1c8-1d1bf8edcafd'}
	(hbnb) City.create()
	ad7128ed-59c6-4942-a4a1-a09100a872d9
	(hbnb) City.update(ad7128ed-59c6-4942-a4a1-a09100a872d9, name, Oakland)
	(hbnb) City.all()
	["[City] (ad7128ed-59c6-4942-a4a1-a09100a872d9) {'updated_at': datetime.datetime(2019, 11, 13, 22, 26, 25, 790329), 'name': 'Oakland', 'created_at': datetime.datetime(2019, 11, 13, 22, 26, 25, 790286), 'id': 'ad7128ed-59c6-4942-a4a1-a09100a872d9'}"]
	(hbnb)
	```

	```bash
	$ ./console.py
	(hbnb) Amenity.create()
	cb8f7cac-4120-4b64-ba65-d7c7fda5a8ad
	(hbnb) Place.create()
	7743dd1f-2d14-4f87-a161-bc39bd4e42e1
	(hbnb) Review.create()
	000cd75c-6aa5-4b66-a91f-4c3883e57e67
	(hbnb) all
	["[Place] (7743dd1f-2d14-4f87-a161-bc39bd4e42e1) {'created_at': datetime.datetime(2019, 11, 13, 22, 29, 17, 20025), 'updated_at': datetime.datetime(2019, 11, 13, 22, 29, 17, 20081), 'id': '7743dd1f-2d14-4f87-a161-bc39bd4e42e1'}", "[Review] (000cd75c-6aa5-4b66-a91f-4c3883e57e67) {'created_at': datetime.datetime(2019, 11, 13, 22, 29, 21, 705391), 'updated_at': datetime.datetime(2019, 11, 13, 22, 29, 21, 705428), 'id': '000cd75c-6aa5-4b66-a91f-4c3883e57e67'}", "[Amenity] (cb8f7cac-4120-4b64-ba65-d7c7fda5a8ad) {'created_at': datetime.datetime(2019, 11, 13, 22, 29, 12, 226034), 'updated_at': datetime.datetime(2019, 11, 13, 22, 29, 12, 226391), 'id': 'cb8f7cac-4120-4b64-ba65-d7c7fda5a8ad'}"]
	(hbnb) Amenity.destroy(cb8f7cac-4120-4b64-ba65-d7c7fda5a8ad)
	(hbnb) Place.destroy(7743dd1f-2d14-4f87-a161-bc39bd4e42e1)
	(hbnb) Review.destroy(000cd75c-6aa5-4b66-a91f-4c3883e57e67)
	(hbnb) all
	(hbnb)
	```

## Authors

	[David Corredor](https://github.com/VIDMORE)

	[Luis Sanjuan](https://github.com/luiscode92)