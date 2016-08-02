
def get_map_gtype(match_details):

    map_dic = { 'cbcea2c0-f206-11e4-8c4a-24be05e24f7e' : 'Riptide',
                'caacb800-f206-11e4-81ab-24be05e24f7e' : 'Plaza',
                'ce89a40f-f206-11e4-b83f-24be05e24f7e' : 'Tyrant',
                'c7805740-f206-11e4-982c-24be05e24f7e' : 'Glacier',
                'cb914b9e-f206-11e4-b447-24be05e24f7e' : 'Rig',
                'c7b7baf0-f206-11e4-ae9a-24be05e24f7e' : 'Parallax',
                'ca737f8f-f206-11e4-a7e2-24be05e24f7e' : 'Overgrowth',
                'ce1dc2de-f206-11e4-a646-24be05e24f7e' : 'Truth',
                'cebd854f-f206-11e4-b46e-24be05e24f7e' : 'Coliseum',
                'cc74f4e1-f206-11e4-ad66-24be05e24f7e' : 'Torque',
                'cc3ca6d1-f206-11e4-87c3-24be05e24f7e' : 'Stasis',
                'cc040aa1-f206-11e4-a3e0-24be05e24f7e' : 'Fathom',
                'cae999f0-f206-11e4-9835-24be05e24f7e' : 'Array',
                'cdb934b0-f206-11e4-8810-24be05e24f7e' : 'Empire',
                'c74c9d0f-f206-11e4-8330-24be05e24f7e' : 'Alpine',
                'cd844200-f206-11e4-9393-24be05e24f7e' : 'Eden',
                'cdee4e70-f206-11e4-87a2-24be05e24f7e' : 'Regret'}

    gtype_dic = { '67ffc2ff-a50e-4e5d-ae08-b40e3d961061' : 'Campaign Test',
                  '1571fdac-e0b4-4ebc-a73a-6e13001b71d3' : 'Strongholds',
                  'a2949322-dc84-45ab-8454-cf94fb28c189' : 'Capture the Flag',
                  'f6051f51-bbb6-4ccc-8ac0-cf42b7291c76' : 'Infection',
                  'dfd51ee3-9060-46c3-b131-08d946c4c7b9' : 'Warzone Firefight',
                  '00000003-0000-0010-8000-00aa00389b71' : 'Campaign',
                  '257a305e-4dd3-41f1-9824-dfe7e8bd59e1' : 'Slayer',
                  '42f97cca-2cb4-497a-a0fd-ceef1ba46bcc' : 'Warzone Assault',
                  '8d4a3dbc-ef7a-405e-862b-34093ff582fd' : 'Big Team CTF',
                  '1e473914-46e4-408d-af26-178fb115de76' : 'Breakout',
                  'b0df8938-0fb6-42ee-846f-a0c3593344d5' : 'Assault',
                  'b45854a7-e6e1-4a9c-9104-139934511779' : 'Big Team Strongholds',
                  'dda182c5-4b50-4a0f-86f3-fcb5e0db4df3' : 'Grifball',
                  'f6de5351-3797-41e9-8053-7fb111a3a1a0' : 'Warzone',
                  '65f033d2-1303-4748-bc26-ef62c38eced4' : 'Big Team Slayer' }


    map_name = map_dic[ match_details['MapId'] ]
    date = match_details['MatchCompletedDate']['ISO8601Date'][0:-10]
    gtype = gtype_dic[match_details['GameBaseVariantId']]

    return [date, map_name, gtype]
