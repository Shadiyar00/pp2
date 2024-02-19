import json
f = open("data.json", "r")
temp = f.read()
dd = json.loads(temp)
print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')
for i in dd['imdata']:
    if len(i["l1PhysIf"]["attributes"]["dn"]) == 42:
        print(i["l1PhysIf"]["attributes"]["dn"] ,' '*29,i["l1PhysIf"]["attributes"]['speed'],' ' ,i["l1PhysIf"]["attributes"]['mtu'])
    else:
        print(i["l1PhysIf"]["attributes"]["dn"] ,' '*30,i["l1PhysIf"]["attributes"]['speed'],' ' ,i["l1PhysIf"]["attributes"]['mtu'])