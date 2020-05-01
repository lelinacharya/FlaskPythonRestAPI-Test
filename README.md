# Rest API Test Site Creation for Smart Device

## Usage

All response will have the form

'''json
{
    "data" : "Mixed type holding the content of the response!!"
    "message" : "Description of the action !!"
}
'''

Subsequent response definition will only detail the expected values of the 'data field'

### List of all devices

**Definition**

'GET /devices'

**Response**

- '200 OK' on success

'''json
[{
     "identifer": "lel-drone",
     "name" : "Jive Drone",
     "device-type" : "vehicle",
     "controller_gateway" : "192.168.0.2" 
}]
'''

### Register a new device

**Definition**

'POST /devices'

**Arguments**

- '"identifier":string' a globally unique identifier for the device
- '"name":string' a user friendly name for the device
- '"device_type":string' the type of device understood by client
- '"controller_gateway":string' the ip adress of the device

If the given identifier already exist , the existing device will be overwritten

**Response**

- '201 Created' on success

'''json
{
     "identifer": "lel-drone",
     "name" : "Jive Drone",
     "device-type" : "vehicle",
     "controller_gateway" : "192.168.0.2" 
}
'''

### Lookup device details

**Definition**

'GET /devices/<identifier>'

**Response**

- '404 not found' if the device doesn't exist in range
- '200 OK' on success

'''json
[{
     "identifer": "lel-drone",
     "name" : "Jive Drone",
     "device-type" : "vehicle",
     "controller_gateway" : "192.168.0.2" 
}]
'''

### Delete a device

**Definition**

'DELETE /devices/<identifier>'

**Response**

- '404 not found' if the device doesn't exist in range
- '204 content deleted' on success deletion

















