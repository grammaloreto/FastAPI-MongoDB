def sstEntity(temperature) -> dict:
    return {
        'id': str(temperature['_id']),
        'sst1': temperature['sst1'],
        'sst2': temperature['sst2'],
        'sst3': temperature['sst3'],
        'sst4': temperature['sst4'],
        'sst5': temperature['sst5'],
        'sst6': temperature['sst6'],
        'sst7': temperature['sst7'],
        'sst8': temperature['sst8'],
        'sst9': temperature['sst9'],
        'sst10': temperature['sst10'],
        'sst11': temperature['sst11']
    }

def sstsEntity(entity) -> list:
        return [sstEntity(temperature) for temperature in entity]
