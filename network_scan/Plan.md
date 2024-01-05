Write a script that will scan a network and add device to netbox.

scan network.
- ~~First how do I ping an ip address?~~
- ~~user inputs a network~~
  - I should add some validation here
- I find all ip addresses of that network and ping them.
  - I want to find a way to multithread this process. my way currently works but its too slow.
try to log into any device that responds to a ping.
create a object based off the devices that i can log into.
create an api call that will populate netbox.