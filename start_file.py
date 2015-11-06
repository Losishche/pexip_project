#! /usr/bin/python3
__author__ = 'grishaev'


import json
import requests
from  auth_conf import host, user, passw
import time


### creating a new vertual audioroom ###

#declaring variables
address = 'https://%s/api/admin/configuration/v1/conference/' % host
auth_value = (user, passw)
verify_value = False
dict_audioroom_lecture_value = {
    'name' : 'Lecture',
    'service_type' : 'lecture',
    'aliases' : [{'alias' : 'lecture@example.com'}]
    }
data_value = json.dumps(dict_audioroom_lecture_value)

"""
#execute request, take response and give answer to variable response
response = requests.post(
    address,
    auth=auth_value,
    verify = verify_value,
    data=data_value
    )

print("Created new Virtual Audioroom:", response.headers['location'])


### deploying a new conferencing node ###

address_for_deploying a new conferencing node_value = 'https://<manageraddress>/api/admin/configuration/v1/worker_vm/'
auth_value = ('user1', 'pass1') #переопределение переменных, объявленных выше! PAY ATTENTION! May require to rebuild
verify_value = False  #переопределение переменных, объявленных выше! PAY ATTENTION! May require to rebuild

dict_for_deploying a new conferencing node_value = {
    'name': 'new_node',
    'hostname': 'newnode',
    'domain' : 'example.test',
    'address': '<newnode_ip_adress>',
    'netmask': '<newnode_ip_mask>',
    'gatevay': '<newnode_gateway>',
    'password': '<newnode_password>',
    'system_location': 'api/admin/configuration/v1/system_location/1/',
    'deployment_type': 'VMWARE',
    'host': 1,
    'host_username': '<vcenter_username>',
    'host_password': '<vcenter_password>',
    'host_network': 'VM Network',
    'host_resource_path': '/<vmware_datacenter>/host/<vmware_host>/Resources',
    'vm_cpu_count': '8',
    'vm_system_memory': '16384'
}
data_value_for_deploying a new conferencing node = json.dumps(dict_for_deploying a new conferencing node_value)

response_for_dncn = requests.post(
    address_for_deploying a new conferencing node_value,
    auth=auth_value,
    verify = verify_value,
    data=data_value_for_deploying a new conferencing node
    )


print("Created new Conferencing Node:", response_for_dncn.headers['location'])
'''

#Creating multiple Virtual Meeting Rooms
#Multiple Virtual Meeting Rooms can be created using a PATCH request.

data = {
    'objects' : [
        {'name' : 'VMR_1', 'service_type': 'conference', 'aliases' : [{'alias' : 'meet1@example.com'}]},
        {'name' : 'VMR_2', 'service_type': 'conference', 'aliases' : [{'alias' : 'meet2@example.com'}]},
    ]
}

request_for_creating_multiple_virtual_meeting_rooms = 'https://%s/api/admin/configuration/v1/conference/' % host

response = requests.patch(
    request_for_creating_multiple_virtual_meeting_rooms,
    auth=auth_value,
    verify=verify_value,
    data=json.dumps(data)
)

#Getting a Virtual Meeting Room
#By submitting a GET to the resource URI of the new Virtual Meeting Room, you can get the Virtual Meeting Room configuration:

request_for_getting_a_virtual_meeting_room = 'https://%s/api/admin/configuration/v1/conference/3' % host

response = requests.get(
    request_for_getting_a_virtual_meeting_room,
    auth=auth_value,
    verify=verify_value
)
print("Virtual Meeting Room:", json.loads(response.text))


#Getting all active Virtual Meeting Room conferences

adress_for_getting_all_active_virtual_meeting_room = 'https://%s/api/admin/status/v1/conference/?service_type=conference' % host
response = requests.get(
    adress_for_getting_all_active_virtual_meeting_room,
    auth=auth_value,
    verify=verify_value
)

print("Active conferences:", json.loads(response.text)['objects'])


# Getting all active conference instances

adress_for_getting_all_active_conference_instances = "https://%s/api/admin/status/v1/conference/" % host

response = requests.get(adress_for_getting_all_active_conference_instances,
    auth=auth_value,
    verify=verify_value
    )
print("Active conferences's instance:", json.loads(response.text)['objects'] )

addr= 'https://185.35.201.84/admin/conferencing/conference/add'

"""
# ВЫЗОВ АБОНЕНТА!!! Dialing a participant into a conference

class Participant:

    def __init__(self, destination_alias, conference_alias, host):
        #constructor

        self.destination_alias = destination_alias
        self.conference_alias = conference_alias
        self.server_host = host

    def dialing_a_participant_into_a_conference(self):
        #dial to participant

        self.address_for_dialing_a_participant_into_a_conference = "https://%s/api/admin/command/v1/participant/dial/" % self.server_host

        data_value_dialing_a_participant_into_a_conference = {
            'conference_alias': self.conference_alias,
            'destination': self.destination_alias,
            'protocol': 'h323',
            'node': '185.35.201.92',
            'role': 'chair',
        }

        print(data_value_dialing_a_participant_into_a_conference)
        response = requests.post(
            self.address_for_dialing_a_participant_into_a_conference,
            auth=auth_value,
            data=data_value_dialing_a_participant_into_a_conference,
            verify=verify_value
        )

        self.resp_of_server= str(response.content, encoding='utf8')

        self.id_of_a_participant = json.loads(self.resp_of_server)['data']['participant_id']

        print("New participant created:", json.loads(self.resp_of_server)['data']['participant_id'])

        return self.id_of_a_participant



def dialing_a_participant_into_a_conference():

    address_for_dialing_a_participant_into_a_conference = "https://%s/api/admin/command/v1/participant/dial/" % host

    data_value_dialing_a_participant_into_a_conference = {
        'conference_alias': 'meet1@example.com',
        'destination': 'Dmitry',
        'protocol': 'h323',
        'node': '185.35.201.92',
        'role': 'chair',
    }

    print(data_value_dialing_a_participant_into_a_conference)
    response = requests.post(
        address_for_dialing_a_participant_into_a_conference,
        auth=auth_value,
        data=data_value_dialing_a_participant_into_a_conference,
        verify=verify_value
    )

    resp_of_server= str(response.content, encoding='utf8')

    id_of_a_participant = json.loads(resp_of_server)['data']['participant_id']

    print("New participant created:", json.loads(resp_of_server)['data']['participant_id'])

    return id_of_a_participant

"""
#json.loads(response.content)

#Getting all participants for a conference

address_for_getting_all_participants_for_a_conference = "https://%s/api/admin/status/v1/participant/?conference=VMR_1" % host

response = requests.get(
    address_for_getting_all_participants_for_a_conference,
    auth=auth_value,
    verify=verify_value
)

print("Active participants for VMR_1:", json.loads(response.text)['objects'])

time.sleep(15)
#Disconnecting a participant

addr_for_disconnecting_a_participant = "https://%s/api/admin/command/v1/participant/disconnect/" % host

data_a_participant = {'participant_id': id_of_a_participant, }

response = requests.post(
    addr_for_disconnecting_a_participant,
    auth=auth_value,
    data=data_a_participant,
    verify=verify_value)

"""